"""
    N-Queen
    https://www.acmicpc.net/problem/9663

    풀이시간 
    BaaaaarkingDog의 백트래킹 강의를 보고 풀이를 시작
    00:05 ~ 01:20 (1시간 15분) - 풀이 참고
    
    문제 조건
    1 <= N <= 15

    시간 복잡도 : O(n!)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 백 트래킹

    - 퀸은 상하좌우와 대각선 방향 이동이 모두 가능합니다.

    - 검사는 각 row를 기준으로 갯수를 확인해야한다.
        - col이 같은 값은 체크
        - 대각선을 검사하기 위해서는 x+y / x-y 의 값이 같은 경우는 체크
            - 대각선은 왼쪽위에서 오른쪽 아래로 향하는 경우 (x,y)를 기준으로 x-y의 값이 같은 경우를 의미한다.
            - 오른쪽 위에서 왼쪽 아래로 향하는 경우 (x,y)를 기준으로 x+y의 값이 같은 경우를 의미한다.
"""

import sys

global count

input = sys.stdin.readline

N = int(input())

count: int = 0

isused_col = [False] * 15  # col이 같은 경우 y가 같음
isused_diag = [False] * 30  # diag(왼쪽 아래 to 오른쪽 위) x+y가 같은 값
isused_diag2 = [False] * 30  # diag(왼쪽 위 to 오른쪽 아래) x-y+n-1가 같은 값


def backtracking(row: int):
    global count

    if row == N:
        count += 1
        return

    # 해당 행의 모든 열 검사
    for col in range(N):
        # 해당 위치에서 하나라도 부적합한 케이스(상하, 대각선)가 있다면 패스
        if isused_col[col] or isused_diag[row + col] or isused_diag2[row - col + N - 1]:
            continue

        # 방문한 위치를 기준으로 접근이 부적합한 경우(상하, 대각선)에 방문 표시
        isused_col[col] = True
        isused_diag[row + col] = True
        isused_diag2[row - col + N - 1] = True

        # 다음 행 검사
        backtracking(row + 1)

        # 검사 결과 불가능한 경우일 때 다시 방문한 표시 해제
        isused_col[col] = False
        isused_diag[row + col] = False
        isused_diag2[row - col + N - 1] = False


# 한 행씩 검사하는 함수
backtracking(0)

print(count)
