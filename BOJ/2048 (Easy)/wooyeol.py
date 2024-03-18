"""
    2048 (Easy)
    https://www.acmicpc.net/problem/12100

    풀이시간 
    14:11 ~ 15:02(오답)
    4시간 정도 재 풀이 및 레퍼런스 참고 (실패)
    
    - 실패한 풀이 -
"""
import sys
import copy

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def oob(x,y,dx,dy):
    return 0 <= x + dx < N and 0 <= y + dy < N
    # return (0 > x + dx) or (x + dx > N) or (y + dy < 0) or (y + dy > N)

def swipe(direction, t_board):
    # col,row
    l_row, l_col = len(t_board), len(t_board[0])

    # 상하좌우
    directions = ((-1,0), (1,0), (0,-1), (0,1))
    directions_increase = ((range(1,l_row), range(l_row-2,-1,-1), range(1, l_col),range(l_col-2,-1,-1)))
    
    # 상 하 움직일 경우
    if direction in (0, 1):
        for c_idx in range(l_col):
            is_combined = [False] * l_row
            for r_idx in directions_increase[direction]:
                x, y = r_idx, c_idx

                # 빈칸이면 이동하지 않는다.
                if t_board[x][y]:
                    # 주어진 방향으로 한 칸 이동
                    dx, dy = directions[direction]
                    nx, ny = x + dx, y + dy

                    # nx,ny가 보드를 벗어난 다면 Break
                    if not oob(x, y, dx, dy):
                        break

                    # print(nx, ny, x, y)

                    # 빈칸일 경우
                    if t_board[nx][ny] == 0:
                        t_board[nx][ny] = t_board[x][y]
                        t_board[x][y] = 0

                    # 같은 값이 있는 경우
                    if t_board[nx][ny] == t_board[x][y] and not is_combined[nx]:
                        t_board[nx][ny] *= 2
                        t_board[x][y] = 0
                        is_combined[nx] = True

        print("\nAfter Swipe", direction)
        for row in t_board:
            print(*row)
            
    # 좌 우 움직일 경우
    elif direction in (2, 3):
        for r_idx in range(l_row):
            is_combined = [False] * l_col
            for c_idx in directions_increase[direction]:
                x, y = r_idx, c_idx
                
                # 빈칸이면 이동하지 않는다.
                if board[x][y]:
                    # 주어진 방향으로 한 칸 이동
                    dx, dy = directions[direction]
                    nx, ny = x + dx, y + dy
                    
                    # nx,ny가 보드를 벗어난다면 Break
                    if not oob(x, y, dx, dy):
                        break

                    # 빈칸일 경우
                    if t_board[nx][ny] == 0:
                        t_board[nx][ny] = t_board[x][y]
                        t_board[x][y] = 0

                    # 같은 값이 있는 경우
                    if t_board[nx][ny] == t_board[x][y] and not is_combined[ny]:
                        t_board[nx][ny] *= 2
                        t_board[x][y] = 0
                        is_combined[ny] = True
            

max_value = -1

def dfs(repeat, board):
    # 종료 조건
    if repeat == 1:
        global max_value
        
        # flag = False
        for row in board:
            temp_max_value = max(row)
            if temp_max_value > max_value:
                # flag = True
                max_value = temp_max_value
        # if flag:
        #     print("\n",max_value)
        #     for row in board:
        #         print(*row)

        return
    
    temp = copy.deepcopy(board)
    # 상 하 좌 우
    for direction in range(4):
        swipe(direction, temp)
        dfs(repeat+1, temp)
        temp = copy.deepcopy(board)
        
    

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dfs(0, board)
print(max_value)