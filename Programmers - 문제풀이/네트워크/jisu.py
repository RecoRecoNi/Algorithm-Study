'''
풀이 시작 : 2023-08-21 12:13

- 그래프 탐색 문제로 보이고 n도 200 이하이므로, 보통의 그래프 탐색 알고리즘(BFS, DFS)을 적용해도 될 것이다.
- 결국 전체 네트워크가 몇 덩어리로 나뉘어져 있는지를 알면 되므로, BFS를 적용해 탐색이 몇 번 일어나는지 확인하면 된다.
- 다만 주어진 인접행렬은 현재 두 컴퓨터가 연결되었다는 정보를 나타내므로, BFS탐색을 용이하게 하기 위해 각 컴퓨터가 연결 중인 다른 컴퓨터의 
리스트를 따로 관리할 필요가 있다.

풀이 완료 : 2023-08-21 12:40 (풀이 시간 27분)

- 근데 풀이하다 보니 인접 행렬을 재구성 하는 과정 없이 풀이가 가능할 것 같다. 탐색 인덱스를 적절히 활용하면 될 것 같다. 
    -> 인접 행렬을 그대로 활용한 풀이 추가
- camel -> snake
'''
from typing import List, Deque
from collections import deque, defaultdict

networks = defaultdict(list)
visited: List[bool] = list()

def bfs(init_computer:int):
    visited[init_computer] = True                    # 초기 컴퓨터 방문 처리
    queue: Deque[int] = deque([init_computer])

    while queue:
        cur_computer = queue.popleft()

        for computer in networks[cur_computer]:      # 현재 탐색 중인 컴퓨터와 연결된 컴퓨터들을 탐색
            if not visited[computer]:                   # 그 중 아직 방문되어있지 않은 컴퓨터들에 대해서만
                queue.append(computer)                  # 큐에 넣고 탐색
                visited[computer] = True

    return 1                                        # 정상 탐색 완료시 1 반환


def solution(n: int, computers: List[List[int]]) -> int:
    '''
    컴퓨터가 연결되어있다는 정보를 나타내는 인접 행렬을 특정 컴퓨터에 대한 연결 컴퓨터들을 담은 dict로 변환한 풀이
    '''

    global networks, visited
    num_of_networks: int = 0
    visited = [False for _ in range(n)]     # 컴퓨터들의 탐색 여부 관리

    for r in range(n):                      # dict: {컴퓨터 : [연결된 컴퓨터 들]} 로 관리
        for c in range(n):
            if computers[r][c]:
                networks[r].append(c)       # 양방향 연결되어있음에 주의해야 함
                networks[c].append(r)

    for computer in range(n):               
        if not visited[computer]:
            num_of_networks += bfs(computer)  # 정상적인 탐색이 한 번 끝나면 하나의 네트워크가 형성되어 있다는 것임

    return num_of_networks

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

def bfs_adjMatrix(init_computer: int, computers: List[List[int]]) -> int:
    global visited
    
    queue = deque([init_computer])
    visited[init_computer] = True
    
    while queue:
        cur_computer = queue.popleft()       
        for nxt_computer, is_connect in enumerate(computers[cur_computer]):   # 현재 탐색 중인 컴퓨터의 연결 정보 순회
            if is_connect and not visited[nxt_computer]:                       # 연결되어있고 아직 방문되지 않은 컴퓨터만 탐색
                queue.append(nxt_computer)
                visited[nxt_computer] = True           
    return 1

def solution_adjMatrix(n: int, computers: List[List[int]]) -> int:
    '''
    주어진 인접 행렬을 그대로 활용한 풀이
    '''
    global visited
    num_of_networks: int = 0
    visited = [False for _ in range(n)]
    
    for computer in range(n):
        if not visited[computer]:
            num_of_networks += bfs_adjMatrix(computer,computers)

    return num_of_networks


def main() -> None:
    case1 = [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]]  # 2
    case2 = [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]  # 1
    print(solution(*case1))
    print(solution(*case2))

main()


