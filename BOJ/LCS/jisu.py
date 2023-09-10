"""
풀이 시작 : 2023-09-10 18:50

- st1과 st2 각각의 문자에 대응하는 matrix(dp 테이블)를 그리기
-----------------
_ A C A Y K P
C 0 1 1 1 1 1       -> A C A Y K P 에서 C 까지 고려했을 때 LCS 길이
A 1 1 2 2 2 2       -> A C A Y K P 에서 C A 까지 고려했을 때 LCS 길이 
P 1 1 2 2 2 3
C 1 2 2 2 2 3
A 1 2 3 3 3 3
K 1 2 3 3 4 4       -> A A C Y K P 에서 C A P C A K 까지 고래했을 때 LCS 길이
-----------------
- 규칙이 보임
    - [r][c]에 대응하는 두 문자열의 문자가 같을 경우 왼쪽 위 대각선([r-1][c-1])에서 +1이 증가함
    - [r][c]에 대응하는 두 문자열의 문자가 다를 경우 왼쪽([r][c-1]), 위쪽([r-1][c]) 중 큰 값이 옴
- r, c가 각각 0일 때에 대한 예외 처리
    - 그냥 임시로 행, 열 하나씩 늘려서 처리하면 동일하게 로직 적용 가능

풀이 완료 : 2023-09-10 19:45(풀이 시간 : 55분)

"""

import sys

input = sys.stdin.readline

st1 = input().rstrip()
st2 = input().rstrip()

dp = [[0 for _ in range(len(st1) + 1)] for _ in range(len(st2) + 1)]

for r in range(1, len(st2) + 1):
    for c in range(1, len(st1) + 1):
        if st2[r - 1] == st1[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])


print(dp[-1][-1])
