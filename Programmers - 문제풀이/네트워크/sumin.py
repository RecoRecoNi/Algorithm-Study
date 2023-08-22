"""
풀이시간: 15분

<input>
- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수
- 각 컴퓨터는 0부터 n-1인 정수로 표현
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현
- computer[i][i]는 항상 1

<solution>
- 각각의 컴퓨터를 하나의 노드로 봤을 때, 연결된 형태(네트워크)의 개수를 찾기 위해서는 DFS를 수행하면 된다.
    - DFS는 스택, 재귀 둘 다로 구현 가능한데 일반적으로 스택 구조가 더 빠르다.

<시간 복잡도>
O(n^2)
- n은 그래프의 노드 수(computers의 크기)
"""
from typing import List

# 스택 구조로 구현
def dfs_stack(computers:List, visited:List, start:int) -> None:
    n = len(computers)
    stack = [start]
    while stack:
        v = stack.pop() # 현재 노드
        if not visited[v]:
            visited[v] = True # 방문처리
            for i in range(n): # v에서 출발하는 모든 노드를 확인
                if computers[v][i] == 1 and not visited[i]: # 아직 방문하지 않은 노드만 스택에 추가
                    stack.append(i)

# 재귀 구조로 구현
def dfs_recur(computers:List, visited:List, start:int) -> None:
    n = len(computers)
    visited[start] = True # 현재 노드 방문처리
    for i in range(n):
        if computers[start][i] == 1 and not visited[i]: # 아직 방문하지 않은 노드(컴퓨터)에 대해
            dfs_recur(computers, visited, i) # DFS 수행


def solution(n:int, computers: List) -> int:
    answer = 0 # 네트워크의 개수
    visited = [False] * n # 방문처리 배열
    for i in range(n):
        if not visited[i]: # 아직 방문하지 않은 노드 -> DFS 수행
            dfs_stack(computers, visited, i) # dfs_recur로도 가능
            answer += 1
    return answer


# 테스트 케이스
n1, computers1 = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n2, computers2 = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n2, computers2))



"""
1) 스택 구조
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10MB)
테스트 4 〉	통과 (0.05ms, 10MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.15ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.11ms, 10.1MB)
테스트 9 〉	통과 (0.14ms, 10.1MB)
테스트 10 〉	통과 (0.07ms, 10.1MB)
테스트 11 〉	통과 (0.52ms, 10.2MB)
테스트 12 〉	통과 (0.41ms, 10.2MB)
테스트 13 〉	통과 (0.20ms, 10.2MB)

2) 재귀 구조
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.27ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.17ms, 10.2MB)
테스트 9 〉	통과 (0.10ms, 10.2MB)
테스트 10 〉	통과 (0.10ms, 10.3MB)
테스트 11 〉	통과 (0.93ms, 10.3MB)
테스트 12 〉	통과 (0.76ms, 10.2MB)
테스트 13 〉	통과 (0.35ms, 10.2MB)
"""