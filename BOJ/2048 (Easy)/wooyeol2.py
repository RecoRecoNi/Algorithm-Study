"""
    2048 (Easy)
    https://www.acmicpc.net/problem/12100

    풀이시간 
    23:23 ~ 24:14(49분)
    
    문제 조건
    1 <= N <=20

    시간 복잡도 : O(N^3 * 4 * 4 ^ 5)
    O(32,768,000)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 시뮬레이션(백 트래킹)
"""
import sys
import copy
from collections import deque

input = sys.stdin.readline

queue = deque()

def swipe(x, y):
    if board[x][y]:
        queue.append(board[x][y])
        board[x][y] = 0


def merge(x, y, direction):
    dx, dy = direction
    while queue:
        value = queue.popleft()
        # 빈칸이라면 현재 값 채우기
        if not board[x][y]:
            board[x][y] = value
        # 해당 칸의 값과 현재 값이 같다면 두배
        elif board[x][y] == value:
            board[x][y] *= 2
            x, y = x+dx, y+dy
        # 해당 칸의 값과 현재 값이 다르다면 다음 칸에 배치
        elif board[x][y] != value:
            x, y = x+dx, y+dy
            board[x][y] = value


def turn(direct):
    # 상하우좌
    directions_from = (0, N-1)
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    directions_increase = (range(1, N), range(N-2, -1, -1))

    if direct in (0, 1):
        for y in range(N):
            for x in directions_increase[direct % 2]:
                swipe(x, y)
            merge(directions_from[direct % 2], y, directions[direct])
    elif direct in (2, 3):
        for x in range(N):
            for y in directions_increase[direct % 2]:
                swipe(x, y)
            merge(x, directions_from[direct % 2], directions[direct])


def dfs(idx):
    global board, answer

    # 종료 조건
    if idx == 5:
        for i in range(N):
            temp_max = max(board[i])
            if temp_max > answer:
                answer = temp_max
        return 
    
    board_copy = copy.deepcopy(board)

    for direct in range(4):
        turn(direct)
        dfs(idx + 1)
        board = copy.deepcopy(board_copy)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dfs(0)
print(answer)