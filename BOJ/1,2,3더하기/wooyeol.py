"""
    1,2,3 더하기
    https://www.acmicpc.net/problem/9095

    어떤 알고리즘으로 풀이할 수 있을까? DP

    1을 1,2,3의 합으로 나타내는 방법의 수 -> D[1]
        (1) : 1
    2을 1,2,3의 합으로 나타내는 방법의 수 -> D[2]
        (1,1),(2) : 2
    3을 1,2,3의 합으로 나타내는 방법의 수 -> D[3]
        (1,1,1),(1,2),(2,1),(3) : 4
"""
import sys

input = sys.stdin.readline


def algorithm(dp: list):
    for i in range(4, 11):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        # 4 : 1,2,3
        # 5 : 2,3,4
        # 6 : 3,4,5
    return dp


def main():
    T = int(input())
    dp = [0, 1, 2, 4] + [0 for _ in range(7)]
    dp = algorithm(dp)
    for _ in range(T):
        # n은 양수이며 11보다 작다.
        print(dp[int(input())])


main()
