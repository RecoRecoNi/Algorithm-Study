"""
풀이 시작 : 2023-09-28 17:22

#### 제한 사항
신이 좋아하는 문자열의 길이를 N이라고 할 때

- matrix는 최대 10 x 10
- K <= 1000
- 문자열 길이 : 1 <= N <= 5
- 복잡도 최대 : 10 x 10 x 1000 x 5 = 5,000,000
- (결과론) 완탐 가능할 것 같지만, dfs 돌릴 때 백트래킹 안하면 시간초과!

#### 풀이
- 알파벳 N이 될 때까지 각 이동마다 재귀해서 문자열이랑 같은 경우 카운트하면 될듯!
- 대신 다시 방문하는 걸 허용하니 visited 필요 없음
- target이 중복으로 주어질 수 있으므로 target에 대한 dict 만들어서 해 저장해놓기
- dfs 과정에서 완탐은 안되고, 백트래킹 수행해야 함! 다음 탐색해야할 문자열이 같을 때만 가지 뻗기

#### 의문 
- 46번 라인의 조건문은 없어도 될 것 같은데, 없으면 전체 통과가 안됨(2/16)
    - 다음 문자가 같을 때만 가지를 뻗으니까.. 되어야 하는데.. 외 안되?
- 의문 해결! 처음 재귀 시작할 때에도 같을 때만 재귀하도록 해줘야 했음! (수정 완료)

풀이 완료 : 2023-09-28 17:49(풀이 시간 : 27분 소요)

메모리 | 시간
-- | --
31256KB | 580ms
"""

import sys

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
matrix = [input().rstrip() for _ in range(N)]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dx = [0, 0, -1, 1, -1, 1, -1, 1]
target_dict = {}
cnt = 0


def dfs(string: str, row: int, col: int):
    global cnt

    if len(string) == len(target):  # 종료 조건 : target의 길이와 같을 때
        cnt += 1  # 카운트
        return

    for d in range(8):
        nxt_row = (row + dy[d] + N) % N  # 환형 좌표 처리
        nxt_col = (col + dx[d] + M) % M

        # 백트래킹 : 다음 탐색해야할 문자가 같을 때만 가지 뻗기
        if target[len(string)] == matrix[nxt_row][nxt_col]:
            dfs(string + matrix[nxt_row][nxt_col], nxt_row, nxt_col)


for _ in range(K):
    target = input().rstrip()
    if target in target_dict:  # target이 중복해서 주어지는 경우
        print(target_dict[target])
    else:
        cnt = 0
        for row in range(N):  # matrix 내 어디서든 시작할 수 있음
            for col in range(M):
                if matrix[row][col] == target[0]:  # 첫 문자 같을 때만 재귀 시작
                    dfs(matrix[row][col], row, col)

        target_dict[target] = cnt  # target의 해 저장해놓기
        print(cnt)
