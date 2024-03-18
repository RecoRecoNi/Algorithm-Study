"""

풀이시간
- 약 1시간 풀이 후 실패로 답지 참조

접근법
- 주어진 변수의 범위가 굉장히 좁음 -> 구현에 집중
- 특정 조건이 있는 그래프 탐색 -> 백트래킹
- visit 배열을 초기화하는 작업이 필요

회고
- 인덱스로 goals 좌표 접근하는 방식 익숙해지기

"""

import sys

lines = []

for line in sys.stdin:
    lines.append(list(map(int, line.split())))

n, m = lines[0]  # 격자의 크기, 순서대로 방문해야 하는 칸의 수
board = lines[1:n + 1]  # 격자
goals = [list(map(lambda val: val - 1, line)) for line in lines[n + 1:]]  # 방문해야 할 칸의 위치 (x,y)

visited = [[False] * n for _ in range(n)]
directions = [(0,1), (1,0), (-1,0), (0,-1)]
cnt = 0

visited[goals[0][0]][goals[0][1]] = True

# 이동이 유효한지 검사
def is_valid(x, y):
    return (
      x > -1 and x < n and y > -1 and y < n and board[x][y] == 0 and not visited[x][y]
    )

# 백트래킹 탐색
def back_tracking(idx, x, y):
    # 마지막으로 방문해야 할 칸에 도달한 경우
    if idx == len(goals) - 1:
        if goals[idx] == [x, y]:
            global cnt
            cnt += 1
            return
        
    # 다음 칸을 목표로 백트래킹
    elif goals[idx] == [x, y]:
        back_tracking(idx + 1, x, y)
    
    # 상하좌우 이동 가능하면 방문, 백트래킹 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if is_valid(nx, ny):
            visited[nx][ny] = True
            back_tracking(idx, nx, ny)
            visited[nx][ny] = False

back_tracking(1, goals[0][0], goals[0][1])

print(cnt)