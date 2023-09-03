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
    - 위 경우 최단 경로는 왼쪽으로 갔다가 오른쪽으로 쭉 가는 것인데, BFS는 가까운 곳부터 탐색하게 된다.
    - 모든 경우 중 최단의 경로로 갈 수 있는 방법을 생각해야 된다.
- 더러운 칸의 수는 최대 10, 결국 더러운 칸을 탐색하는 순서가 문제가 되므로 더러운 칸을 방문하는 순서의 순열을 구해 완전탐색하면 된다.
    - 이 경우 한 더러운 칸에서 다른 더러운 칸으로 이동하는 최단 경로를 모두 알아야 함 -> 인접 행렬형태의 distance matrix를 만들어 활용한다.
    - distancd matrix를 한 번 구해놓으면 순서에 따라 거리만 참조하면 된다.
    - 시간 복잡도.. 괜찮을까?
        - 최단 경로 matrix 만들기 -> 최대 distance matrix(10 * 10 / 2) * BFS(20 * 20) = 20000
        - 최단 경로 구하기 -> 최대 10! * 거리는 이미 구해져있으므로 1 = 3628800
        - 위 두 경우는 독립적으로 시행되므로 20000 + 3628800 가능! 구현해보자.

풀이 완료 : 2023-08-30 22:10 (소요시간 4시간 20분)
"""
import sys
from typing import List, Tuple
from collections import deque
from itertools import product, permutations

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(
    matrix: List[List[str]],
    st: Tuple[int, int],
    dt: Tuple[int, int],
) -> int:
    """
    주어진 matrix에서 두 점 사이의 최단 거리를 구해 반환한다.
    """
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque([(*st, 0)])
    visited[st[0]][st[1]] = True

    while queue:
        y, x, cnt = queue.popleft()

        if (y, x) == dt:
            return cnt

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if (
                0 <= ny < h
                and 0 <= nx < w
                and not visited[ny][nx]
                and matrix[ny][nx] != "x"
            ):
                queue.append((ny, nx, cnt + 1))
                visited[ny][nx] = True

    return -1


def get_distance_matrix(
    matrix: List[List[str]], points: List[Tuple[int, int]]
) -> List[List[int]]:
    """
    로봇청소기와 더러운 칸, 더러운 칸과 더러운 칸의 모든 거리를 저장한 distance matrix를 만들어 반환한다.

    points = 로봇청소기 위치 + 더러운칸 위치(robot_and_dirty_place)
    """
    distance_matrix = [[0 for _ in range(len(points))] for _ in range(len(points))]

    for st, dt in product(
        range(len(points)), range(len(points))
    ):  # 모든 (시작점 idx, 도착점 idx) 집합을 순회한다.
        if distance_matrix[st][dt]:  # distance matrix는 대칭이므로 이전 연산에 의해 이미 저장되어있는 경우
            continue

        distance = bfs(
            matrix, points[st], points[dt]
        )  # matrix에서 두 점사이의 최단 거리는 bfs로 구한다.

        if distance == -1:  # 탐색에 실패하는 경우(더러운 칸에 갈 수 없는 경우)
            return -1  # 실패 반환
        else:
            distance_matrix[st][dt] = distance_matrix[dt][
                st
            ] = distance  # distance_matrix는 대칭

    return distance_matrix


def get_min_path(distance_matrix: List[List[int]]) -> int:
    """
    주어진 distance_matrix에서 최단 이동 경로를 구해 반환한다.
    """
    min_path = 1000000

    for case in permutations(
        range(1, len(distance_matrix))
    ):  # 더러운 곳 탐색 순서의 모든 경우의 수 탐색(최대 10!), 0번째는 로봇 위치임
        tmp = distance_matrix[0][case[0]]  # 로봇 -> 첫 번째 더러운 곳
        for i in range(len(case) - 1):  # 더러운 곳 -> 더러운 곳
            tmp += distance_matrix[case[i]][case[i + 1]]
        min_path = min(min_path, tmp)  # 최단 이동 경로 업데이트

    return min_path


def start_simulation(
    matrix: List[List[str]],
    dirty_places: List[Tuple[int, int]],
    robot_idx: Tuple[int, int],
) -> int:
    """
    주어진 조건에서 최단 이동경로를 찾기 위한 시뮬레이션을 시작한다.
    1. 모든 더러운 칸끼리의 거리를 저장한 distance matrix생성한다. (로봇 포함)
        1-1. distance_matrix 만들기에 실패하면 -1을 반환한다.
    2. 주어진 distance_matrix에서 최단 이동 경로를 구해 반환한다.

    """
    robot_and_dirty_place = [robot_idx] + dirty_places  # 로봇과 더러운 칸과의 거리도 알아야 하므로 위치 합치기
    distance_matrix = get_distance_matrix(matrix, robot_and_dirty_place)
    if distance_matrix == -1:
        return -1

    return get_min_path(distance_matrix)


def simulation() -> int:
    """
    주어진 각 테스트케이스마다 시뮬레이션을 위한 셋업(matrix만들기, 로봇 위치, 더러운 칸 위치) 후 시뮬레이션을 호출한다.
    """
    matrix = []
    dirty_places = []
    robot_idx = None

    for r in range(h):
        row = list(input().rstrip())

        for c in range(w):
            if not robot_idx and row[c] == "o":  # 로봇은 한 대만 주어짐
                robot_idx = (r, c)
            if row[c] == "*":
                dirty_places.append((r, c))

        matrix.append(row)

    return start_simulation(matrix, dirty_places, robot_idx)  # 최단 이동 경로를 얻기 위한 시뮬레이션 시작


while True:
    w, h = map(int, input().rstrip().split())

    if not h:
        break

    print(simulation())
