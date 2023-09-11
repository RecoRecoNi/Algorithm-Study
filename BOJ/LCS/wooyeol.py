"""
    LCS
    https://www.acmicpc.net/problem/9251
    
    풀이 참조 : https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence

    풀이시간
    13:22 ~ 14:22(1시간 고민 후 풀이 참고)
    
    문제 조건
    문자열의 최대 길이는 1000

    시간 복잡도 :
    O(N * N) = O(N^2)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> DP

    점화식:
        1. 문자열A, 문자열B의 한글자씩 비교해봅니다.
        2. 두 문자가 다르다면 LCS[i - 1][j]와 LCS[i][j - 1] 중에 큰값을 표시합니다.
        3. 두 문자가 같다면 LCS[i - 1][j - 1] 값을 찾아 +1 합니다.
        4. 위 과정을 반복합니다.

"""
import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

s1_length = len(s1)
s2_length = len(s2)

dp = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]

for i in range(1, s1_length + 1):
    for j in range(1, s2_length + 1):
        # 점화식을 코드로 옮긴 내용
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
