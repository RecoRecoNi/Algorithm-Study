"""
    순서대로 방문하기
    https://softeer.ai/practice/info.do?idx=1&eid=2050

    풀이시간 
    22:08 ~ 22:50 (42분)
    
    문제 조건
    [조건 1] 2 ≤ n ≤ 4
    [조건 2] 2 ≤ m ≤ n**2
    
    시간 복잡도 :
    O(4**(n**2))

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 백 트래킹

    가능한 모든 경우를 계산하기 위해서는 백 트래킹을 통해서 가능한 방법을 모두 확인하는 것이 필요하겠다고 생각했습니다.

    1. table을 입력받고 block들을 입력받을 때는 0 인덱스가 시작지점이 될 수 있게 Lambda를 통해 좌표 형식을 통일합니다.
    2. 초기값 세팅을 위해서 시작 지점 세팅 및 시작 지점 방문 처리를 진행합니다.
    3. backtracking 진행
        1. 종료 컨디션 지정 : block의 인덱스와 m이 같아지면 모든 block을 방문했기 때문에 종료
        2. 4방향에 대해서 좌표값이 유효한지 벽 혹은 방문한 좌표가 아닌지 검사합니다.
        - 이상이 없다면 백트래킹을 위해 방문 처리를 진행하고 다시 재귀문을 통해서 현재 좌표가 현재 지나가야하는 
          좌표와 같다면 block 인덱스 증가 후 백 트래킹 진행 아니라면 인덱스 증가 없이 백 트래킹 진행
    
    4. 전체 answer를 반환합니다.
"""
import sys

input = sys.stdin.readline

# 재귀를 사용한 백 트래킹을 위한 answer 전역 변수 선언
global answer
answer = 0

# 데이터 입력
n, m = map(int, input().split())

table = [list(map(int,input().split())) for _ in range(n)]

transporation = lambda x : int(x) - 1
block = [tuple(map(transporation, input().split())) for _ in range(m)]

# 초기값 세팅
start_x,start_y = block[0]
table[start_x][start_y] = 1 # start 지점 방문 처리

# 방향 지정
directions = ((-1,0),(1,0),(0,-1),(0,1)) # 상하좌우
def backtracking(x, y, idx):
    # 전역변수 answer 사용
    global answer

    # 종료조건
    if idx == m:
        answer += 1
        return

    # 4방향에 대해서 검사를 진행
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 테이블 안에 존재하며 (벽이 아닐 경우 + 방문하지 않았을 경우)
        if 0 <= nx < n and 0 <= ny < n and table[nx][ny] == 0:

            # 방문처리
            table[nx][ny] = 1
            
            # 현재 방문해야하는 좌표일 경우
            if block[idx] == (nx, ny):
                # 다음 방문 인덱스 업데이트
                backtracking(nx, ny, idx+1)
            # 아닐 경우
            else:
                # 다른 방향으로 탐색 진행
                backtracking(nx, ny, idx)

            # 방문처리 해제
            table[nx][ny] = 0

# 백트래킹 기법을 통해 가능한 모든 경우를 계산한다.
backtracking(start_x, start_y, 1)

# 전역변수로 업데이트된 answer 출력
print(answer)