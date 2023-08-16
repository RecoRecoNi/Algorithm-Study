"""
    빙산
    https://www.acmicpc.net/problem/2573
    
    풀이시간
    10:33 ~ 14:12 (풀이 실패)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? bfs

    시간 초과와 메모리 초과로 실패했습니다.

"""
import sys
import copy
from collections import deque

input = sys.stdin.readline


def check_cycle(R: int, C: int, start_point: tuple, iceberg_count: int, iceberg: list):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    count: int = 1
    visited = set()
    s_queue = deque([start_point])

    while s_queue:
        tx, ty = s_queue.popleft()
        visited.add((tx, ty))
        for dtx, dty in directions:
            ntx, nty = tx + dtx, ty + dty

            # 범위 검증
            if 0 <= ntx < R and 0 <= nty < C:
                if (not (ntx, nty) in visited) and iceberg[ntx][nty]:
                    s_queue.append((ntx, nty))
                    count += 1

    # 하나의 점으로부터 bfs 탐색을 했을 때 모든 점이 카운트 되지 않았다면 2개 이상의 cycle이 생긴 것으로 확인
    if iceberg_count != count:
        return True
    return False


def solution(R: int, C: int, iceberg: list, queue: deque):
    iceberg_count = len(queue)

    pre_year: int = 0

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    record_iceberg: list = copy.deepcopy(iceberg)

    while queue:
        year, x, y = queue.popleft()

        if year > pre_year:
            iceberg = copy.deepcopy(record_iceberg)
            start_point = (x, y)

            # 2개 이상의 덩어리가 생겼는지 확인
            if check_cycle(R, C, start_point, iceberg_count, iceberg):
                return year + 1

        # 4방향으로 탐색하며 빙산 값 업데이트
        temp_count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 범위 검증
            if 0 <= nx < R and 0 <= ny < C:
                # 0이라면
                if iceberg[nx][ny] == 0:
                    # 낮아지는 빙하 갯수 카운트
                    temp_count += 1

        # 업데이트 된 빙산 높이 업데이트
        record_iceberg[x][y] = max(0, iceberg[x][y] - temp_count)

        # 작업 큐 업데이트
        if record_iceberg[x][y]:
            queue.append(((year + 1), x, y))
        else:
            iceberg_count -= 1

        pre_year = year

        # print()
        # print(queue)
        # for tr in iceberg:
        #     print(*tr)
        # print()
        # for tf in record_iceberg:
        #     print(*tf)
        # print()

    return 0


def main():
    R, C = map(int, input().split())

    queue: deque = deque()

    iceberg: list = list()

    # 빙산 데이터 입력 받기
    for r in range(R):
        data = list(map(int, input().split()))
        checksum = sum(data)
        # 빙산의 높이 값이 존재한다면
        if checksum:
            for c in range(len(data)):
                # 작업 큐 업데이트 (year, row, col)
                queue.append((0, r, c))
        iceberg.append(data)

    return solution(R, C, iceberg, queue)


print(main())
