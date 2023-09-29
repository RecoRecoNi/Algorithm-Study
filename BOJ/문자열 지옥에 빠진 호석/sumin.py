"""
풀이시간: 30분

<input>
N행 M열의 격자(각 칸에 알파벳이 써있고, 환형으로 이어진다)
아무 곳에서 시작해 상하좌우나 대각선 방향의 칸으로 한 칸씩 이동할 수 있다. (이미 지나왔던 칸들을 다시 방문하는 것은 허용)
시작하는 격자의 알파벳을 시작으로, 이동할 때마다 각 칸에 써진 알파벳을 이어 붙여 문자열을 만든다.
각 문자열마다 만들 수 있는 경우의 수를 구해라.(방문 순서가 다르면 다른 경우)
ex. (1, 1) -> (1, 2) != (1, 2) -> (1, 1)

- n, m: 격자의 크기(3 ≤ N, M ≤ 10, 자연수)
- k: 신이 좋아하는 문자열의 개수(1 ≤ K ≤ 1,000, 자연수)
- 1 ≤ 신이 좋아하는 문자열의 길이 ≤ 5

<solution>
n과 m이 매우 작기 때문에 DFS 탐색(아무 곳에서 시작할 수 있으니 모든 좌표를 탐색)
문자열의 길이는 최대 5이므로 그 이후는 탐색 x
문자열을 만들 때마다 딕셔너리에 해당 문자열의 경우의 수를 + 1 해준다.

<시간복잡도>
O(N * M * 8^5)
- dfs 함수는 각 칸에서 재귀적으로 최대 8개의 인접한 칸을 탐색하고, 최대 깊이 5까지 탐색할 수 있음: O(8^5)
- 모든 칸에 대해서 시작할 수 있음: O(NM)
"""
import sys
input = sys.stdin.readline
from collections import defaultdict


# 상하좌우, 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

cnt = defaultdict(int) # 각 문자열이 등장하는 경우의 수
def dfs(x: int, y: int, s: str) -> None:
    # 문자열 s가 등장한 경우의 수를 1추가
    cnt[s] += 1
    if len(s) == 5: # 문자열의 길이는 최대 5이기 때문에 더 이상 탐색 x
        return
    for k in range(8):
        nx, ny = (x+dx[k]) % n, (y+dy[k]) % m
        dfs(nx, ny, s+board[nx][ny])

# 격자의 크기, 신이 좋아하는 문자열의 개수
n, m, k = map(int, input().split())
board = [input() for _ in range(n)]

# 모든 칸에 대해서 DFS 수행
for i in range(n):
    for j in range(m):
        dfs(i, j, board[i][j])

# 신이 좋아하는 K개의 각 단어를 만들 수 있는 경우의 수 출력
for _ in range(k):
    word = input().rstrip()
    print(cnt[word])