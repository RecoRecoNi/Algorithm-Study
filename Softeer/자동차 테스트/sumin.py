"""
풀이시간: 15분

<input>
n: 자동차의 개수(1 ≤ n ≤ 50,000)
q: 질의의 개수(1 ≤ q ≤ 200,000)

<solution>
3대의 자동차에 대해서만 테스트가 가능하기 때문에
[중앙값보다 작은 수들, 중앙값, 중앙값보다 큰 수들]라고 생각했을 때
중앙값보다 작은 수들 * 중앙값보다 큰 수들은 모든 경우의 수가 된다.

<시간복잡도>
O(NlogN + QlogN)
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline

# 자동차의 개수, 질의의 개수
n, q = map(int, input().split())
# 자동차 연비
efficiency = sorted(map(int, input().split()))

for _ in range(q):
    # 중앙값
    m = int(input())
    idx = bisect_left(efficiency, m)
    # 중앙값이 자동차 연비에 존재하면 해당 수보다 작은 수들의 개수 * 큰 수의 개수
    if idx < n and efficiency[idx] == m:
        print(idx * (n - idx - 1))
    else:
        print(0)