"""
풀이 시작 : 2023-08-30 11:55

1 <= w, h <= 20 이므로 일단 구현에 집중해보자.

- 기본 탐색은 BFS로 진행한다.
- BFS로 탐색하다가 더러운 칸 방문시 카운트는 유지하되, 방문 정보는 초기화한다.
    - 자연스럽게 현재 기준 가까운 더러운 칸부터 탐색이 되는 개념
- 더러운 칸을 만났을 때 해당 칸이 마지막 더러운 칸이라면 카운트 반환
- 탐색이 모두 끝났을 때 더러운 칸이 남아있으면 탐색이 실패한 것

풀이 정지 : 2023-08-30 13:00  (1시간 5분 경과)
풀이 재개 : 2023-08-30 14:20
풀이 정지 : 2023-08-30 14:55 (1시간 40분 경과)
풀이 재개 : 2023-08-30 20:35 

- 위와 같이 BFS 탐색 시 마지막으로 탐색된 더러운 칸 기준 가장 가까운 칸부터 탐색이 됨
    - [*.o******]   이 경우 문제가 될 수 있음
    - 모든 경우 중 최단의 경로로 갈 수 있는 방법을 생각해야 된다.
- 더러운 칸의 수는 최대 10! 결국 더러운 칸을 탐색하는 순서가 문제가 되므로 더러운 칸을 방문하는 순서의 순열을 구해 완전탐색하자.
    - 한 더러운 칸에서 다른 더러운 칸으로 이동하는 최단 경로를 모두 알아야 함
    - 시간 복잡도.. 괜찮을까?
        - 더러운 칸 순열 * BFS 탐색 * 더러운 칸 수 = 10! * 20^2 * 10
"""
import sys
from typing import List, Tuple
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(
    matrix: List[List[str]], num_dirty_place: int, robot_idx: Tuple[int, int, int]
) -> int:
    """
    BFS 탐색을 진행한다. 더러운 칸 방문시 카운트는 유지하되, 방문 정보는 초기화한다.
    """
    r, c = len(matrix), len(matrix[0])
    queue = deque([robot_idx])
    visited = [[False for _ in range(c)] for _ in range(r)]

    tmp_visited = deepcopy(visited)
    tmp_visited[robot_idx[0]][robot_idx[1]] = True

    while queue:
        y, x, cnt = queue.popleft()

        if matrix[y][x] == "*":
            num_dirty_place -= 1

            if num_dirty_place == 0:
                return cnt
            else:
                matrix[y][x] = "."
                queue.clear()
                tmp_visited = deepcopy(visited)
                tmp_visited[y][x] = True

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]

            if (
                0 <= ny < r
                and 0 <= nx < c
                and not tmp_visited[ny][nx]
                and not matrix[ny][nx] == "x"
            ):
                queue.append((ny, nx, cnt + 1))
                tmp_visited[ny][nx] = True

    return -1


def simulation(w: int, h: int) -> int:
    """
    각 테스트케이스마다의 탐색을 진행한다.
    """
    matrix = []
    num_dirty_place = 0
    robot_idx = None

    for r in range(h):
        row = list(input().rstrip())
        num_dirty_place += row.count("*")

        if not robot_idx:
            for c in range(w):
                if row[c] == "o":
                    robot_idx = (r, c, 0)
                    break

        matrix.append(row)

    return bfs(matrix, num_dirty_place, robot_idx)


while True:
    w, h = map(int, input().rstrip().split())

    if not h:
        break

    print(simulation(w, h))
