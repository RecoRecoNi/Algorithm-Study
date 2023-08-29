"""

풀이시간
- 1시간 30분 (이후 해결 실패로 답지 참고)

접근법
- 시간복잡도 O(N^3) 까지도 가능?
    - 퀸 하나를 놓을 수 있는 최대 경우의수 : 15*15
    - 퀸의 개수 최대 15개
    - 즉 최대 경우의수 15**3
- 그래프 탐색 문제 -> DFS/BFS 로 접근 가능할 것 같음
    - 퀸을 하나씩 두어가며 경우의 수를 탐색하므로 DFS 가 적절할 것이라 판단
- 재귀가 아닌 방식을 활용해보고 싶어서 풀다가 포기 ㅠㅠ
    
회고
- DFS/BFS 가 조금은 익숙해진 느낌이지만 아직 구현하는 연습을 더 많이해야겠다고 느낌
    - DFS/BFS 원리를 조금 더 면밀히 이해할 필요가 있음
- 백트래킹? 개념은 몰랐지만 실패한 본인 풀이에서 백트래킹 개념으로 풀이하고 있었음
    - Q. 따로 공부하는 개념이 아니라 문제를 많이 풀어보는게 좋을까요?!

"""

from collections import deque

def is_safe(row, col, queens): # 주어진 행과 열의 위치에 퀸을 놓을 수 있는지 확인하는 함수
    for r, c in queens: # 기존 퀸의 위치 좌표를 받아옴
        if row == r or col == c or abs(row - r) == abs(col - c): # 같은행, 같은열, 대각선에 퀸이 있는지 확인
            return False # 퀸이 존재하므로 False 반환
    return True

def n_queen(n, row, queens): # DFS
    if row == n: # 모든 행 탐색이 끝났을 때 -> 모든 퀸을 다 놓은 것 -> 1 을 반환
        return 1

    count = 0
    for col in range(n): # 행을 입력으로 받은 후 해당 행의 모든 열을 순회
        if is_safe(row, col, queens): # 만약 특정 좌표에 퀸을 둘 수 있다면
            queens.append((row, col)) # 퀸 좌표 스택에 추가 (즉 퀸을 두었다고 볼 수 있음)
            count += n_queen(n, row + 1, queens)
            queens.pop()

    return count

N = int(input())
queens = deque()
result = n_queen(N, 0, queens)
print(result)

"""
ex : 8 -> 92

ex1 : 1 -> 1
ex2 : 2 -> 0
ex3 : 3 -> 0
ex4 : 4 -> 2
"""