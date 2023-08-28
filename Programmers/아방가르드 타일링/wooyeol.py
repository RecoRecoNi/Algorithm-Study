"""
    아방가르드 타일링
    https://school.programmers.co.kr/learn/courses/30/lessons/181186

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> DP
    
    - dp로 갯수의 패턴을 찾고 점화식을 세워 풀이
    
    - 풀이 참고 (https://schini.tistory.com/entry/아방가르드-타일링-181186번-프로그래머스-Programmers)
"""


def solution(n):
    dp = [1, 1, 3, 10, 23, 62]

    if n <= 5:
        return dp[n]

    four_iter = [2, 2, 0]
    five_iter = [2, 0, 0]
    six_iter = [0, 0, 0]

    for i in range(6, n + 1):
        current = dp[-1] + 2 * dp[-2] + 5 * dp[-3]

        idx = (i - 2) % 3
        five_iter[idx] += dp[1] * 2
        # print(f"dp[1] : {dp[1]}\n")
        # print(f"dp[1] * 2] : {dp[1] * 2}")
        # print(f"four_iter[{idx}] : {five_iter[idx]}")
        current += five_iter[idx]

        idx = (i - 1) % 3
        four_iter[idx] += dp[2] * 2
        # print(f"dp[2] : {dp[2]}\n")
        # print(f"dp[2] * 2 : { dp[2] * 2}")
        # print(f"four_iter[{idx}] : { four_iter[idx]}")
        current += four_iter[idx]

        idx = i % 3
        six_iter[idx] += dp[0] * 4
        # print(f"dp[0] : {dp[0]}\n")
        # print(f"dp[0] *4 : {dp[0] *4}")
        # print(f"six_iter[{idx}] : {six_iter[idx]}")
        current += six_iter[idx]

        dp = dp[1:] + [current]

    return dp[-1] % 1_000_000_007


print(solution(10))
