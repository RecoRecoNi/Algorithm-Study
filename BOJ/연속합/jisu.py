"""
풀이 시작 : 2023-09-10 16:19

- 제한 사항
    - 수는 100,000개까지 주어지므로 O(NlogN) 알고리즘을 설계해야 한다.
- 풀이 방법
    - 별도의 dp배열을 활용해 해당 배열의 i번째 원소는 수열에서 i번째부터 연속 합을 구했을 때의 가장 큰 합을 저장한다.
    - 이를 위해 dp 배열을 순회하며 i-1번째 까지의 최대 연속합에 i번째 원소를 더할 것인지, i번쨰 원소부터 다시 시작할 지 결정해야 한다.
        - 둘 중 최대값을 선택해 업데이트 한다. (`dp[i] = max(dp[i-1]+nums[i], nums[i])`)
- 주의 사항
    - dp[i]반쩨 깂은 연속 합을 위해서 dp[i-1]에 좋든 싫든 수열의 i번째 원소를 고려한 값으로, dp배열의 마지막 값이 문제의 해는 아니다.
        - 즉, dp배열의 최대값이 문제의 해이다.

풀이 완료 : 2023-09-10 16:50 (풀이 시간 : 31분)
"""

import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))
dp = [0 for _ in range(n)]  # dp의 i번째 원소는 수열의 i번째 원소부터 고려했을 때 최대 연속 합
answer = dp[0] = numbers[0]

for i in range(1, n):
    dp[i] = max(
        dp[i - 1] + numbers[i], numbers[i]
    )  # i-1번째 까지 연속합에 i번째 원소를 더할 것인지, i번쨰 원소부터 다시 시작할 지 결정
    answer = max(dp[i], answer)  # 문제의 해는 dp 배열의 최대값

print(answer)
