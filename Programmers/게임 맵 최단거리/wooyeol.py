"""
    게임 맵 최단거리
    https://school.programmers.co.kr/learn/courses/30/lessons/1844

    풀이시간 
    20:25 ~ 20:37 (12분)
    
    문제 조건
    Maps = N x M

    1 <= N <= 100
    1 <= M <= 100

    시간 복잡도 : 
    O(N * M) = O(10,000)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> BFS

    전형적인 BFS 알고리즘을 사용한 풀이
"""

from collections import deque

def bfs(start,maps):
    # BFS 탐색을 위한 deque
    queue = deque([start])
    
    # 하,상,좌,우
    directions = ((0,1),(0,-1),(-1,0),(1,0))
    
    # 방문 노드 기억하기
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    visited[start[0]][start[1]] = True
    
    # BFS 탐색
    while queue:
        x,y = queue.popleft()
        
        # 4방향으로 검사
        for dx,dy in directions:
            nx,ny = x + dx, y + dy
            # 맵 밖으로 나가지 않고
            if 0 <= nx < len(visited) and 0 <= ny < len(visited[0]):
                # 벽이 아니고 방문한 적이 없다면
                if maps[nx][ny] > 0 and not visited[nx][ny]:
                    # 다음 방문 노드 추가 및 방문 처리와 현재까지 걸린 시간 업데이트
                    queue.append((nx,ny)) # 다음 방문 노드 추가
                    maps[nx][ny] += maps[x][y] # 현재까지 걸린 시간
                    visited[nx][ny] = True # 방문 처리
    
    # 예외처리 : n,m 진영이 1이라면 방문할 수 없는 것
    return maps[-1][-1] if maps[-1][-1] > 1 else -1
    

def solution(maps):
    return bfs((0,0),maps)

case1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] # 11
case2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] # -1

print(solution(case1))
print(solution(case2))