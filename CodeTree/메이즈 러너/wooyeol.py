"""
    메이즈 러너
    https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=1&pageSize=20

    풀이시간 
    10:20 ~ 11 :54
    13:12 ~ 14: 04
    14:14 ~ 18:09 (6시간 19분)
        
    문제 조건
    N: 미로의 크기 (4≤N≤10)
    M: 참가자 수 (1≤M≤10)
    K: 게임 시간 (1≤K≤100)

    시간 복잡도 : 
    O(K * (M^2 + M + MlogM + N^2 + M + N^2))
    O(100 * (100 + 10 + 10log10 + 100 + 10 + 100))

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 시뮬레이션

    1초 동안 진행하기 위해 필요한 연산들
    
    - 현재 턴에 모든 플레이어 이동
        - 1초마다 상하좌우를 검사하고 최단 거리가 갱신되는 칸으로 이동

    - 가장 작은 정사각형 확인하기
        - 모든 플레이어를 기준으로 좌상단에 가까운 가장 작은 사각형을 만들고 그 중에서 가장 작은 정사각형 반환

    - 가장 작은 정사각형 회전하기
        - 임시 정사각형을 만들어서 회전시킨 값을 저장시키고 회전된 값을 다시 미로에 적용
"""
import sys

input = sys.stdin.readline

def oob(nx, ny):
    return nx < 0 or nx >= N or ny < 0 or ny >= N

def calc_distance(x, y):
    return abs(x-exit_coordinate[0]) + abs(y-exit_coordinate[1])

def move(players):
    global exit_coordinate

    move_distance = 0

    escape_players = []
    added_players = []

    # 상 하 좌 우
    directions = ((-1,0),(1,0),(0,-1),(0,1))

    # 모든 플레이어 이동
    for player in players:
        player_x, player_y = player

        # 상 하 좌 우를 탐색하며 이동 할 수 있는 공간 확인
        for dx, dy in directions:
            nx, ny = player_x + dx, player_y + dy
            new_player = (nx,ny)

            # 범위 밖으로 이동 불가
            if oob(nx,ny):
                continue
            
            # 최단거리가 갱신된다면
            if (calc_distance(nx, ny) < calc_distance(player_x, player_y)) and maze[nx][ny] == 0:
                # 이동거리 증가 + 플레이어 이동
                move_distance += 1
                
                # 탈출 리스트
                if nx == exit_coordinate[0] and ny == exit_coordinate[1]:
                    escape_players.append(player)
                else:
                    # 이전 위치 제거 후 다음 플레이어 추가
                    escape_players.append(player)
                    added_players.append(new_player)

                # 이미 이동했기 때문에 바로 다음 사람으로 넘어가기
                break

    # 탈출한 플레이어 제거
    for e_player in escape_players:
        players.remove(e_player)
    
    # 이동한 위치 추가
    for a_player in added_players:
        players.append(a_player)

    return move_distance

def find_square(players):
    global exit_coordinate 
    
    square = []

    for player_x, player_y in players:
        # 정사각형의 한 변의 길이
        row_dif, col_dif =  abs(player_x - exit_coordinate[0]), abs(player_y - exit_coordinate[1])
        length = max(row_dif + 1, col_dif + 1)

        # 정사각형의 좌대각 위 좌표
        s_r, s_c = max(player_x, exit_coordinate[0]) - length + 1, max(player_y, exit_coordinate[1]) - length + 1
        s_r, s_c = max(0, s_r), max(0, s_c)

        square.append([length, s_r, s_c])
    
    square.sort(key=lambda x : (x[0],x[1],x[2]))

    return square[0]

def rotate_square(length, square_r, square_c):
    global exit_coordinate

    temp_square = [[0] * length for _ in range(length)]

    # 임시 정사각형 회전한 값 저장
    for r in range(length):
        for c in range(length):
            temp_square[c][length - 1 - r] = maze[square_r + r][square_c + c]
            if (square_r + r,square_c + c) == exit_coordinate:
                temp_square[c][length - 1 - r] = "#"

    # 회전하는 값 중에 player가 있다면 해당 값을 -1로 표기
    remove_list = []
    for (player_r,player_c) in players:
        r, c = player_r - square_r, player_c - square_c
        if 0 <= r < length and 0 <= c < length:
            remove_list.append((player_r,player_c))
            temp_square[c][length - 1 - r] += -1
        
    for removed in remove_list:
        players.remove(removed)

    # 회전된 값을 다시 미로에 적용
    for r in range(length):
        for c in range(length):
            # 회전된 플레이어 다시 추가
            if temp_square[r][c] != "#" and temp_square[r][c] < 0:
                modify_player = (square_r + r, square_c + c)
                for _ in range(-temp_square[r][c]):
                    players.append(modify_player)
                temp_square[r][c] = 0

            # 회전된 exit_coordinate 위치 업데이트
            elif temp_square[r][c] == "#":
                exit_coordinate = (square_r + r, square_c + c)
                temp_square[r][c] = 0
            
            # 빈칸이 아니면
            if temp_square[r][c]:
                # 내구도를 감소시킴
                maze[square_r + r][square_c + c] = temp_square[r][c] - 1
            else:
                # 빈칸 업데이트
                maze[square_r + r][square_c + c] = 0


# 데이터 입력
N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
players = list(tuple(map(lambda x : int(x)-1, input().split())) for _ in range(M))
exit_coordinate = tuple(map(lambda x : int(x)-1, input().split()))

# K초 동안 게임 진행
total_distance = 0
# print(players)

# for _ in range(K):
for k in range(K):
    # 현재 턴에 플레이어 이동
    total_distance += move(players)
    # print(players)

    if not players:
        break

    # 가장 작은 정사각형 확인하기
    square = find_square(players)

    # 가장 작은 정사각형 회전하기
    rotate_square(*square)

print(total_distance)
print(exit_coordinate[0]+1, exit_coordinate[1]+1)