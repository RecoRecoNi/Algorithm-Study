"""
풀이 시작 : 2023-10-06 13:05

#### 제한사항
- mxn은 최대 30x30
- 구현에 집중

#### 풀이
- 시뮬레이션
- 한번 전체 탐색으로 없어질 블록 탐색
- 카운트 후 없애야 함(겹치는 부분도 없어져야 하므로)
- 없어진 좌표 기준으로 블록 '한 칸' 내리기
    - 겹치는 블럭을 고려하기 위해 없애아 하는 좌표는 set으로 관리한다.
    - 주의!
        - 없어진 블록을 채울 때 아래 블록 한 칸을 먼저 채우게 되면 바로 위 없어져야할 블록이 아래 블록으로 채워지게 되므로 오류
        - 정렬을 통해 없어질 블록 중 위 블록을 먼저 채워야 한다.
        - 정렬을 위해 불가피하게 리스트로 변환 후 정렬을 수행한다.


풀이 완료 : 2023-10-06 13:28(풀이시간 : 23분 소요)
"""

from typing import List


def solution(m: int, n: int, board: List[str]) -> int:
    # 없어질 블록을 'X'로 대체할 것이므로 List[str] -> List[List]
    board = list(map(list, board))

    answer = 0
    while True:
        rm_blocks = set()  # 중복해서 없어짐을 고려하기 위해 set으로 관리
        for row in range(m - 1):
            for col in range(n - 1):
                if (
                    board[row][col] != "X"  # 유효한 블록이면서
                    and board[row][col]  # 4개 블록이 같은 경우
                    == board[row][col + 1]
                    == board[row + 1][col]
                    == board[row + 1][col + 1]
                ):
                    rm_blocks.add((row, col))  # 없앨 블록에 추가
                    rm_blocks.add((row, col + 1))
                    rm_blocks.add((row + 1, col))
                    rm_blocks.add((row + 1, col + 1))

        if len(rm_blocks) == 0:  # 없앨 블록이 없으면 종료
            break
        else:  # 중복을 제외한 블록 개수를 없앰
            answer += len(rm_blocks)

        rm_blocks = sorted(list(rm_blocks))  # 없어질 2행 중 위부터 메꿔야 함(14 line 참고)

        for y, x in rm_blocks:
            tmp_y = y
            while tmp_y - 1 >= 0:
                board[tmp_y][x] = board[tmp_y - 1][x]  # 한칸씩 아래로 밀기
                tmp_y -= 1
            board[0][x] = "X"  # 맨 위는 유효하지 않은 블록 표시

    return answer


def main() -> None:
    case1 = [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]]
    case2 = [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]

    print(solution(*case1))
    print(solution(*case2))


main()
