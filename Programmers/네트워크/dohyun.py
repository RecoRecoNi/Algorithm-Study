"""

풀이시간
- 약 1시간

접근법
- N = 200 -> 시간 복잡도 크게 고려하지 않아도 될 것 같음 (각 배열을 고려해 N^2 해도 충분)
- 모든 컴퓨터를 탐색하여 연결 정보를 찾아야 함 
    - 그래프 탐색 알고리즘(DFS/BFS)을 사용해야겠다라고 판단
- 제한 시간을 초과해서 답지를 봤습니다 .. ㅎ

회고
- DFS/BFS 유형은 매우 중요한데도 거의 손도 못대겠음 ㅠㅠ 해당 유형 문제 많이 풀어보기

"""

def solution(n, computers):
    def dfs(node):
        visited[node] = True # 현재 노드 방문 표시
        for neighbor in range(n): # 모든 노드 반복
            if computers[node][neighbor] == 1 and not visited[neighbor]: # 현재 노드와 연결되어 있고 and 방문하지 않은 노드
                dfs(neighbor)
    
    visited = [False] * n
    networks = 0
    
    for i in range(n):
        if not visited[i]: # 방문하지 않은 노드에 대해 dfs 실시
            dfs(i)
            networks += 1
    
    return networks

print(solution(n=3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print('----------')
print(solution(n=3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1