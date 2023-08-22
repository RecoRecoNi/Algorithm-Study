"""
    종이의 개수
    https://www.acmicpc.net/problem/1780
    
    풀이시간 
    08:30 ~ 09:30 + 13:30~14:44 (2시간 14분)
    N(1 <= N <= 3**7, N은 3**k 꼴)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? 재귀 / 분할 정복

    문제에는 두 가지 조건이 주어진다. 첫 번째는 9개의 값이 같은 값이라면 그 종이는 하나
    9개의 값이 다른 경우 그 종이는 각각 하나의 종이씩이다.

    그렇기에 범위 내의 데이터가 모두 같을 경우와 같지 않을 경우를 검사하고 같지 않다면 
    9개로 나눠서 다시 연산 진행 3**N 으로 주어지기에 3**(N-1)의 경우 다시 검사하여
    9개로 나눠진 값이 각각 하나씩만 반환할 때까지 분할해서 정복한다.

    풀이 참조 : https://velog.io/@yje876/python백준분할정복-1780-종이의-개수
"""
import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

values: dict = {-1: 0, 0: 0, 1: 0}


# 해당 범위 내의 데이터가 모두 같은 값인지 확인
def is_same_value(n: int, row: int, col: int):
    for i in range(row, row + n):
        for j in range(col, col + n):
            if paper[row][col] != paper[i][j]:
                return False
    return True


def recursive(n: int, row: int, col: int):
    # 조건 1: 하나의 값으로만 이루어져 있을 경우
    if not is_same_value(n, row, col):
        # 조건 2 : 9개의 값 확인하여 갯수 확인
        n_trisection = n // 3

        # 첫번째 행
        recursive(n_trisection, row, col)
        recursive(n_trisection, row, col + n_trisection)
        recursive(n_trisection, row, col + (2 * n_trisection))

        # 두번째 행
        recursive(n_trisection, row + n_trisection, col)
        recursive(n_trisection, row + n_trisection, col + n_trisection)
        recursive(n_trisection, row + n_trisection, col + (2 * n_trisection))

        # 세번째 행
        recursive(n_trisection, row + (2 * n_trisection), col)
        recursive(n_trisection, row + (2 * n_trisection), col + n_trisection)
        recursive(n_trisection, row + (2 * n_trisection), col + (2 * n_trisection))
        return
    else:
        # 결과에 따른 값 카운트
        values[paper[row][col]] += 1


recursive(N, 0, 0)

for value in values.values():
    print(value)
