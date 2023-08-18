"""
풀이시간: 25분

<input>
- 1 ≤ N ≤ 15
- 0 ≤ r, c < 2N

<solution>
1. 함수의 정의
- 2^n x 2^n 배열에서 (r,c)를 방문하는 순서를 반환하는 함수

2. base condition
- n = 0일 때, return 0

3. 재귀식
- (r,c)가 1번 사각형일 때, return go(n-1, r, c)
- (r,c)가 2번 사각형일 때, return half*half + go(n-1, r, c-half)
- (r,c)가 3번 사각형일 때, return 2*half*half + go(n-1, r-half, c)
- (r,c)가 4번 사각형일 때, return 3*half*half + go(n-1, r-half, c-half)

"""
def go(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    if r < half and c < half: # 1사분면
        return go(n-1, r, c)
    elif r < half and c >= half: # 2사분면
        return half * half + go(n-1, r, c-half)
    elif r >= half and c < half: # 3사분면
        return 2 * half * half + go(n-1, r-1, c)
    return 3 * half * half + go(n-1, r-half, c-half) # 4 사분면


n, r, c = map(int, input().split())
print(go(n, r, c))