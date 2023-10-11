"""
    등굣길
    https://school.programmers.co.kr/learn/courses/30/lessons/42898

    풀이시간 
    22:59 ~ 23:59 (풀이참조)
    https://dev-note-97.tistory.com/141

    문제 조건
    1 <= N,M <= 100
    0 <= len(puddles) <= 10

    시간 복잡도 :
    O(100 * 100)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> DP

    처음에는 BFS/DFS로 접근하며 최단 거리를 가지는 경우를 DP 테이블로 만들려고 시도하였습니다.
    하지만 BFS/DFS 경로 탐색은 최단 거리 탐색을 위한 알고리즘이라 해당 경로로 몇개의 선이 지나갔는지 표현 할 수 없었습니다.
    결국 한 시간은 넘겨 풀이를 참고하고 다시 풀이를 진행하였습니다.

    DP 테이블을 만들기 위해서 DP 테이블의 각 원소가 의미하는 바를 현재 칸을 지나는 경로의 개수로 정의하고 점화식을 세웠습니다.
    
    점화식 : dp[y][x] = dp[y-1][x] + dp[y][x-1] (왼쪽 + 오른쪽 경로를 지나는 개수)

    이렇게 했을 때 범위를 벗어나는 경우에 대한 고려를 해보았지만 row를 기준으로 왼쪽 상단부터 값을 업데이트 하기 때문에 범위를 넘어가는
    경우에는 해당 범위의 값이 0으로 초기화되어있습니다.
"""
def solution(m, n, puddles):
    # Table 생성 
    dp = [[0] * (m+1) for _ in range(n+1)]

    # puddles 좌표 집합으로 자료형 변환
    puddles = set(map(tuple, puddles))

    # start point
    dp[1][1] = 1

    # 모든 테이블에 대해서
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            # 초기값 skip
            if x == 1 and y == 1: 
                continue
            
            # puddle 값이 아닌 경우 점화식 유도
            if (x, y) not in puddles:
                # 점화식 : dp[y][x] = dp[y-1][x] + dp[y][x-1] (왼쪽 + 오른쪽 경로를 지나는 개수)
                dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % (10**9 + 7)

    return dp[-1][-1] 

case1 = (4, 3, [[2, 2]])
print(solution(*case1)) # 4