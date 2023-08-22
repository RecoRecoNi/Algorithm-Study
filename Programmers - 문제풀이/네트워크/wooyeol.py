"""
    네트워크
    https://school.programmers.co.kr/learn/courses/30/lessons/43162

    풀이시간 
    22:40 ~ 23:13(33분)
    
    문제 조건
    컴퓨터의 개수(n) : 1 ~ 200
    
    시간 복잡도 : O(n^2)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> BFS or DFS를 사용하여 네트워크의 개수 파악하기
    
    - 전체 컴퓨터를 대상으로 BFS 탐색을 진행한다.
        - 컴퓨터를 하나씩 확인하며 방문하지 않은 컴퓨터일 경우 탐색을 진행
        - 해당 컴퓨터 방문 처리 + 현재 컴퓨터와 네트워크를 형성하는 컴퓨터들을 탐색하기 위한 BFS 진행
            - 해당 컴퓨터를 기점으로 발생한 네트워크가 확인된 것이기 때문에 네트워크 개수 +1
"""
from typing import List
from collections import deque


def bfs(computer_idx: int, visited: List[bool], computers: List[List]):
    # 입력받은 컴퓨터를 큐에 삽입
    queue: deque = deque([computer_idx])

    while queue:
        # 큐의 탐색 대상 컴퓨터 확인
        target = queue.popleft()

        # 대상 컴퓨터와 연결된 컴퓨터 확인하기
        for connection_idx, connection in enumerate(computers[target]):
            # 해당 컴퓨터와 커넥션이 있는 컴퓨터 and 방문한 적이 없는 컴퓨터를 큐에 삽입하고 방문처리
            if connection and not visited[connection_idx]:
                visited[connection_idx] = True
                queue.append(connection_idx)


def solution(n: int, computers: List[List]):
    # 네트워크의 개수
    answer: int = 0

    # 방문한 컴퓨터 기록 테이블
    visited: List = [False for _ in range(n)]

    # 전체 컴퓨터를 대상으로 BFS 탐색
    for idx in range(n):
        # 방문하지 않은 컴퓨터일 경우 탐색을 진행
        if not visited[idx]:
            # 현재 컴퓨터 방문 처리
            visited[idx] = True

            # 현재 컴퓨터와 네트워크를 형성하는 컴퓨터들을 탐색하기 위한 BFS 진행
            bfs(idx, visited, computers)

            # 네트워크 갯수 추가하기
            answer += 1

    return answer


case1 = (3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])  # 2
case2 = (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])  # 1
print(solution(*case1))
print(solution(*case2))
