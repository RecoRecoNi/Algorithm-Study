"""
    연속합
    https://www.acmicpc.net/problem/1912
    
    풀이시간
    00:57 ~ 01:44 (47분)
    
    문제 조건
    1 <= N <= 100,000

    시간 복잡도 : O(N)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> DP
    DP 테이블 : 현재 인덱스까지 중에서 가장 높은 값 저장하는 테이블

    DP 테이블을 업데이트하며 최대 값 업데이트

"""
import sys

input = sys.stdin.readline

N = int(input())
n_array = list(map(int, input().split()))

# DP 테이블 = 현재 인덱스까지 중에 최대값
dp = [0] * N

# 초기 값 세팅
dp[0] = n_array[0]
max_value = dp[0]

# 1번째 인덱스 부터 N-1까지 데이터를 순회하며 DP 테이블 업데이트 후 최대 값 기억하기
for i in range(1, N):
    dp[i] = n_array[i]
    if dp[i] < dp[i - 1] + n_array[i]:
        dp[i] = dp[i - 1] + n_array[i]:
    if dp[i] > max_value:
        max_value = dp[i]

print(max_value)
