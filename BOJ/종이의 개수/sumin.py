"""
풀이시간: 30분

<input>
N(1 ≤ N ≤ 37, N은 3k 꼴) -> N x N 행렬

<solution>
1. (x, y, n)이 같은 수로 돼있는지 확인
2. 그렇지 않으면 9등분하고 다시 확인

<시간복잡도>
O(n^2 * log_3(n))
"""

# 해당 종이 내부에 같은 숫자로만 채워졌는지 확인하는 함수
def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

# (x, y)부터 가로로 n개, 세로로 n개의 종이 개수를 확인하는 함수
def solve(x, y, n):
    if check(x, y, n): # 만약 같은 숫자로만 이루어져있다면
        cnt[paper[x][y]+1] += 1 # 해당 숫자의 개수 갱신
        return
    m = n // 3
    # 9등분
    for i in range(3):
        for j in range(3):
            solve(x+i*m, y+j*m, m)


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)] # 종이
cnt = [0] * 3 # -1, 0, 1로 채워진 종이 갯수
solve(0, 0, n)
print('\n'.join(map(str, cnt)))
