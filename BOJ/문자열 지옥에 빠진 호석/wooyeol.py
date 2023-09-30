"""
    문자열 지옥에 빠진 호석
    https://www.acmicpc.net/problem/20166

    풀이시간 
    12:42 ~ (문제 풀이 실패)
    
    문제 조건
    3 <= N,M <= 10
    1 <= K <= 1,000
    1 <= 신이 좋아하는 문자열 <= 5

    시간 복잡도 :
    O(N * M * 8^5 + K)
    O(3,277,800)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> BFS 탐색

    1. 만들어질 수 있는 모든 문자열을 탐색하여 해시테이블에 등록
    2. 등록된 해시 테이블의 값에서 입력받은 문자열의 값을 반환
"""
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

# 상, 하, 좌, 우, 대각선 왼쪽 위, 대각선 오른쪽 위, 대각선 왼쪽 아래, 대각선 오른쪽 아래
directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1))

def bfs(x, y):
    queue = deque()
    queue.append([x, y, table[x][y]])

    while queue:
        x, y, text = queue.popleft()
        
        # 지금까지 확인된 문자열의 갯수 증가
        answer_dict[text] += 1

        # 문자열의 길이가 5 이상이라면 더 이상 검색하지 않는다.
        if len(text) >= 5:
            continue
        
        # BFS 탐색
        for dx, dy in directions:
            # nx,ny의 환형 구조를 반영
            nx, ny = (x + dx) % N, (y + dy) % M

            # 다음 탐색할 노드 추가
            queue.append((nx, ny, text + table[nx][ny]))

N, M, K = map(int, input().split())

# N by M 의 격자 
table = []
for _ in range(N):
    table.append(input().rstrip())

# 격자에서 가능한 모든 문자열 갯수 탐색
answer_dict = defaultdict(int)
for row_i, row in enumerate(table):
    for col_i, col in enumerate(row):
        bfs(row_i, col_i)

# 입력받은 문자열의 갯수 출력
for _ in range(K):
    # 입력 받은 신이 좋아하는 문자열
    target_string = input().rstrip()
    print(answer_dict[target_string])
