"""
풀이 시작 : 2023-10-03 18:03

#### 제한 사항
- m과 n은 100이하이지만, 물에 잠긴 지역이 10개 이하이므로 완전탐색으로 모든 경우를 고려하기는 어렵다.

#### 풀이
- 학창시절 배운 최단경로 탐색 적용
- 오른쪽 혹은 아래로만 갈 수 있다.
    - 점화식은 `dp[r][c] = dp[r-1][c] + dp[c][r-1]`
    - r과 c가 0일 때를 생각해줘야 한다. 0인 좌표는 제외하고 한 방향에서만 온다.
- 물이 잠긴 지역은 set으로 관리해서 좌표 검사 후 0에서 업데이트를 하지 않으면 자연스레 피해서 가는 것!
- 후.... m이 가로고 n이 세로였다.. 출제자 줄빠따 마렵네
- 후.... puddles도 마찬가지다 주의하자

풀이 완료 : 2023-10-03 18:33 (풀이 시간 : 30분 소요)
"""
from typing import List


def solution(m: int, n: int, puddles: List[List[int]]) -> int:
    """
    n이 row, m이 col임
    """
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    # 2차원 리스트 to set
    puddles_set = {(row - 1, col - 1) for col, row in puddles}
    matrix[0][0] = 1

    for r in range(n):
        for c in range(m):
            # 물에 잠긴 지역은 갈 수 없다.
            if (r, c) in puddles_set or (r == 0 and c == 0):
                continue

            # 점화식 : 오른쪽 혹은 아래로만 이동할 수 있다.
            if r == 0:  # r과 c가 각각 0일 때 예외 처리 : 한 방향에서만 온다
                matrix[r][c] += matrix[r][c - 1]
            elif c == 0:
                matrix[r][c] += matrix[r - 1][c]
            else:
                matrix[r][c] += matrix[r][c - 1] + matrix[r - 1][c]

            matrix[r][c] %= 1000000007  # dp 최적화

    return matrix[-1][-1] % 1000000007


def main() -> None:
    case1 = [4, 3, [[2, 2]]]
    case2 = [4, 3, [[2, 2], [2, 3]]]
    case3 = [4, 3, [[2, 2], [3, 1]]]

    print(solution(*case1))  # 4
    print(solution(*case2))  # 3
    print(solution(*case3))  # 1


main()
