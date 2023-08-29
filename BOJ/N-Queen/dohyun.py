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
- 행을 고정하여 탐색을 시작하는 것이 중요했던 것 같음

"""

import sys
limit_number = 987654321
sys.setrecursionlimit(limit_number)

def n_queen(n, row, columns, diagonals1, diagonals2):
    if row == n:
        return 1  # 모든 행에 퀸을 배치한 경우 1을 반환하여 가능한 경우의 수를 세기 시작

    count = 0  # 퀸을 놓을 수 있는 경우의 수

    # 현재 행에서 가능한 모든 열을 확인하며 백트래킹
    for col in range(n):
        # 만약 해당 열이나 대각선에 퀸이 이미 존재하면 다음 열로 넘어감
        if columns[col] or diagonals1[row + col] or diagonals2[row - col]:
            continue

        # 현재 위치에 퀸을 배치하고 충돌 체크를 업데이트
        columns[col] = diagonals1[row + col] = diagonals2[row - col] = True

        # 다음 행으로 넘어가면서 가능한 경우의 수를 재귀적으로 탐색
        count += n_queen(n, row + 1, columns, diagonals1, diagonals2)

        # 퀸 배치를 되돌리고 다음 열로 넘어감
        columns[col] = diagonals1[row + col] = diagonals2[row - col] = False

    return count

N = int(input()) # N 하나만 받으므로 sys 모듈 사용하지 않아도 문제 없음

# 각 열, 대각선의 충돌 여부를 저장하는 배열 초기화
columns = [False] * N
diagonals1 = [False] * (2 * N - 1) # 왼쪽 위에서 오른쪽 아래로 향하는 대각선 (0, 0 ~ n-1, n-1)
diagonals2 = [False] * (2 * N - 1) # 오른쪽 위에서 왼쪽 아래로 향하는 대각선 (0, n-1 ~ n-1, 0)

# 첫 행부터 탐색 시작
result = n_queen(N, 0, columns, diagonals1, diagonals2)
print(result)