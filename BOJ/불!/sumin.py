"""
풀이시간: 35분

<input>
1 ≤ R, C ≤ 1000
- R: 미로 행의 개수
- C: 열의 개수

<solution>
이 문제의 경우 불과 지훈이가 동시에 이동하기 때문에, 이 처리를 어떻게 해줄 것인지가 관건인 문제다.
하지만, 불은 1분에 인접한 네 방향으로 모두 이동지만, 지훈이의 경우 한 칸 밖에 이동하지 못한다.
따라서 둘에 대해 각각의 BFS 확인해 각 칸에 도착하는데 걸리는 이동 시간을 확인하면 된다.
불의 전파시간에 대한 BFS를 먼저 확인 후, 지훈이의 이동에 대한 BFS를 돌면 되는데 이 때 다음의 조건을 확인하면 된다.
- 지훈이가 도착할 예정시간보다 불이 해당 칸에 전파되는 시간이 더 짧은 경우(지훈이가 도착하면 이미 불이 붙어있기 때문에 탈출 실패)

<시간복잡도>
BFS 시간복잡도: O(R*C), 최대 1,000,000번 연산
"""
import sys

input = sys.stdin.readline
from collections import deque

# 행과 열 입력받기
r, c = map(int, input().split())

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire = [[-1] * c for _ in range(r)]  # 불의 전파 시간
jihoon = [[-1] * c for _ in range(r)]  # 지훈이의 이동 시간


q1 = deque()  # 불의 전파에 대한 BFS 돌기 위한 큐
q2 = deque()  # 지훈이 이동에 대한 BFS 돌기 위한 큐
board = [list(input()) for _ in range(r)]  # 미로
for i in range(r):
    for j in range(c):
        if board[i][j] == "F":  # 불
            q1.append((i, j))
            fire[i][j] = 0
        elif board[i][j] == "J":  # 지훈
            q2.append((i, j))
            jihoon[i][j] = 0


# 불에 대한 BFS
while q1:
    x, y = q1.popleft()
    for i in range(4):  # 현재위치에서 상하좌우 위치 확인
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue  # 미로의 범위를 벗어난 경우 무시
        if fire[nx][ny] >= 0 or board[nx][ny] == "#":
            continue  # 이미 방문한 노드이거나, 벽인 경우 무시
        fire[nx][ny] = fire[x][y] + 1
        q1.append((nx, ny))

# 지훈이에 대한 BFS
while q2:
    x, y = q2.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:  # 범위를 벗어났다는 것은 탈출에 성공했다는 의미
            print(jihoon[x][y] + 1)  # 탈출한 시간 출력
            exit()
        if jihoon[nx][ny] >= 0 or board[nx][ny] == "#":
            continue
        if fire[nx][ny] != -1 and fire[nx][ny] <= jihoon[x][y] + 1:
            continue  # 불의 전파 시간을 조건에 추가 (지훈이의 도착시간보다 불이 먼저 붙을 곳)
        jihoon[nx][ny] = jihoon[x][y] + 1
        q2.append((nx, ny))

print("IMPOSSIBLE")  # 탈출에 실패
