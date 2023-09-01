"""
    로봇 청소기
    https://www.acmicpc.net/problem/4991

    풀이시간 
    22:41 ~ (풀이 포기 후 풀이 참조)

    풀이 참조 : https://chldkato.tistory.com/66
    
    문제 조건
    1 ≤ w, h ≤ 20
    더러운 칸 k 는 10개 이하
    로봇 청소기는 하나

    시간 복잡도 : 
    O(WH + 5WH + K-1 * 5WH + K! * k) : O((5K+1) * WH + K! * k)
    O(51 * 400 + 10! * 10)
    O(20,400 + 36,288,000)
    O(36,308,400) 이기 때문에 1초 안에 Pass가 되지 않는다.

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 시뮬레이션

    [그리디] 로봇 청소기 위치에서 가장 가까운 더러운 칸을 연산으로 구하여 이동 후 해당 위치에서 가장 가까운 다음 더러운 칸으로 이동
        - 벽으로 인해 최단 거리 계산에 어려움이 생김 -> 잘못된 접근
    
    해결법
    [BFS] 로봇을 기준으로 모든 맵에 대한 bfs 탐색을 통해 각 더러운 칸 별로 최단 거리 구하기 + 더러운 칸에서 다른 더러운 칸으로의 최단거리 확인
        - 로봇의 방문 순서를 순열로 모두 계산하여 이동 거리를 모두 더하고 가장 값이 작은 값으로 계산하기
        - 극단의 BFS
    
    - 예외처리 : (0 0)이 주어지면 프로그램 종료
    1. Input 데이터 입력받기
        - 입력받으며 로봇, 더러운 칸 장소 탐색 : O(WH)

    2. BFS 탐색을 통한 로봇 청소기를 기준으로 모든 칸과의 거리 측정
        - O(V + E)일 때 V = WH + 4 * WH = 5WH

    3. 모든 더러운 칸에 접근 가능한지 확인 후 로봇부터 더러운 칸까지의 거리 측정
        - 최대 9(K-1)번의 BFS 연산을 시행 : O(K-1 * 5WH)

    4. 모든 더러운 칸들 간의 거리를 계산하여 저장하기
        - 더러운 칸의 거리를 인접행렬로 나타내기


    5. 더러운 칸의 방문 순서를 순열로 만들기
        - 최대 10(K)! = 3,628,800개의 순열이 생성

    6. 방문 순서대로 방문하였을 때 거리 계산 후 최소값과 비교하기
        - 10(K)!의 방문 순서대로 최대 10(K)개의 더러운 칸을 방문해야하기 때문에 : O(K! * k)
    
"""
import sys
from collections import deque
from itertools import permutations
from typing import List, Tuple

input = sys.stdin.readline


