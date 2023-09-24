"""

풀이시간
- 약 30분

접근법
- N이 1만이하 -> O(NlogN) 쯤의 복잡도로 해결해야함
- 특정 값과 비교해서 조건을 오바하면 줄이기, 조건보다 부족하면 늘리기 + O(NlogN)? -> 이진탐색

회고
- 순간 헷갈려서 시작점을 예산요청의 최소값으로 설정하니 특정 케이스(47%)에서 에러가 계속 발생했음
    - 1로 설정하여 해결 -> 이것때메 버벅이느라 시간 낭비 ㅠㅠ

"""

import sys

inputs = sys.stdin.readline

N = int(inputs())
demands = list(map(int, inputs().split()))
M = int(inputs())

demands.sort() # 이진탐색을 위한 정렬
start, end = 1, demands[-1] # 최소 예산부터 최대 예산까지 탐색점 설정

answer = end

while start <= end: # 다 찾을 때까지 반복
    mid = (start + end) // 2
    temp_sum = 0

    for demand in demands:
        if demand >= mid: # 상한액보다 크다면 상한액으로 치환
            demand = mid
        temp_sum += demand

    if temp_sum > M: # 합이 예산보다 크다면 상환액을 조금 더 줄여야 함
        end = mid - 1

    else: # 그렇지 않다면 조건 만족
        answer = mid # 하지만 최대라는 보장은 없으므로 값만 업데이트하고 계속 진행
        start = mid + 1 # 더 크게 상한액을 설정할 수 있는지를 확인하기 위해 시작점을 늘려봄

print(answer)