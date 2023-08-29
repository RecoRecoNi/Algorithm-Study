"""
풀이시간: 25분

<input>
- N(1 ≤ N < 15)

<solution>
- N X N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓기 위해서는 각 행에 1개의 퀸을 놔야 한다.
- 퀸은 상하좌우, 대각선으로 움직이기 때문에 위에서부터 아래로 내려오며 퀸을 배치할 수 있는 곳에 배치해야 한다.
- 모든 경우의 수를 확인하되, 퀸을 둘 수 없는 칸(상하좌우, 대각선 칸에 이미 다른 퀸이 있는 경우)에 대해 처리하기 때문에 백트래킹으로 풀이가 가능하다.
    1) 같은 열인지 확인: 같은 col을 가질 때
    2) 같은 ↗ 대각선에 있는지 확인: row + col값이 같을 때
    3) 같은 ↘ 대각선에 있는지 확인: row - col값이 같을 때

<시간복잡도>
열만 가지고 생각했을 때는 O(N!)일 수 있지만, 실제 백트래킹에서 가지치기가 빈번하게 발생하면 이보다 훨씬 시간복잡도가 줄어들기 때문에 제대로 파악하기 어려움
"""
n = int(input())
check_col = [False] * n # 같은 열에 다른 퀸이 있는지 확인하기 위한 배열
check_dig = [False] * (2*n-1) # ↗ 대각선을 확인하기 위한 배열: n x n 사각형의 대각선 개수는 (2*n-1)개
check_dig2 = [False] * (2*n-1) # ↘ 대각선을 확인하기 위한 배열: n x n 사각형의 대각선 개수는 (2*n-1)개

def go(row: int) -> int:
    if row == n: # 마지막 행까지 퀸을 모두 배치하면 종료
        return 1
    ans = 0 # (서로 공격할 수 없게) n개의 퀸을 놓을 수 있는 모든 경우의 수
    for col in range(n): # (row, col)에 퀸을 놓기
        # 같은 열에 퀸이 있거나, ↗, ↘ 대각선에 퀸이 있는 경우 퀸을 둘 수 없음(가지치기)
        if check_col[col] or check_dig[row+col] or check_dig2[row-col+n-1]:
            continue
        check_col[col] = True # (row, col)과 같은 열에 모든 칸에 퀸을 둘 수 없음
        check_dig[row+col] = True # (row, col)의 ↗ 대각선에 있는 모든 칸에 퀸을 둘 수 없음
        check_dig2[row-col+n-1] = True # (row, col)의 ↘ 대각선에 있는 모든 칸에 더 이상 퀸을 둘 수 없음
        ans += go(row+1)

        # 백트래킹
        check_col[col] = False
        check_dig[row+col] = False
        check_dig2[row-col+n-1] = False

    return ans

print(go(0))