"""
풀이 시작 : 2023-10-08 11:17

#### 제한 사항
- q <= 200,000 이므로, O(NlogN) 이하의 알고리즘을 설계해야 한다.

#### 이전 풀이
- 백트래킹으로 m보다 작은 수 하나, 큰 수 하나를 고르는 경우의 수를 구한다.(시간초과)

#### 풀이
- m을 확정한 상태에서 m보다 작은 하나, m보다 큰 하나를 고르는 경우의 수
- 정렬 후 m의 위치 찾기(binary search)
- [1, 2, 3, 5, 6] 에서 m이 3이면, 3은 fix, 나머지 경우의 수는 [1, 2]에서 하나, [5, 6]에서 하나

풀이 완료 : 2023-10-08 12:20 (소요 시간 : 1시간 3분)
"""
import sys
from typing import List

input = sys.stdin.readline


def binary_search(costs: List[int], target: int) -> int:
    """
    costs 내에서 target의 위치를 찾아 탐색 성공 시 위치를 반환한다.
    탐색 실패 시 -1을 반환한다.
    """
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        if costs[mid] == target:
            return mid
        elif costs[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n, q = map(int, input().rstrip().split())
costs = sorted(list(map(int, input().rstrip().split())))

for _ in range(q):
    idx = binary_search(costs, int(input().rstrip()))

    if idx == -1:  # 탐색 실패 시
        print(0)  # 0 반환
        continue

    print(idx * (n - idx - 1))  # line 13 참고

""" 시간초과 (List.index() 사용)
for _ in range(q):
    try:
        idx = costs.index(int(input().rstrip()))
    except:
        print(0)
        continue

    print(idx * (n-idx-1))
"""
