"""

풀이시간
- 약 7시간 (공부하면서 같이 풀었습니다!!)

접근법
- 불의 좌표를 구해서 행렬 값을 번지는 불로 바꿔볼까? -> 시간복잡도 걸릴 것 같음
- 불의 좌표 구하고 행렬 값을 바꾸지말고 불 인덱스를 추가하자 -> 불에 닿으면 IMPOSSIBLE
- 그리고 불이나 벽이나 글로 못가는건 똑같음 -> 벽 인덱스도 추가
- 문제에서 보면 "불이 도달하기 전에" -> "불이 도착점에 도달하기 전에"
    - 지훈이의 탈출 지점에 불이 더 빨리 도착하냐? 지훈이가 더 빨리 도착하냐? 를 계산하면 될것같음
- 계속 보다보니 예전에 잠깐 봤던 BFS 가 생각나서 BFS 알고리즘 코드는 인터넷에서 배꼈습니당 .. ㅎ 
    - 혼자 BFS 를 짜다보니 도저히 감도 안오고 시간도 오래걸리고, 외우다시피 익숙해지는게 좋다고 해서 우선은 배꼈습니다!! 앞으로 연습 많이 할게요!!

회고
- 왜 틀렸다고 뜨는지 도저히 잘 모르겠어요 ,, ㅠㅠ 어디 때문에 안되는지 혹시 아시겠다면 말씀해주시면 정말 감사하겠습니다 !!!

"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    ex = [x for x in sys.stdin.readline().rstrip()]
    board.append(ex)

row_idx = 0

# 불과 지훈이의 초기점 찾기
for i in range(n):
    for j in range(m):
        element = board[i][j]
        if element=='F':
            fire_idx = (i, j)
        elif element=='J':
            jihoon_idx = (i, j)

# 상하좌우 네 방향을 의미
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]  

def bfs(start_idx):
    vis = [[-1] * m for _ in range(n)]  # 해당 칸을 방문했는지 여부를 저장
    Q = deque()
    vis[start_idx[0]][start_idx[1]] = 0  # 시작점의 좌표를 방문했다고 명시
    Q.append(start_idx)  # 큐에 시작점인 좌표를 삽입.

    escape = []
    count = 0

    while Q:
        cur = Q.popleft()
        # 걸린 시간 증가
        count += 1
        # print("cur:", cur, "value:", vis[cur[0]][cur[1]]) # 디버깅을 위함

        for dir in range(4):  # 상하좌우 탐색
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            
            # 정상적인 범위안에 들어왔을 경우
            if 0 <= nx < n and 0 <= ny < m:
                # 이미 방문한 칸이 아니거나 벽, 불이 아닌 경우
                if (vis[nx][ny]==-1) & (board[nx][ny]!="#") & (board[nx][ny]!="F"): 
                    vis[nx][ny] = count  # (nx, ny) 에 걸린 시간을 입력
                    Q.append((nx, ny))
            
            # 정상적인 범위를 넘어감 -> 즉 탈출에 성공!
            else:
                # 탈출 직전의 좌표를 받음
                escape.append(cur)

    return vis, escape

fire_visit, fire_escape = bfs(fire_idx)
jihoon_visit, jihoon_escape = bfs(jihoon_idx)

answer = []

# 지훈이가 도착점까지 걸린시간보다 불이 더 늦게 도착했는지 확인
for escape_point in jihoon_escape:
    x, y = escape_point[0], escape_point[1]
    if (jihoon_visit[x][y] < fire_visit[x][y]) or (fire_visit[x][y]==-1):
        answer.append(jihoon_visit[x][y] + 1)


if answer:
    print(min(answer))

else:
    print("IMPOSSIBLE")


"""
### ex -> 3
4 4
####
#JF#
#..#
#..#
"""

"""
### ex1 -> 1
3 2
##
#J
#F
"""

"""
### ex2 -> 3
4 4
F###
#J##
#...
#.##
"""

"""
### ex3 -> 2
4 4
#.##
#.F#
#J##
#.##
"""