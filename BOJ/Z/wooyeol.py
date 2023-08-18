"""
    Z
    https://www.acmicpc.net/problem/1074
    
    풀이시간 07:00 ~ 07:25(25분)

    1 <= N <= 15
    0 <= r,c < 2**N

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? 재귀적 구현

    제 4사분면으로 분리하고 각 사분면의 시작점을 기준으로 이전 값들을 더해주는 연산을 진행한다면
    재귀로 편하게 나타낼 수 있다.

    그렇기에 BaseCondition은 N이 0일 때 0을 반환하게 한다.

    가장 작은 N은 0이고 이는 r,c에 관계없이 순서가 0번째임을 나타내는 것이다.

    그렇다면 N == 1이라면,
    size = 2 **(n-1)일때 size=1
    x * (1 * 1) + 0 이다. (x는 사분면 - 1) 
    이다.
    
"""
import sys

input = sys.stdin.readline


def recursive(n: int, r: int, c: int):
    # Base Condition
    if n == 0:
        return 0

    size = 2 ** (n - 1)

    # print(n, size, r, c)

    # 제 2사분면
    if r < size and c < size:
        return 0 * (size * size) + recursive(n - 1, r, c)

    # 제 1사분면
    if r < size and c >= size:
        return 1 * (size * size) + recursive(n - 1, r, c - size)

    # 제 3사분면
    if r >= size and c < size:
        return 2 * (size * size) + recursive(n - 1, r - size, c)

    # 제 4사분면
    if r >= size and c >= size:
        return 3 * (size * size) + recursive(n - 1, r - size, c - size)


N, r, c = map(int, input().split())

print(recursive(N, r, c))
