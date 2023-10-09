"""
풀이시간: 40분

<input>
n: 격자의 크기(2 ≤ n ≤ 4)
m: 순서대로 방문해야 하는 칸의 수(2 ≤ m ≤ n^2)

n개의 수(0 or 1)
- 0: 빈 칸
- 1: 벽

방문해야할 m개의 칸 (x, y)가 주어진다
- 주어진 칸에 벽이 있는 경우능 없고, 중복도 없다.

<solution>
n과 m이 매우 작기 때문에 DFS를 통해 모든 경우의 수를 확인한다.(브루트 포스)
이 때, 더 이상 다음 칸으로 이동할 수 없다면 탐색을 포기한다.(백트래킹)

<시간복잡도>
O(N^2)
"""
import sys
input = sys.stdin.readline


def dfs(cur_x: int, cur_y: int, nxt_idx: int):
    """
    cur_x: 시작 칸의 x좌표
    cur_y: 시작 칸의 y좌표
    nxt_idx: 다음 칸의 인덱스
    """
    global cnt
    # 다음 칸에 도달한 경우
    if cur_x == go[nxt_idx][0] and cur_y == go[nxt_idx][1]:
        # 1) 마지막 칸까지 도달했다면 경우의 수를 1 증가시키고 종료
        if nxt_idx == m-1:
            cnt += 1
            return
        # 2) 이동한 칸이 마지막 칸이 아니라면 방문해야할 칸의 idx 증가
        else:
            nxt_idx += 1

    # 현재 위치 방문처리
    visited[cur_x][cur_y] = True

    for k in range(4):
        nx, ny = cur_x+dx[k], cur_y+dy[k]
        if (0 <= nx < n and 0 <= ny < n) and board[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny, nxt_idx)

    visited[cur_x][cur_y] = False


# n: 격자의 크기, m: 순서대로 방무해야 하는 칸의 수
n, m = map(int, input().split())
# 격자판(0: 빈 칸, 1: 벽)
board = [list(map(int, input().split())) for _ in range(n)]
# 방문처리 배열
visited = [[False] * n for _ in range(n)]

# 방문해야할 칸의 좌표
go = []
for _ in range(m):
    x, y = map(int, input().split())
    go.append((x-1, y-1))

# 상, 하, 좌, 우 방향으로 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 경우의 수
cnt = 0
# 순차적으로 방문
dfs(go[0][0], go[0][1], 1)
print(cnt)