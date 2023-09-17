"""

풀이시간
- 약 20분

접근법
- 그래프 탐색, 최단거리 -> BFS

회고
- 기본적인 문제, 행과 열 헷갈려서 버벅거리지말고 차분히 풀자!

"""

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    direction = [[0,-1], [0,1], [-1, 0], [1, 0]] # 상하좌우

    queue = deque()
    queue.append([0, 0]) # 시작점(0,0)과 종료점(n-1, m-1)이 고정
    maps[0][0] += 1
    
    while queue:
        x, y = queue.popleft()
        
        for dir in direction:
            nx, ny = x + dir[0], y + dir[1]
                
            if (0 <= nx < n) and (0 <= ny < m):
                if maps[nx][ny]==1: # 벽이 없으면 지나가기
                    queue.append([nx, ny])
                    maps[nx][ny] = maps[x][y] + 1

    return maps[n-1][m-1]-1 if maps[n-1][m-1]>1 else -1