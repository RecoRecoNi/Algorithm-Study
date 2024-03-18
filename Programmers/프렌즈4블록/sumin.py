"""
풀이시간: 35분

<input>
m: 판의 높이(2 ≦ n, m ≦ 30)
n: 판의 폭(2 ≦ n, m ≦ 30)
board: 판의 배치 정보(대문자 A-Z)

<solution>
문제에서 주어진대로 구현한다.
더 이상 제거되는 블록이 없을 때까지 다음의 과정을 반복

1. 제거되는 블록 확인하기(2x2)
- 제거되는 블록의 좌상단 좌표만 따로 보관하기

2. 제거되는 블록은 .으로 값 변경하기
- 제거되는 블록의 좌상단 좌표를 이용해 2x2 칸은 모두 .으로 변경

3. 제거되는 블록의 위 블록들 내려주기
- 재귀를 통해 더 이상 블록을 내릴 수 없을 때까지 제거된 블록 위의 블록들 내려주기

<시간복잡도>
O(NM) + O(NM) + O(NM) = O(3NM) = O(NM)을 더 이상 블록이 제거될 수 없을 때까지 반복
- 제거되는 블록이 있는지 확인
- 제거되는 블록 .으로 변경
- 블록을 내리는 작업
 
"""
from typing import List


# (x, y) 좌표에서 더 이상 내릴 수 없을 때까지 블록을 내리는 함수
def go(x, y, board) -> None:
    """
    x: 확인하고 있는 칸의 x좌표
    y: 확인하고 있는 칸의 y좌표
    board: 판의 배치 정보
    """
    # base condition(불가능한 경우: 최하단인 경우)
    if x == len(board) - 1:
        return
    # 아래로 내릴 수 있는 경우만 계속해서 재귀호출(블록 내리기)
    if board[x+1][y] == '.':
        board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
        go(x+1, y, board)


def solution(m: int, n: int, board: List[str]) -> int:
    """
    m: 판의 높이(세로)
    n: 판의 폭(가로)
    board: 판의 배치 정보
    """
    flag = True # 계속해서 진행할지 판단하기 위한 변수
    board = [list(row) for row in board]
    while flag:
        flag = False
        remove = [] # 제거되는 블록의 좌상단 좌표
        # 1) 제거되는 블록이 있는지 확인
        for i in range(m-1): # 높이
            for j in range(n-1): # 폭
                # 2) 판의 각 칸에서 2x2가 같은 알파벳이라면 지워지는 블록을 추가
                if board[i][j] == board[i][j+1] == board[i+1][j+1] == board[i+1][j] != '.':
                    remove.append((i, j))

        # 제거되는 블록이 있다면
        if remove:
            flag = True # 제거된 블록이 있기 때문에 게임을 계속 진행
            # 2) 제거되는 블록은 .으로 표시
            for x, y in remove:
                board[x][y] = board[x][y+1] = board[x+1][y] = board[x+1][y+1] = '.'
            # 3) 제거된 블록이 있는 경우 더 이상 내릴 수 없을 때까지 블록 내리기(아래쪽부터 확인하며 내리기)
            for i in range(m-2, -1, -1):
                for j in range(n):
                    # 현재 칸이 비어있지 않고, 바로 아래 칸이 비어있는 경우(제거된 블록이 있는 경우) 블록을 내릴 수 있음
                    if board[i][j] != '.' and board[i+1][j] == '.':
                        go(i, j, board)

    # 4) 제거된 블록의 개수 세기
    answer = sum(row.count('.') for row in board)

    return answer


def main() -> None:
    case1 = [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]]
    case2 = [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]

    print(solution(*case1)) # 14
    print(solution(*case2)) # 15


main()
