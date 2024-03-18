"""
풀이 시작 : 2023-10-11 16:00

#### 제한 사항
- 보드 크기 1 1 <= N <= 20
- 보드 내부 수 < 1024

#### Solution
- 시뮬레이션
- 최대 5번 이동시키는 경우의 수는 5 ** 4 = 625
- 한 번의 재귀에서 N^2이어도 20 * 40 = 400
    - 625 * 400 = 250000의 연산량이므로 N^2이 훨씬 넘어도 괜찮다.

- 한 번 합쳐진 블록은 또 합쳐질 수 없음 => 별도의 표시 필요
- up, down, left, right를 구현해야 함
    - 각 이동 메서드는 어떻게 구현?
        - 1. 0이 아닌 비교하여 합칠 값 찾기
        - 2. 판단 후 합치기
            - 2-1. 값이 같고 아직 합쳐지지 않은 경우 합치기
            - 2-2. 바꿀 위치가 0인 경우
            - 2-3. 그 외 합칠 수 없는 경우 끌어 올리기만
    - trick
        - up-left 는 row와 col을 바꿔서 그대로 로직을 적용하면 됨
        - down-right 는 up-left에서 배열을 반전시켜 적용 후 다시 반전시켜주면 됨
- 각 상태공간에서 matrix는 독립적이므로 깊은 복사(deepcopy) 필요

풀이 중단 : 2023-10-11 17:10 (1시간 10분 경과)
풀이 재개 : 2023-10-12 13:10
풀이 완료 : 2023-10-12 14:10 (2시간 10분 소요)

"""

import sys
from typing import List
from copy import deepcopy

input = sys.stdin.readline

N = int(input().rstrip())

matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = 0


def up(matrix: List[List[int]]) -> None:
    """
    matrix의 값들을 위쪽으로 1회 합친 결과를 반환한다.
    """
    merged = [[False for _ in range(N)] for _ in range(N)]

    for col in range(N):
        for row in range(1, N):
            # 1. 비교할 위치 찾기
            tmp_row = row - 1
            while tmp_row - 1 >= 0 and matrix[tmp_row][col] == 0:
                tmp_row -= 1

            # 2-1. 값이 같고 합쳐질 수 있는 경우
            if (
                matrix[tmp_row][col] == matrix[row][col] != 0
                and not merged[tmp_row][col]
            ):
                matrix[tmp_row][col] *= 2
                matrix[row][col] = 0
                merged[tmp_row][col] = True
            # 2-2. 위의 0을 대체하는 경우
            elif matrix[tmp_row][col] == 0 and matrix[row][col] != 0:
                matrix[tmp_row][col], matrix[row][col] = (
                    matrix[row][col],
                    matrix[tmp_row][col],
                )
            # 2-3. 이외에 합칠 수 없는 경우 해당 위치 아래에 적재
            elif matrix[row][col] != 0:
                matrix[tmp_row + 1][col], matrix[row][col] = (
                    matrix[row][col],
                    matrix[tmp_row + 1][col],
                )

    return matrix


def left(matrix: List[List[int]]) -> None:
    """
    matrix의 값들을 왼쪽으로 1회 합친 결과를 반환한다.
    """
    merged = [[False for _ in range(N)] for _ in range(N)]

    for row in range(N):
        for col in range(1, N):
            # 1. 비교할 위치 찾기
            tmp_col = col - 1
            while tmp_col - 1 >= 0 and matrix[row][tmp_col] == 0:
                tmp_col -= 1

            # 2-1. 값이 같고 합쳐질 수 있는 경우
            if (
                matrix[row][tmp_col] == matrix[row][col] != 0
                and not merged[row][tmp_col]
            ):
                matrix[row][tmp_col] *= 2
                matrix[row][col] = 0
                merged[row][tmp_col] = True

            # 2-2. 위의 0을 대체하는 경우
            elif matrix[row][tmp_col] == 0 and matrix[row][col] != 0:
                matrix[row][tmp_col], matrix[row][col] = (
                    matrix[row][col],
                    matrix[row][tmp_col],
                )

            # 2-2. 합칠 수 없는 경우
            elif matrix[row][col] != 0:
                matrix[row][tmp_col + 1], matrix[row][col] = (
                    matrix[row][col],
                    matrix[row][tmp_col + 1],
                )

    return matrix


def down(matrix: List[List[int]]) -> None:
    """
    matrix의 값들을 아래쪽으로 1회 합친 결과를 반환한다.
    trick: matrix를 위로 반전시켜 up()을 적용 후 결과를 다시 반전시켜 반환한다.
    """
    matrix = up(matrix[::-1])
    return matrix[::-1]


def right(matrix: List[List[int]]) -> None:
    """
    matrix의 값들을 아래쪽으로 1회 합친 결과를 반환한다.
    trick: matrix를 좌우로 반전시켜 left()을 적용 후 결과를 다시 반전시켜 반환한다.
    """
    matrix = left(list(map(lambda x: x[::-1], matrix)))
    return list(map(lambda x: x[::-1], matrix))


def move(count: int, matrix: List[List[int]]) -> None:
    """
    matrix를 상, 하, 좌, 우로 5번 밀어 합치는 모든 경우의 수 중 가장 큰 블록의 크기를 반환한다.
    """
    global answer

    if count == 5:  # 최대 5회
        max_block = max(map(max, matrix))  # matrix 내 최대 블록 값
        if max_block > answer:
            answer = max_block
        return

    # 모든 상태 공간의 matrix들은 모두 독립적이어야 하므로 deepcopy로 matrix를 복제하여 호출한다.
    move(count + 1, up(deepcopy(matrix)))
    move(count + 1, left(deepcopy(matrix)))
    move(count + 1, down(deepcopy(matrix)))
    move(count + 1, right(deepcopy(matrix)))


move(0, deepcopy(matrix))
print(answer)
