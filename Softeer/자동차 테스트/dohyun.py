"""

풀이시간
- 10분

접근법
- n 5만 이하 -> 대충 O(NlogN)
- 3대의 자동차를 고르는것이 고정
    - 중앙값이 존재하지 않으면 0
    - 존재하면 경우의 수는 (중앙값보다 작은 값의 수) x (중앙값보다 큰 값의 수)
- 즉 해당 값이 존재하는지 탐색하고, 존재한다면 인덱스를 잘 활용하면 됨 -> 이진탐색

회고
- 3개의 값을 선택, 중앙값이라는 힌트로 이진탐색을 쉽게 눈치챌 수 있었음

"""

import sys

inputs = sys.stdin.readline

n, q = map(int, inputs().split())
yeonbi = [int(x) for x in inputs().split()]
m_i = [int(inputs()) for _ in range(q)]

yeonbi.sort()

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end)//2
        if yeonbi[mid] == target:
            return mid
        elif yeonbi[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

for m in m_i:
    result = binary_search(m, 0, len(yeonbi)-1) # 이진탐색으로 인덱스 값 반환
    
    if result == -1 or result == 0 or result == len(yeonbi)-1: # 값이 없거나 작은수, 큰수가 없을 떄
        print(0)
    else:
        print((len(yeonbi)-result-1) * (result)) # 작은 수 * 큰 수
