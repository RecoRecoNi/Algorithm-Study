"""

풀이시간
- 약 1시간 30분 -> 풀이 실패 후 답지 참고

접근법
- 그래프 탐색 + 최단 거리 -> BFS 활용해보자
    - 초기에 더러운 곳의 개수를 세고, BFS 내에서 "*" 를 발견하면 "." 으로 바꾸고 count += 1
    - 이후 count 가 더러운 곳의 개수와 같아질 때 탈출하도록 설계

- "같은 칸을 여러번 방문할 수 있다" 를 잘 처리해보자
    - 여러 번 방문할 수 있지만, 최대한 방문하지 않는 편이 좋지 않을까..? -> 문제에 풀어내는 법은 잘 모르겠음
    - 해당 조건 때문에 방문 배열이 필요없다고 생각했는데 아니었음

- 더러운 칸 10개가 최대 -> 그냥 거리를 다 구하는 방법도 있을 것 같다
    - 하지만 중간에 x 가 있으면 얘기가 달라짐 -> 하면 안될 듯

- 풀이 실패로 답지 참고
    - 알고보니 위에서 말한 거리를 다 구하는 방법을 BFS 로 해결하면 되는데 너무 복잡하게 생각한 것 같음 ㅠ ㅠ

회고
- 왜 대각선 움직임은 고려하지 않는건지 잘 모르겠음..?!
- 순열을 통해 더러운 곳의 방문 순서를 정의하는 것이 인상적
    - 더러운 칸 간의 거리를 쪼개서 미리 구해놓고 순열을 통해 풀어냈음
        - 본인 풀이는 어떻게 한 번에 청소를 다 할때까지의 거리를 구해야하나 고민했는데... 대단하다...
    - 더러운 칸의 개수가 최대 10개인 것이 힌트라고 볼 수도 있을 것 같음

"""

from collections import deque
from itertools import permutations
import sys

inputs = sys.stdin.readline

# 상하좌우 움직임 정의
direction = [(0, 1), (0,-1), (-1, 0), (1, 0)]

# BFS 함수를 정의
def bfs(x, y):
    queue = deque()
    
    # 방문 여부와 이동 거리를 저장할 배열을 생성
    visit = [[0]*w for _ in range(h)]
    queue.append([x, y])
    visit[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            # 범위 내에 있고, 가구('x')가 아니며, 아직 방문하지 않았다면 이동 거리를 업데이트하고 큐에 추가
            if 0 <= nx < h and 0 <= ny < w:
                if room[nx][ny] != 'x' and not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append([nx, ny])
    return visit

while True:
    # 가로와 세로 크기를 입력받습니다.
    w, h = map(int, inputs().split())
    if not (w and h): # 0 과 0, 즉 마침을 나타내는 입력이 들어왔을 때 출력을 멈춤
        break

    room, dirty = [], []
    for i in range(h):
        # 방 정보를 입력받아 2차원 배열 room 에 저장
        row = list(inputs().strip())
        room.append(row)
        
        for j, k in enumerate(row):
            if k == 'o':
                sx, sy = i, j  # 로봇 청소기의 시작 위치 저장
            elif k == '*':
                dirty.append([i, j])  # 더러운 칸의 위치 저장

    r2d, flag = [], 0 # r2d -> robot to dirty
    visit = bfs(sx, sy)  # 로봇 청소기에서 더러운 칸까지의 거리 계산
    
    for i, j in dirty:
        if not visit[i][j]:  # 방문할 수 없는(즉 방문하지 않은) 더러운 칸이 있는 경우
            flag = 1
            break
        r2d.append(visit[i][j]-1)  # 로봇 청소기에서 더러운 칸까지의 거리 저장
    if flag: # 더러운 칸이 안 없어졌다면 -1 반환
        print(-1)
        continue

    d2d = [[0]*len(dirty) for _ in range(len(dirty))] # d2d -> dirty to dirty
    
    for i in range(len(dirty)-1): # 이중 반복문으로 하나의 더러운칸과 다른 더러운 칸을 탐색
        dirty_x, dirty_y = dirty[i][0], dirty[i][1]
        visit = bfs(dirty_x, dirty_y)  # 하나의 더러운 칸에서 다른 더러운 칸까지의 거리 계산
        
        for j in range(i+1, len(dirty)):
            d2d[i][j] = visit[dirty[j][0]][dirty[j][1]]-1 # 거리 저장
            d2d[j][i] = d2d[i][j] # 양 측의 거리는 같음

    p = list(permutations([i for i in range(len(d2d))])) # 순열을 통해 더러운 곳의 방문 순서를 정의
    
    ans = sys.maxsize # 최대 거리 정의 후 앞으로 갱신할 것
    for i in p:
        dist = 0
        dist += r2d[i[0]] # 로봇부터 더러운 곳의 거리 계산
        nfrom = i[0] # 출발 지점
        for j in range(1, len(i)):
            nto = i[j] # 도착지점
            dist += d2d[nfrom][nto] # 출발지점과 도착지점간의 계산해놓은 거리 갱신
            nfrom = nto
        ans = min(ans, dist)  # 모든 순열을 비교하여 최솟값을 찾음 (즉 방문순서 별 최소 거리)
    print(ans)
