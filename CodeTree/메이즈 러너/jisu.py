"""
풀이 시작 : 2023-10-13 12:40 (이후 시간을 측정하지 않고 과제 느낌으로 풀이)
#### 제한사항
- 미로의 크기 : 4 <= N <= 10
- 참가자 수 : 1 <= M <= 10
- 게임 시간 : 1 <= K <= 100

#### 풀이
1. 이동
2. 회전
    2-1. 정사각형 찾기
    2-2. 회전시키기

풀이 완료 : 2023-10-14 18:03 (이틀동안 이거만 함 ㅎㅎ..)
수행시간 | 메모리
--|--
327ms | 27MB
"""

import sys
from typing import Tuple
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
participants = deque(
    [tuple(map(lambda x: int(x) - 1, input().rstrip().split())) for _ in range(M)]
)
E = tuple(map(lambda x: int(x) - 1, input().rstrip().split()))

dy = [-1, 1, 0, 0]  # 상 하 좌 우 순서
dx = [0, 0, -1, 1]

answer = 0


def move(py: int, px: int) -> int:
    """
    특정 참가자를 출구와 가까운 쪽으로 1만큼 이동시킨다.
    이동 시 출구와 가까워지는 쪽으로, 상-하-좌-우 우선순위로 이동한다.

    input : 이동시킬 참가자 (y, x) 좌표
    output : 참가자 이동 여부 (이동했으면 1, 이동하지 않았으면 0)
    """
    # 기존 참가자와 출구까지의 최단 거리
    dist = abs(py - E[0]) + abs(px - E[1])

    for d in range(4):
        ny = py + dy[d]
        nx = px + dx[d]
        # 이동 후 참가자와 출구까지의 최단 거리
        new_dist = abs(ny - E[0]) + abs(nx - E[1])
        # 이동 가능하며, 출구와 가까워지는 경우
        if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 0 and new_dist < dist:
            # 이동 후 좌표가 탈출구인 경우 탈출시키고 아닌 경우, 이동시킨 좌표를 큐에 삽입
            if (ny, nx) != E:
                participants.append((ny, nx))
            # 이동 성공 시 count 1 반환
            return 1
    # 이동 실패 시 원래 좌표를 다시 큐에 삽입, count 0 반환
    participants.append((py, px))

    return 0


def get_rectangle() -> Tuple[int, int, int, int]:
    """
    출구와 최소 한 명의 참가자를 포함하는 최소 넓이 직사각형의 네 좌표를 반환한다.

    input : x
    output : 직사각형의 min_y, min_x, max_y, max_x
    """
    rectangles = []

    for y, x in set(participants):
        max_y = max(y, E[0])
        min_y = min(y, E[0])
        max_x = max(x, E[1])
        min_x = min(x, E[1])

        # 한 변의 길이
        side_len = max(max_y - min_y, max_x - min_x)
        # 한 변의 길이를 유지하는 최소의 좌상단 좌표를 가지는 직사각형 좌표 구하기
        min_y = max(max_y - side_len, 0)
        max_y = min_y + side_len
        min_x = max(max_x - side_len, 0)
        max_x = min_x + side_len

        rectangles.append((side_len**2, min_y, min_x, max_y, max_x))
    # 우선순위 : 넓이 > 좌상단 y좌표 > 좌상단 x좌표
    return min(rectangles)[1:]


def rotate(min_y: int, min_x: int, max_y: int, max_x: int) -> None:
    """
    rotate시킬 정사각형의 좌표를 받아 시계방향으로 90도 회전시킨다.

    input : rotate 시킬 정사각형의 min_y, min_x, max_y, max_x 좌표
    output : x
    """
    global E

    participants_set = set(participants)
    # rotate 시킬 부분의 임시 matrix
    rotate_matrix = [
        [0 for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)
    ]

    # rotate전 정보 백업
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            # 벽의 경우 내구도 -1 시켜 백업
            if matrix[y][x] > 0:
                rotate_matrix[y - min_y][x - min_x] = matrix[y][x] - 1
            # 출구 좌표 정보 백업
            elif (y, x) == E:
                rotate_matrix[y - min_y][x - min_x] = "E"
            # 참가자 좌표 정보 백업
            elif (y, x) in participants_set:
                # 참가자는 동일 좌표에 여러명이 위치할 수 있음
                cnt = 0
                while (y, x) in participants:
                    cnt += 1
                    participants.remove((y, x))
                # 참가자 한 명당 *의 개수로 백업
                rotate_matrix[y - min_y][x - min_x] = "*" * cnt

    # 해당 백업 matrix 90도 회전
    rotate_matrix = [list(row)[::-1] for row in zip(*rotate_matrix)]

    # 원본 matrix의 정사각형 위치를 90도 회전시킨 백업 matrix로 대치
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            # 회전 후 참가자 위치를 다시 큐에 삽입
            if str(rotate_matrix[y - min_y][x - min_x]).startswith("*"):
                # 기존 존재하던 참가자 수만큼 삽입
                for _ in range(len(rotate_matrix[y - min_y][x - min_x])):
                    participants.append((y, x))
                    matrix[y][x] = 0
            # 회전 후 출구 위치
            elif rotate_matrix[y - min_y][x - min_x] == "E":
                E = (y, x)
                matrix[y][x] = 0
            # 회전 후 벽의 내구도
            else:
                matrix[y][x] = rotate_matrix[y - min_y][x - min_x]


# 최대 k초 이동 가능
for i in range(K):
    # 참가자 당 한 번씩 move
    M = len(participants)
    for _ in range(M):
        answer += move(*participants.popleft())
    # 이동 과정에서 참가자가 모두 탈출한 경우 종료
    if not participants:
        break
    # 정사각형 좌표를 구해 해당 위치 90도 rotate
    rotate(*get_rectangle())

print(answer)
print(E[0] + 1, E[1] + 1)
