"""
풀이시간: 40분

<input>
- n: 행의 개수(3 <= m <= 300)
- m: 열의 개수(3 <= m <= 300)

<solution>
1. 각 빙산 좌표에서 BFS를 통해 빙산이 몇 칸의 인접한 바다가 있는 만큼 빙산을 녹여준다.
2. 빙산이 모두 녹을 때까지 또는 빙산이 두 개 이상으로 분리될 때까지 시간을 증가시키며 반복한다.

<시간복잡도>
O(10 * k * n*m)
- 10: 빙산 한 겹이 사라지는데 걸리는 시간
- k: 빙산의 겹은 최대 100
- n*m: 빙산 하나에 대한 BFS
"""
import sys

input = sys.stdin.readline
from collections import deque


# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 행, 열의 개수
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 그래프(빙산과 바다 정보)
ice = set()  # 빙산 좌표

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:  # 빙산
            ice.add((i, j))


def bfs(x, y):  # 빙산 좌표 BFS
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):  # 인접한 네 방향을 모두 살펴봄
            nx, ny = x + dx[i], y + dy[i]
            if not visited[nx][ny]:  # 아직 방문하지 않은 칸
                if (
                    graph[nx][ny] == 0 and graph[x][y] != 0
                ):  # 인접한 칸이 바다(0)이고, 현재 위치는 빙산일 때
                    graph[x][y] -= 1  # 빙산을 1 녹임
                if graph[nx][ny] != 0:  # 인접한 칸이 빙산일 경우 -> 방문처리 후 큐에 추가
                    visited[nx][ny] = True
                    q.append((nx, ny))
        if graph[x][y] == 0:  # 바다에 의해 다 녹아버리는 빙산 좌표를 제거
            ice.remove((x, y))


year = 0  # 빙산이 분리되는 최초의 시간(년)
while True:
    cnt = 0  # 분리된 빙산의 수
    visited = [[False] * m for _ in range(n)]  # 방문처리 배열
    ice_berg = ice.copy()
    for r, c in ice_berg:  # 빙산에 대해 BFS
        if graph[r][c] != 0 and not visited[r][c]:
            bfs(r, c)
            cnt += 1
    # 빙산이 두 개 이상으로 분리된 경우
    if cnt >= 2:
        print(year)
        break
    # 빙산이 분리되지 않은 경우
    if cnt == 0:
        print(0)
        break
    year += 1
