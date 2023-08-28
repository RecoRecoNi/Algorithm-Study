"""
    빙산
    https://www.acmicpc.net/problem/2573
    
    풀이시간
    10:33 ~ 14:12 (풀이 실패) + 4시간 (풀이 성공)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? BFS

    시간 초과와 메모리 초과로 실패했습니다. -> 리뷰를 보며 다시 풀이를 진행하여 풀이해낼 수 있었습니다.

    - 빙산 테이블을 만들면서 빙산의 위치를 덱에 기억시켜놓고 첫 요소를 기점으로 BFS로 진행합니다.
        - BFS 연산을 거치며 해당 빙산 주변 바다의 갯수를 통해 빙산의 높이를 조절합니다.
    - 하나의 빙산 덩어리는 첫 요소를 기점으로 BFS를 진행하였을 때 모든 요소를 탐색 할 수 있습니다. 
    - 혹시라도 빙산의 위치를 저장시킨 덱의 요소를 다 검사하였을 때 한 번 더 BFS 탐색을 한다면 두 개의 빙산 덩어리가 발생하였다는 것 이므로 현재 연도를 반환
    - 만약 BFS 연산이 일어나지 않았다면 0개의 덩어리라는 것이므로 0을 반환
"""

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

iceberg_queue: deque = deque()

iceberg: list = list()

# 빙산 데이터 입력 받기
for r in range(R):
    data = list(map(int, input().split()))
    checksum = sum(data)
    # 빙산의 높이 값이 존재한다면
    if checksum > 0:
        for c in range(C):
            # 작업 큐 업데이트 (year, row, col)
            if data[c] != 0:
                iceberg_queue.append((0, r, c))
    iceberg.append(data)


def bfs(x: int, y: int):
    q: deque = deque([(x, y)])
    visited[x][y] = True

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:
        x, y = q.popleft()

        # 4방향으로 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 방문 빙산인지 확인
            if (0 <= nx < R) and (0 <= ny < C) and not visited[nx][ny]:
                # 주변에 바다가 있는지 확인하고 해당 칸이 바다인지도 확인
                if iceberg[nx][ny] == 0 and iceberg[x][y] != 0:
                    iceberg[x][y] -= 1

                # 주변에 바다가 아닌 빙산이 있다면 다음 탐색을 위해 큐에 삽입
                if iceberg[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        # 4방향으로 바다를 검사했음에도 빙산이 녹지 않았다면 빙산 덱에 추가
        if iceberg[x][y] != 0:
            iceberg_queue.append((current_year + 1, x, y))

    return 1


current_year = 0
while True:
    cnt = 0
    visited = [[False] * C for _ in range(R)]

    # print(f"\niceberg queue : {iceberg_queue}")
    # print(f"current_year : {current_year}\n")
    # for row in iceberg:
    # print(*row)

    while iceberg_queue and iceberg_queue[0][0] == current_year:
        y, r, c = iceberg_queue.popleft()
        if iceberg[r][c] and not visited[r][c]:
            cnt += bfs(r, c)

    # 빙산 덩어리 갯수가 2개 이상이 된다면 종료
    if cnt > 1:
        print(current_year)
        break
    # 빙산 덩어리가 0개가 된다면 종료
    elif cnt == 0:
        print(0)
        break
    # 빙산 덩어리가 1개라면 다시 다음해로 이동
    current_year += 1
