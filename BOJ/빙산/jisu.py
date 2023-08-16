'''
풀이 시작 : 2023-08-16 10:20

- N과 M은 최대 300 -> O(N^2) 보다 훨씬 이상도 가능, 전형적인 그래프 탐색 문제로 접근
- 1년에 해당하는 time step 마다 모든 좌표에서 BFS를 실행
- 이 때 BFS가 처음으로 두 번 이상 실행되는 time step을 구하면 될 것 같다.
- 한 번 BFS를 돌릴 때마다 현재 방문 중인 빙산은 인접한 바다 방면만큼 줄이기
    - 특정 빙산이 1 -> 0이 되는 경우 애초에 바다로 인식할 수 있으므로, 이동할 경로를 먼저 담고 빙산을 줄이자.

풀이 완료 : 2023-08-16 10:55
'''

import sys
from typing import List, Tuple, Deque
from collections import deque

input = sys.stdin.readline

MAP: List[List[int]] = list()           # MAP과 visited는 전역으로 활용할 것임
visited: List[List[bool]] = list()
dy = [-1, 1, 0, 0]                      # BFS시 다음 좌표 탐섹에 활용
dx = [0, 0, -1, 1]

def BFS(init: Tuple[int, int]):         # BFS : 빙산의 이어진 부분을 탐색
    global MAP, visited

    queue: Deque = deque([init])        # 초기 좌표 세팅 
    visited[init[0]][init[1]] = True    # 초기 좌표 방문 처리

    while queue:
        y, x = queue.popleft()
        
        decreaseCount: int = 0          # 현재 빙산이 바닷물에 닿아 없어질 높이 카운트
                                        # 이렇게 카운트 했다가 마지막에 한 번에 때는 이유는 line 7 설명에 의거
        for d in range(4):                  # 상, 하, 좌, 우 탐색
            ny, nx = y+dy[d], x+dx[d]

            if (0 <= ny < len(MAP)) and (0 <= nx < len(MAP[1])) and not visited[ny][nx]:    # 좌표 예외 처리 및 방문하지 않은 좌표 탐색
                if MAP[ny][nx]:                 # 다음 좌표가 빙산인 경우
                    queue.append((ny, nx))          # 큐에 다음 경로 append
                    visited[ny][nx] = True          # 해당 좌표 방문 처리
                else:                           # 다음 좌표가 바다인 경우
                    decreaseCount += 1              # 없어질 빙산 높이 카운트

        MAP[y][x] = max(0, MAP[y][x]-decreaseCount)     # 높이는 음수가 될 수 없음

    return 1        # 한 이어진 빙산 탐색이 끝나면 한 개의 덩어리임을 나타내는 1 반환

def solution() -> int:
    global MAP, visited
    
    BFSCount: int = 1           # 한 time step에 빙산이 몇 덩어리인지 나타낼 변수
    S: int = 0                  # time step 변수

    R, C = map(int, input().rstrip().split())

    MAP = [list(map(int, input().rstrip().split())) for _ in range(R)]
    
    while BFSCount == 1:        # 덩어리가 2개 이상이거나 없어질 때까지 반복
        BFSCount = 0
        S += 1                  # time step update
        visited = [[False for _ in range(C)] for _ in range(R)]
        for r in range(R):                              # 모든 좌표에 걸쳐 빙산이 몇 덩어리인지 계산(BFS가 몇번 실행되는지)
            for c in range(C):
                if MAP[r][c] and not visited[r][c]:
                    BFSCount += BFS((r, c))

    print(0 if BFSCount == 0 else S-1)      # 위 반복문을 탈출한 경우 빙산의 덩어리 개수는 0개 or 2개 이상, 2개 이상인 경우 시점 출력
                                            # S-1인 이유는 최종 시점에 S += 1이 한 번 더 반영되므로 이를 고려해 줌
solution()