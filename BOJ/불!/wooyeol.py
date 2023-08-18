"""
    불!
    https://www.acmicpc.net/problem/4179
    
    풀이시간
    20:10 ~ 03:00 오답 (약 7시간)

    1 <= R <= C <= 1000
    1000 by 1000 = 1,000,000

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? BFS or DFS
    
    - 불은 1분에 4칸씩 번짐
    - 사람은 1분에 한 칸씩 움직임

    맵에서 끝까지 어디로든 끝까지 간다면 탈출 성공 아니면 실패

    불을 기준으로 bfs 진행하고 사람을 기준으로 bfs를 진행하며 사람이 테이블 밖으로 무사히 나가진다면 결과가 바로 반환 (최소 값을 찾기 때문에)
    지훈이 밖으로 나갈 수 있다면 바로 출력하고 탐색 이후에도 나가지 못했다면 불가능으로 판단 후 반환

    이때에 지훈이 지나가려는 장소에 불이 온적이 있는지 확인하고 자기보다 빨리 혹은 같은 시간에 지나갔다면 지훈은 지나갈 수 없음

    - 다음의 알고리즘을 bfs를 두 번 사용하여 풀이 할 수 있었습니다.
"""
import sys
from collections import deque

input = sys.stdin.readline


def solution(
    row: int,
    col: int,
    fire: list,
    jihun: tuple,
    f_table: list,
    j_table: list,
    table: list,
):
    # 예외처리 - 지훈이 주어지지 않으면 불가능
    if not jihun:
        return "IMPOSSIBLE"

    # 지훈의 bfs 탐색을 위한 큐 생성
    queue = deque([jihun])

    # 상하좌우
    directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

    # 예외처리 - 엣지에 위치하면 바로 탈출이 가능하기 때문에 1반환
    if jihun[1] == row - 1 or jihun[2] == col - 1 or jihun[1] == 0 or jihun[2] == 0:
        return 1

    # print("############### FIRE ###############")
    # 1. 불의 이동
    while fire:
        time, f_r, f_c = fire.popleft()

        # 불을 기준으로 4방향으로 이동시키기
        for i, j in directions:
            t_r, t_c = f_r + i, f_c + j

            # 테이블을 벗어난다면 인덱스 오류가 발생할 수 있기 때문에 continue로 예외처리
            if t_r < 0 or t_c < 0 or t_r >= row or t_c >= col:
                continue

            # 테이블이 지나간 자리거나 벽 혹은 불의 시작점이면 방문하지 않음
            if (
                f_table[t_r][t_c] != 0
                or table[t_r][t_c] == "#"
                or table[t_r][t_c] == "F"
            ):
                continue

            # 새로 옮겨간 불의 걸린 시간 마킹
            f_table[t_r][t_c] = time + 1

            # 새로 옮겨간 불을 다른 큐에 추가
            fire.append((time + 1, t_r, t_c))

    # print("############### JIHUN ###############")
    # 2. 지훈 이동
    while queue:
        time, jihun_r, jihun_c = queue.popleft()

        # 지훈을 기준으로 4방향으로 이동하며 탐색하기 - BFS
        for i, j in directions:
            j_r, j_c = jihun_r + i, jihun_c + j

            # table 밖으로 움직였다면 반환
            if j_r < 0 or j_c < 0 or j_r >= row or j_c >= col:
                return time + 1

            # 이미 방문한 곳이거나 벽 혹은 불이 이미 지나간 자리는 지나갈 수 없기 때문에 스킵
            if (
                (j_table[j_r][j_c] != 0)  # 이미 지나간 자리
                or (table[j_r][j_c] == "#")  # 벽
                or (table[j_r][j_c] == "F")  # 불의 시작지
                or (
                    f_table[j_r][j_c] != 0 and f_table[j_r][j_c] <= time + 1
                )  # 불이 방문한적이 있고 불이 지나간 시간이 지훈이 지나가려고 하는 시간보다 작거나 같으면 이동 할 수 없다.
            ):
                continue

            # 예외 상황들과 관계가 없다면
            # 테이블에 현재 이동거리만큼 마킹
            j_table[j_r][j_c] = time + 1

            # 끝에 도착하지 않았다면 다음 탐색을 위해 큐에 삽입
            queue.append((time + 1, j_r, j_c))

    return "IMPOSSIBLE"


def main():
    # Row, Col 갯수
    row, col = map(int, input().split())

    # 불의 위치를 기록하고 두 개의 덱을 통해 옮겨가며 진행하기 위해서 다음과 같은 2차원 배열 생성
    fire: deque = deque()

    # jihun의 위치 (time, row, col)
    jihun: tuple = None

    # 불의 위치를 나타내기 위한 미로
    f_table: list = [[0] * col for _ in range(row)]

    # 지훈의 위치를 나타내기 위한 미로
    j_table: list = [[0] * col for _ in range(row)]

    # table
    table: list = list()

    # 미로를 입력받으며 Jihun의 위치와 불의 위치를 기록
    for r in range(row):
        line = list(input().rstrip())

        # Fire 과 Jihun의 현재 위치를 기록
        if ("J" in line) or ("F" in line):
            for c, character in enumerate(line):
                if character == "F":
                    fire.append((0, r, c))
                elif character == "J":
                    jihun = (0, r, c)
        table.append(line)

    print(solution(row, col, fire, jihun, f_table, j_table, table))


main()

# 4 4
# ####
# #JF#
# #..#
# #..#

# 4 4
# ####
# .J..
# ....
# .#.F
