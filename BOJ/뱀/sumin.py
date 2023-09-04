"""
풀이시간: 40분

<input>
- N: 보드의 크기 (2 ≤ N ≤ 100)
- K: 사과의 개수 (0 ≤ K ≤ 100)
- L: 뱀의 방향 변환 횟수 (1 ≤ L ≤ 100)
    - X, C: X초가 끝난 뒤에 C방향으로 90도 회전

<solution>
- 0: 빈공간, 1: 벽, 2: 사과, 3: 뱀으로 보드를 표현
- 그 외 나머지 규칙 구현

<시간복잡도>
O(N^2 + K + L)
"""
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())  # 보드 크기
K = int(input())  # 사과 개수

# N x N의 보드를 만든다.
board = [[1] * (N + 2)] + [[1] + [0] * N + [1] for _ in range(N)] + [[1] * (N + 2)]

for i in range(K): # 사과 정보
    row, col = map(int, input().split()) # 사과의 위치
    board[row][col] = 2  # 사과는 숫자 2로 표현

# 뱀의 방향 변환 정보
L = int(input())  # 뱀의 방향 변환 횟수
change = [list(input().split()) for _ in range(L)]  # [X, C] 형태의 리스트로 저장

# 초기 상태 설정
time = 0 # 게임 시간 초기화
x, y = 1, 1  # 뱀의 첫 위치(1행 1열)
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)} # 북동남서
cur = 1 # 초기 방향은 오른쪽 (동쪽)
snake = deque([[1, 1]]) # 뱀의 위치

# board -> 0: 빈 공간, 1: 벽, 2: 사과, 3: 뱀
# 이동한 후에 뱀 머리의 위치가 벽이거나, 자신의 몸일 경우 stop
while True:
    # 뱀의 머리 위치 업데이트
    x = x + directions[cur][0]
    y = y + directions[cur][1]
    time += 1

    # 1) 이동한 곳에 사과가 있는 경우 -> 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[x][y] == 2:
        board[x][y] = 3  # 사과 대신 뱀 머리
        snake.append([x, y]) # 뱀 길이 증가

    # 2) 이동한 곳이 빈 공간인 경우 -> 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다.(몸길이는 변하지 않는다.)
    elif board[x][y] == 0:
        board[x][y] = 3  # 뱀 머리 위치 변경
        snake.append([x, y]) # 뱀 길이 증가
        tail_x, tail_y = snake.popleft() # 뱀 꼬리 위치 업데이트
        board[tail_x][tail_y] = 0 # 뱀 꼬리 자리를 빈 공간으로 변경

    # 3) 벽 또는 자신의 몸과 부딪힌 경우(게임 종료)
    else:
        break

    # 다음 방향 확인 -> 방향 전환
    if change and time == int(change[0][0]):
        _, next_direction = change.pop(0)
        if next_direction == 'L':
            cur = (cur - 1) % 4  # 왼쪽으로 회전
        else:
            cur = (cur + 1) % 4  # 오른쪽으로 회전

print(time)