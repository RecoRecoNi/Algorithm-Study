"""
    예산
    https://www.acmicpc.net/problem/2512

    풀이시간 
    10 : 20 ~ 10 : 32 (12분)

    문제 조건
    3 <= N <= 10,000
    1 <= x <= 100,000

    시간 복잡도 : 
    O(N + logx * N)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 이진 탐색
    
    목표하는 상한액을 찾기 위해서 1 ~ 100,000안의 값을 찾아야 하기 때문에 이진 탐색을 통해서 탐색합니다.
"""
import sys

input = sys.stdin.readline

def binary_search(start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        
        # 정수 상한액을 적용하여 sum 적용한 결과
        temp_sum = sum([x if x <= mid else mid for x in budget])

        # 합이 국가 총 예산보다 크다면 상한액 줄이기
        if temp_sum > target_sum:
            end = mid - 1
        # 국가 총 예산액보다 작거나 같다면 상한액 늘리기
        elif temp_sum <= target_sum:
            start = mid + 1
            answer = mid
        
    return answer

# 지방의 개수
N = int(input())

# 지방의 각 예산
budget = list(map(int, input().split()))

# 요청 받은 지방의 예산 중 최대 값
max_budget = max(budget)

# 국가 총 예산
target_sum = int(input())

# 국가 총 예산이하라면 정수 상한액은 예산 중 최대 값
if target_sum >= sum(budget):
    print(max_budget)
# 아니라면 이진 탐색
else:
    print(binary_search(0, max_budget))