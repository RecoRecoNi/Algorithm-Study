"""
풀이 시작 : 2023-08-31 11:07

- 제한 사항
    - 2 <= N(보드 크기) <= 100, 0 <= K(사과 개수) <= 100
    - 1 <= L(방향 전환 횟수) <= 100
    - X(경과 초) <= 10000
    - 구현에 집중해도 좋을만한 범위라고 판단
- 풀이
    - 머리를 이동시키는 방식 
        - 상 하 좌 우 이동시킬 만큼의 좌표를 미리 지정해놓고 현재 방향에 따라 이동시키기
            - 'L', 'D'에 따라 전환되는 방향을 숫자로 표현해서 모듈러 연산을 활용해 방향을 전환한다.
        - 이동한 좌표가 보드 바깥이거나, 몸통인 경우 현재 카운트 출력하고 종료
        - 이동 후 카운트가 방향 전환을 실행할 카운트인 경우, 마지막에 방향 전환(문제 조건에 X초가 끝난 뒤 방향 전환이라고 명시)
    - 꼬리 이동 방식(중요)
        - 머리 이동 시 사과를 먹지 않는 경우에는 모두 꼬리를 줄여야 함
        - 그냥 현재 머리 이동 방향 따라서 줄이면 안되고, 현재 꼬리 위치에서 머리가 움직인 방향대로 꼬리가 움직여야 함
            - 이를 위해 머리 이동 시 보드에 방향 기록 필요
        - 보드에 기록된 방향을 따라 꼬리를 이동시키기

풀이 중단 : 2023-08-31 12:07    (1시간 경과)
풀이 재개 : 2023-08-31 13:30
풀이 완료 : 2023-08-31 14:00    (소요 시간 1시간 30분)
"""

import sys

input = sys.stdin.readline

N = int(input().rstrip())  # 보드 크기
board = [[-1 for _ in range(N)] for _ in range(N)]  # 보드
K = int(input().rstrip())  # 사과 개수

for _ in range(K):
    r, c = map(int, input().rstrip().split())
    board[r - 1][c - 1] = "A"  # 주어지는 사과 좌표는 1,1부터 시작함

L = int(input().rstrip())  # 방향 전환 횟수
operations = {
    int(time): operation
    for time, operation in [input().rstrip().split() for _ in range(L)]
}
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 위, 오른쪽, 아래, 왼쪽 방향 별 이동 좌표

h_y, h_x = 0, 0  # 머리 좌표
t_y, t_x = 0, 0  # 꼬리 좌표
d = 1  # 뱀은 처음에는 오른쪽을 향한다.
board[h_y][h_x] = 1  # 뱀은 게임이 시작할때 맨 위 맨 좌측에 존재하며 길이는 1이다.
clock = 0

while True:
    clock += 1
    ny, nx = h_y + directions[d][0], h_x + directions[d][1]  # 머리 이동
    if (
        ny < 0
        or ny >= N
        or nx < 0
        or nx >= N
        or (board[ny][nx] != "A" and board[ny][nx] >= 0)
    ):  # 이동한 머리 좌표가 보드를 벗어나거나 몸과 부딫히는 경우
        print(clock)
        break

    if board[ny][nx] == "A":  # 사과를 먹으면
        pass  # 몸 안줄여도 됨
    else:  # 몸 줄이기
        record = board[t_y][t_x]  # 보드에 기록된 머리가 움직인 방향을 따라 꼬리가 이동해야 함
        board[t_y][t_x] = -1  # 꼬리 줄이기
        t_y, t_x = (
            t_y + directions[record][0],
            t_x + directions[record][1],
        )  # 보드에 기록된 머리가 움직인 방향을 따라 꼬리가 이동

    if clock in operations:  # 이동 후 방향 전환이 필요한 경우
        d = (d - 1) % 4 if operations[clock] == "L" else (d + 1) % 4  # 방향 전환

    board[ny][nx] = d  # 보드에 이동 방향 기록 (추후 꼬리를 줄일 때 따라오기 위함)
    h_y, h_x = ny, nx  # 머리 좌표 최종 업데이트
