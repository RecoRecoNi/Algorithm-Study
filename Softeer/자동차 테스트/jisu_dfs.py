"""
# 시간 초과 풀이
풀이 시작 : 2023-10-08 11:17

#### 제한 사항
- q <= 200,000 이므로, O(NlogN) 이하의 알고리즘을 설계해야 한다.

#### 풀이
- m을 확정한 상태에서 m보다 작은 하나, m보다 큰 하나를 고르는 경우의 수
- 백트래킹으로 m보다 작은 수 하나, 큰 수 하나를 고르는 경우의 수를 구한다.(시간초과)
"""
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, q = map(int, input().rstrip().split())
costs = sorted(list(map(int, input().rstrip().split())))
cnt = 0


def dfs(idx: int, m: int, before: bool, after: bool):
    global cnt

    if before and after:
        cnt += 1
        return

    if idx == n:
        return

    if not before and costs[idx] < m:  # 작은 값으로 하나 선택하는 경우
        dfs(idx + 1, m, True, after)
    elif not after and costs[idx] > m:  # 큰 값으로 하나 선택하는 경우
        dfs(idx + 1, m, before, True)

    dfs(idx + 1, m, before, after)  # 선택하지 않는 경우


for _ in range(q):
    m = int(input().rstrip())
    cnt = 0

    if m in costs and m >= costs[1] and m <= costs[-2]:
        dfs(0, m, False, False)
    print(cnt)
