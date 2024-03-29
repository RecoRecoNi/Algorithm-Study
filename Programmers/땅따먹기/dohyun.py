"""

풀이시간
- 약 1시간 풀이 후 실패로 답지 참조

접근법
- N 10만 이하 -> O(NlogN)
- 그리디? -> 현재 행에서 최대라고 해서 합이 최대가 되는게 아니기 때문에 X
- 열은 왜 4개로 고정? -> 각 열별로 결과를 저장해놓으면 될듯
- 현재 열을 제외한 이전 행의 최대값과 현재 열의 값을 계속해서 더해가며 갱신하면 될듯

회고
- 로직은 같은데 1차원 배열로만 해결하려다가 사고가 멈춰버린듯함 ㅠㅠ
    - DP테이블은 2차원 배열도 가능하다는거 꼭 인지하기

"""

def solution(land):
    N = len(land)
    
    dp = [[0] * 4 for _ in range(N)] # DP 테이블
    dp[0] = land[0]
    
    for i in range(1, N):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][:j] + dp[i-1][j+1:]) # 이전 행에서 같은 열을 제외한 나머지 열 중에서 최대 점수 더함
    
    return max(dp[-1]) # 최대 점수 반환