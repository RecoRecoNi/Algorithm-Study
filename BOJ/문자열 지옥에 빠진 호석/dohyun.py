"""

풀이시간
- 약 1시간 풀이 후 실패로 답지 참조

접근법
- BFS 로 한번 탐색해보자
    - 각 선호 문자열마다 BFS 를 돌리면 너무 오래 걸림
    - 한번의 bfs 에 문자열 배열을 저장해놓고 선호 문자열이 존재하는지 여부를 조사하는 것이 나을듯

- 답지 풀이
    - BFS/DFS 둘 다 사용해도 상관없는듯 함
    - 본 풀이에서는 재귀로 구현이 편리한 DFS 활용
    - visit 배열이 아닌 딕셔너리를 활용
        - key: 문자열, value: 해당 문자열이 나올 수 있는 경우의수
    - 조건문이 아닌 나머지 연산을 활용하여 범위를 넘어간 DFS 를 구현

회고
- 하 문제 길ㄷㅏ ... 집중력이 많이 부족해서 놓친 부분이 꽤 있었음 (ex: 신이 좋아하는 문자열의 길이는 5이하 조건)

"""

import sys
sys.setrecursionlimit(987654321)

inputs = sys.stdin.readline

n, m, k = map(int, inputs().split())
arr = [list(inputs().rstrip()) for _ in range(n)]
ans, ans_list = {}, [] # 가능한 경우의 수를 담을 dict, 신이 선호하는 문자열 list

for _ in range(k):
    data = inputs().rstrip()
    ans[data] = 0
    ans_list.append(data)

directions = [(1,0), (0,1), (-1,0), (0,-1), (1,-1), (1,1), (-1,1), (-1,-1)]

def DFS(x, y, cnt, string):
    if cnt > 5: # 신이 좋아하는 문자열의 길이는 5이하
        return
    
    if string in ans: # 문자열이 딕셔너리에 존재 -> 가능한 경우의 수 +1
        ans[string] += 1

    for dx, dy in directions:
        nx, ny = (x + n + dx) % n, (y + m + dy) % m # 범위를 넘어가면 다시 돌아오는 조건에 맞게 변환
        DFS(nx, ny, cnt + 1, string + arr[nx][ny])

# 가능한 모든 그래프의 시작점에서 DFS 
for i in range(n):
    for j in range(m):
        start = ''
        DFS(i, j, 1, start + arr[i][j])

for k in ans_list:
    if k in ans:
        print(ans[k])