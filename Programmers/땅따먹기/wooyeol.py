"""
    땅따먹기
    https://school.programmers.co.kr/learn/courses/30/lessons/12913

    풀이시간 
    19:09 ~ 19:18 / 19:40 ~ 20:20 (49분)
    
    문제 조건
    행의 개수(N) : 100,000 이하의 자연수
    열의 개수 : 4개
    점수 : 최대 100이하의 자연수

    시간 복잡도 : 
    O(N * (4 * 3 * 3) + 4) = O(N)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> DP

    - 현재 행의 자기 열의 값에 이전 행의 자신의 열을 제외한 나머지 열들의 최대 값을 현재 열에 더해주기

    dp 테이블은 현재 행의 자신의 열중 최댓값을 기록
"""
def solution(land):
    for row_idx in range(1, len(land)):
        land[row_idx][0] += max(land[row_idx - 1][1:])
        land[row_idx][1] += max(land[row_idx - 1][:1] + land[row_idx-1][2:])
        land[row_idx][2] += max(land[row_idx - 1][:2] + land[row_idx-1][3:])
        land[row_idx][3] += max(land[row_idx - 1][:3])
    
    return max(land[-1])

case1 = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(case1)) #16

case2 = [[1, 1, 3, 1], [2, 3, 2, 2], [1, 4, 1, 1]]
print(solution(case2)) #9