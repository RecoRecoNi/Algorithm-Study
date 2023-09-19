"""
풀이 시작 : 2023-09-19 10:21

#### 제한 사항
- 행의 개수 N : 100,000이하 자연수
- 열의 개수 : 4
- O(NlogN) 이하 알고리즘을 설계해야 한다.

#### 풀이
- 점수는 100 이하의 "자연수" 이므로 최대값을 더해주는 방식으로 설계하면 될 것 같다.
- i행 에서 i-1행 중 같은 열을 제외하고 최대값으로 누적합을 구하기
- 시간복잡도 : 최대 연산 N(100,000) * 4(i열) * 4(i-1열) = 1,600,000

풀이 완료 : 2023-09-19 10:31 (풀이 시간 : 10분 소요)
"""
from typing import List


def solution(land: List[List[int]]) -> int:
    """
    i번째 행의 각 열에 i-1번째 행의 해당 열을 제외한 나머지 열들의 최댓값을 누적합한다.
    """
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i - 1][k] for k in range(4) if k != j])

    return max(land[-1])


def main() -> None:
    case1 = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

    print(solution(case1))  # 16


main()
