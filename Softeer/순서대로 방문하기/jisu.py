"""
풀이 시작 : 2023-10-08 14:41

#### 제한 조건
- 2 <= n <= 4
- 2 <= m <= 16

#### 풀이
- 방문 지점의 방문 순서를 matrix에 기록
    - '0' : 빈 칸 / '1' : 벽 / 0 ~ m : 방문 지점
- 스킬트리 문제처럼, 특정 방문 지점에 방문하기 위해서는 직전 지점이 방문되어야 함
    - 다음 지점이 방문 지점인 경우, 직전 지점이 방문된 경우에만 탐색하도록 dfs
- 마지막 방문 순서에 해당하는 지점을 탐색하면 경우의 수 +1 후 dfs 종료

풀이 완료 : 2023-10-08 15:19 (풀이 시간 : 38분)
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

matrix = [list(input().rstrip().split()) for _ in range(n)]

for i in range(m):
    y, x = map(int, input().rstrip().split())
    matrix[y - 1][x - 1] = i  # 방문해야 되는 순서를 matrix에 기록
    # '0' : 빈 칸 / '1' : 벽 / 0 ~ m : 방문 지점

    if i == 0:
        st_y, st_x = y - 1, x - 1  # 시작 좌표 저장

order = [False for _ in range(m)]  # 특정 순서의 지점이 방문되었는지 관리
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0


def dfs(y, x):
    global cnt

    if matrix[y][x] == m - 1:  # 마지막 순서에 해당하는 번호를 방문하면
        cnt += 1  # 탐색 성공
        return

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx

        if (
            0 <= ny < n
            and 0 <= nx < n
            and matrix[ny][nx] != "1"
            and not visited[ny][nx]
        ):
            if matrix[ny][nx] == "0":  # 일반 빈 칸의 경우
                visited[ny][nx] = True
                dfs(ny, nx)  # 이어서 탐색
                visited[ny][nx] = False
            else:  # 방문 지점에 해당하는 경우
                if order[matrix[ny][nx] - 1]:  # 해당 방문 지점의 직전 지점이 방문된 경우에만
                    visited[ny][nx] = True
                    order[matrix[ny][nx]] = True
                    dfs(ny, nx)  # 이어서 탐색
                    visited[ny][nx] = False
                    order[matrix[ny][nx]] = False


# 첫번째 방문해야 하는 순서부터 dfs 시작
visited[st_y][st_x] = True
order[0] = True
dfs(st_y, st_x)

print(cnt)
