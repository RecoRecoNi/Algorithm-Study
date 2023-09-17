"""
풀이 시작 : 2023-09-17 15:19

#### 제한 사항
- map의 크기는 최대 10000(nxm)
- O(N^2) <= solution <= O(NlogN) 알고리즘을 설계할 수 있다.
- 초기 위치도 카운트 하는 데에 주의
- 문제에서는 (1,1) -> (n,m)으로 표기되어있음 => 풀이에서는 (0, 0) -> (n-1, m-1)

#### 풀이 방법
- 주어진 matrix 내 최단 거리를 구해야 함
- 전형적인 그래프 탐색 문제에서 최단 거리를 구하는 데 적합한 BFS를 적용할 수 있다.

풀이 완료 : 2023-09-17 15:30 (풀이 시간 : 12분 소요)
"""
from typing import List
from collections import deque


def solution(maps: List[List[int]]) -> int:
    """
    (0, 0) -> (n-1, m-1) 까지 탐색 성공 시 최단 길이를 반환, 탐색 실패시 -1을 반환한다.
    """
    n = len(maps)
    m = len(maps[0])
    target_y, target_x = n - 1, m - 1  # 좌표는 임의로 0부터 시작

    queue = deque([(0, 0, 1)])  # 시작 좌표, cnt는 1부터 시작
    visited = [[False for _ in range(m)] for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x, cnt = queue.popleft()

        if y == target_y and x == target_x:  # 탐색 성공 시
            return cnt  # 최단 거리 반환

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if (
                0 <= ny < n  # 행 유효 범위
                and 0 <= nx < m  # 열 유효범위
                and maps[ny][nx] == 1  # 갈 수 있는 길
                and not visited[ny][nx]  # 아직 방문 안한 경우
            ):
                queue.append((ny, nx, cnt + 1))  # queue에 삽입
                visited[ny][nx] = True  # 방문 처리

    return -1


def main() -> None:
    case1 = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ]
    case2 = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ]

    print(solution(case1))  # 11
    print(solution(case2))  # -1


main()
