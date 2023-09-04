"""
풀이시간: 50분

<input>
- w, h: 방의 가로, 세로 (1 ≤ w, h ≤ 20)
- 방의 정보
    - .: 깨끗한 칸
    - *: 더러운 칸
    - x: 가구
    - o: 로봇 청소기의 시작 위치
- 더러운 칸의 개수는 10개를 넘지 않으며, 로봇 청소기의 개수는 항상 하나
- 입력의 마지막 줄에는 0이 두 개

<solution>
- 더러운 칸(최대 10)개의 순서를 모두 구하고(10!), 각 더러운 칸(10개)에 대해 BFS를 모두 돌리면 최악의 경우 10! * 400 * 10 = 14,515,200,000로 시간 초과
- 따라서, 매 순열마다 BFS를 수행하지 않고 미리 시작지점과 더러운 칸들 간의 거리를 계산 = O(W*H*10)
- 모든 순열을 만들어 모든 칸을 방문하는데 걸리는 시간 중 최소값을 구한다. -> 모든 순열을 구하는데 O(10! * 10)

<시간복잡도>
O(W * H * 10) + O(더러운 칸의 개수! * 더러운 칸의 개수) = 최대 36,292,000의 연산횟수
"""

import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def calculate_distance(distances, start, order):
    """
    distances: BFS를 통해 구한 각 더러운 칸까지의 거리
    start: 시작 인덱스
    order: 방문할 더러운 칸의 순서
    """
    distance = 0
    current = start
    for next_index in order:
        distance += distances[current][next_index]
        current = next_index
    return distance

def bfs(room, sx, sy):
    """
    room: 방의 구조를 나타내는 2차원 배열
    sx: 시작점 x좌표
    sy: 시작점 y좌표
    """
    n, m = len(room), len(room[0])
    dist = [[-1] * m for _ in range(n)] # 시작점에서 각 칸까지 이동하는데 걸리는데 필요한 최소 시간(거리)
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4): # 상하좌우 네 방향 탐색
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m: # 방의 범위 내
                if dist[nx][ny] == -1 and room[nx][ny] != 'x': # 이동할 칸이 아직 방문하지 않았고 가구가 아니라면
                    dist[nx][ny] = dist[x][y] + 1 # 해당 칸까지 거리 갱신
                    q.append((nx, ny))
    return dist

while True: # 테스트 케이스 입력받기
    w, h = map(int, input().split()) # 방의 가로, 세로
    if w == 0 and h == 0: # 입력의 마지막 줄
        break

    room = [input().rstrip() for _ in range(h)] # 방의 구조
    dirty = [(0, 0)] # 로봇 청소기가 꼭 방문해야 하는 칸
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o': # 로봇 청소기 시작 위치
                dirty[0] = (i, j)
            elif room[i][j] == '*': # 더러운 칸
                dirty.append((i, j))

    l = len(dirty) # 방문해야 하는 칸의 수
    distances = [[-1] * l for _ in range(l)] # 더러운 칸 간의 최단거리를 저장하는 2차원 배열 초기화
    ok = True

    for i in range(l):
        dist = bfs(room, dirty[i][0], dirty[i][1]) # (청소해야 하는)한 칸에서 다른 칸까지의 최단거리
        for j in range(l): # 최단 거리를 배열에 저장(distances[i][j]는 방문해야하는 청소기가 움직여야 하는 칸 i번 째에서 j번 째까지 가는데 걸리는 최단거리)
            distances[i][j] = dist[dirty[j][0]][dirty[j][1]]
            if distances[i][j] == -1: # 이동할 수 없는 칸이 있음
                ok = False

    if not ok: # 이동할 수 없는 칸이 있는 경우 -1 출력
        print(-1)
        continue

    start = 0 # 청소기의 index
    order = list(range(1, l)) # distances의 1~l까지는 더러운 칸의 index
    ans = float('inf') # 모든 칸을 깨끗하게 만드는데 필요한 이동 횟수의 최솟값

    for perm in permutations(order): # permutations를 통해 청소할 순서를 정함
        res = calculate_distance(distances, start, perm) # perm 순서대로 청소할 때 움직이는 거리
        min_distance = min(ans, res) # 최솟값 갱신

    print(ans)