def bfs(x: int, y: int) -> List[List]:
    q = deque([[x, y]])
    d = ((0, 1), (0, -1), (-1, 0), (1, 0))  # 상하좌우
    dists = [[-1] * w for _ in range(h)]
    dists[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            # print("탐색할 위치 : ", nx, ny)
            if 0 <= nx < h and 0 <= ny < w:
                if room[nx][ny] != "x" and dists[nx][ny] < 0:
                    dists[nx][ny] = dists[x][y] + 1
                    q.append((nx, ny))
            # print("현재 큐 상태 :", q)

    # # 디버깅 : 시작 위치로부터 최단 거리 확인
    # for row in dists:
    #     print(*row)
    # print()

    return dists


while True:
    answer: int = sys.maxsize
    robot: Tuple = ()
    dirty: List = list()

    # 1. Input 데이터 입력받기
    w, h = map(int, input().split())

    # 예외처리 : 0,0이 입력되었을 때 종료
    if w + h == 0:
        exit()

    ## 방 입력받기
    room = list()
    for i in range(h):
        # 한 행 입력받기
        row = list(input())
        for j, col in enumerate(row):
            # 로봇 위치와 더러운 칸 위치 기억
            if col in ("o", "*"):
                if col != "o":
                    dirty.append((i, j))
                else:
                    robot = (i, j)
        room.append(row)

    # 2. BFS 탐색을 통한 로봇 청소기를 기준으로 모든 칸과의 거리 측정
    dists = bfs(robot[0], robot[1])

    # 3. 모든 더러운 칸에 접근 가능한지 확인 후 로봇부터 더러운 칸까지의 거리 측정
    robot2dirty = []
    flag = False
    for x, y in dirty:
        if dists[x][y] < 0:
            flag = True
            break
        else:
            robot2dirty.append(dists[x][y])
    if flag:
        print(-1)
        continue

    # 4. 모든 더러운 칸들 간의 거리를 계산하여 저장하기
    ## 더러운 칸의 거리를 인접행렬로 나타내기
    dirty2dirty = [[0] * len(dirty) for _ in range(len(dirty))]  # 맵의 가장 큰 크기는 10 by 10
    for i in range(
        len(dirty) - 1
    ):  # -1을 하는 이유 : 인접행렬이 만들어지는 과정에서 대각선 기준 대칭으로 만들어지기에 마지막 요소는 안해도 자동으로 만들어져 있음
        dirty_dists = bfs(dirty[i][0], dirty[i][1])

        for j in range(i + 1, len(dirty)):
            # i번째 dirty 칸에서 j번째 dirty 칸까지 거리
            dirty2dirty[i][j] = dirty_dists[dirty[j][0]][dirty[j][1]]
            # j번째 dirty 칸에서 i번째 dirty 칸까지 거리
            dirty2dirty[j][i] = dirty2dirty[i][j]

    # 5. 최대 10개의 더러운 칸의 방문 순서를 순열로 만들기
    ## 최대 10! = 3,628,800
    permu = list(permutations(idx for idx in range(len(dirty))))
    # print("순열 :", permu)

    # 6. 방문 순서대로 방문하였을 때 거리 계산 후 최소값과 비교하기
    for p in permu:
        start = p[0]
        dist = robot2dirty[start]
        for j in range(1, len(p)):
            end = p[j]
            dist += dirty2dirty[start][end]
            start = end
        answer = min(answer, dist)

    print(answer)
    # # 디버깅 : 방 확인
    # for row in room:
    #     print(*row)

# 7 5
# .......
# .o...*.
# .......
# .*...*.
# .......
# 0 0

# 2 1 2 3 4 5 6
# 1 0 1 2 3 4 5
# 2 1 2 3 4 5 6
# 3 2 3 4 5 6 7
# 4 3 4 5 6 7 8

# 15 13
# .......x.......
# ...o...x....*..
# .......x.......
# .......x.......
# .......x.......
# ...............
# xxxxx.....xxxxx
# ...............
# .......x.......
# .......x.......
# .......x.......
# ..*....x....*..
# .......x.......
# 0 0

# 4 3 2 1 2 3 4 -1 14 15 16 17 18 19 20
# 3 2 1 0 1 2 3 -1 13 14 15 16 17 18 19
# 4 3 2 1 2 3 4 -1 12 13 14 15 16 17 18
# 5 4 3 2 3 4 5 -1 11 12 13 14 15 16 17
# 6 5 4 3 4 5 6 -1 10 11 12 13 14 15 16
# 7 6 5 4 5 6 7 8 9 10 11 12 13 14 15
# -1 -1 -1 -1 -1 7 8 9 10 11 -1 -1 -1 -1 -1
# 13 12 11 10 9 8 9 10 11 12 13 14 15 16 17
# 14 13 12 11 10 9 10 -1 12 13 14 15 16 17 18
# 15 14 13 12 11 10 11 -1 13 14 15 16 17 18 19
# 16 15 14 13 12 11 12 -1 14 15 16 17 18 19 20
# 17 16 15 14 13 12 13 -1 15 16 17 18 19 20 21
# 18 17 16 15 14 13 14 -1 16 17 18 19 20 21 22
