'''
풀이 시작 : 2023.08.15 21:00

- 불은 4방향으로 확산 되며, 지훈님도 상하좌우로 이동할 수 있다.
- BFS를 활용해서 지훈님과 불의 각 time step 별로 이동 경로를 정의한다.
- BFS를 위한 지훈님과 불의 queue를 별도로 정의해야 하며, queue에는 다음 time step에서 이동 경우의 좌표와 timestep을 함께 관리한다.

-  지훈님 초기 위치 판별을 위한 로직 필요
-  불이 timestep 마다 번지므로 이를 어떻게 관리할지 고려 필요
    - visited의 각 좌표 별 원소를 [방문 여부, 불 탄 time step]으로 표시하면 될 듯
    - 그러면 지훈님은 아직 방문하지 않은 곳(visited[0])과 현재 시점에서 아직 불에 타지 않은 곳 (timestep < visited[1])에 갈 수 있다.
- 불과 지훈님이 동시에 특정 지점에 닿으면 안되므로, 일단 불부터 이동시켜야 함
- 그리고 큐에는 timestep마다 갈 수 있는 곳이 담기는데, 각 timestep마다 지훈님이 갈 수 있는 곳, 불이 갈 수 있는 곳이 다르게 담긴다.
    - 별도의 변수를 둬서 시간 동기화가 필요하다.

풀이 완료 : 2023.08.15 23:00
'''
import sys
from typing import List, Deque, Tuple
from collections import deque

input = sys.stdin.readline

MAP: List[List[str]] = list()               # MAP과 visited는 전역으로 사용할 것임
visited: List[List[List]] = list()
NOTVISIT: int = 1000001                     # 불이 아직 안번졌음을 나타내는 변수
dy: List[int] = [-1, 1, 0, 0]               # BFS 좌표 변경에 활용할 변수
dx: List[int] = [0, 0, -1, 1]

def BFS(jihun_init: Tuple[int, int, int], fire_init: List[Tuple[int, int, int]]) -> int:
    q_j: Deque = deque([jihun_init])        # 지훈 이동 경로를 담을 queue
    q_f: Deque = deque(fire_init)           # 불 이동 경로를 담을 queue
    S: int = 0                              # timestep 동기화를 위한 변수

    # 초기 방문 처리
    visited[jihun_init[0]][jihun_init[1]][0] = True         # 지훈 초기 위치 방문 처리
    for y, x, timestep in fire_init:                        # 불 초기 위치 방문 처리
        visited[y][x][1] = timestep                             # NOTVISIT -> 0

    # BFS
    while q_j or q_f:                               # 두 queue가 다 죽을 때까지                        
        while q_f and S == q_f[0][2]:               # 불 이동 BFS & 시간 동기화
            y, x, timestep = q_f.popleft()
            for d in range(4):                          # 상, 하, 좌, 우 이동
                ny, nx = y+dy[d], x+dx[d]                   # 이동한 다음 좌표
                if (0 <= ny < len(MAP)) and (0 <= nx < len(MAP[0])) and (MAP[ny][nx] != '#') and (visited[ny][nx][1] == NOTVISIT):          # 아직 불이 번지지 않은 지점 및 예외처리
                    q_f.append((ny, nx, timestep+1))      # 큐에 다음 불이 번지는 좌표와 시점 push
                    visited[ny][nx][1] = timestep+1         # 불이 번진 시점 저장
                                             
        while q_j and S == q_j[0][2]:                   # 지훈님 이동 BFS & 시간 동기화
            y, x, timestep = q_j.popleft()
            
            # 정답 조건
            if y in {0, len(MAP)-1} or x in {0, len(MAP[0])-1}:     # 가장자리에 도달했을 경우
                return timestep+1                                   # 탈출 가능 (0부터 시작했으므로 +1)

            for d in range(4):                                      # 상, 하, 좌, 우 이동
                ny, nx = y+dy[d], x+dx[d]                               # 이동한 다음 좌표
                if (0 <= ny < len(MAP)) and (0 <= nx < len(MAP[0])) and (MAP[ny][nx] == '.') and (not visited[ny][nx][0]) and (timestep+1 < visited[ny][nx][1]):        # 아직 방문하지 않은 지점 및 불이 아직 번지지 않은 지점(timestamp가 불이 번진 시점 이전인 경우) 및 예외처리
                    q_j.append((ny, nx, timestep+1))                    # 다음 좌표와 이동한 시점 push
                    visited[ny][nx][0] = True                           # 다음 좌표 방문 처리

        S += 1      # 1초 경과

    return -1   # 반복문을 탈출한 경우 탈출할 수 있는 경우가 없는 것

def solution() -> str:
    global MAP, visited
    R, C = map(int, input().rstrip().split())
    c_j: int = -1                       # 지훈님 초기 위치 담을 변수
    c_f: List[int] = list()             # 불 초기 위치 담을 리스트

    for r in range(R):                  # map 입력 받으면서 지훈님과 불 초기 위치 파악
        rows = input().rstrip()

        if c_j == -1:                   # 지훈님 초기 위치 찾기, 아직 못찾았을 때만 로직이 실행되도록 구현
            c_j = rows.find('J')
            if c_j != -1:               # 찾았을 경우 지훈님 위치 최종 업데이트
                c_j = (r, c_j, 0)

        c_f += [(r, idx, 0) for idx, col in enumerate(rows) if col == 'F']  # 초기 불 위치 찾기, 불이 여러 개일 수 있음

        MAP.append(rows)

    visited = [[[False, NOTVISIT] for _ in range(C)] for _ in range(R)]     # [지훈 방문 여부, 불 번진 시간] 을 관리하는 visit list
    answer = BFS(c_j, c_f)

    print('IMPOSSIBLE' if answer == -1 else answer)

solution()