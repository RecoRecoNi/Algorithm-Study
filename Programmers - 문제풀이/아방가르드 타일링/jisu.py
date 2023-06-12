"""
17:30 -> ... 해결 x
[풀이 참고](https://magentino.tistory.com/172)

특별 경우의 수 : i=4, 7, ..., i=5, 8, ...일 때 2, i=6, 9, ...일 때 4 가 반복됨을 활용해 점화식을 구하고,
각 SUM을 memoization하는 과정에서 업데이트 하는 방법으로 최적화
"""

def solution(n):
    init = [0, 1, 3, 10]

    if n < 4:
        return init[n]
    
    dp = init + [0] * (n-3)             # n에 해당하는 경우의 수를 담을 memoization table
    dp_sum = sum(init)                  # 1번째 Term : 전체 경우의 수 SUM
    partial_dp_sum = [10, 1, 3]         # 2번째 Term : i가 3, 6, 9, ... / 1, 4, 7, ... / 2, 5, 8, ... 각각의 SUM

    

    for i in range(4, n+1):
        _add = 2 if i%3 else 4      # 특별 경우의 수 : i=4, 7, ..., i=5, 8, ...일 때 2, i=6, 9, ...일 때 4
        dp[i] = (2 * dp_sum + 2*partial_dp_sum[i%3] - dp[i-1] + dp[i-3] + _add) # 점화식
        dp_sum = (dp_sum + dp[i])   # 전체 SUM update
        partial_dp_sum[i%3] = (partial_dp_sum[i%3] + dp[i]) # 부분 SUM update
 
    return dp[n] % 1000000007
    


case1 = 2
case2 = 3
case3 = 4
print(solution(case1)) # 3
print(solution(case2)) # 10
print(solution(case3)) # 23