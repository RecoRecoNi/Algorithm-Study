"""
풀이 시작 : 2023-09-24 14:02

#### 제한 사항

- 3 <= N <= 10,000, 각 수는 1이상 100,000 이하이다.
    - 지방의 수와 예산을 계산하는 부분에 대한 알고리즘을 O(NlogN)으로 설계해야 한다.

#### 풀이
- 예산의 상한을 maximum으로 하고, 배정 가능한 최대 maximum을 구하면 된다.
- 상한으로 가능한 범위는 low, high = 0, max(requests)
- 이분 탐색으로 upperbound(예산을 배정 가능한 최대 maximum)를 구하면 된다.
- upperbound를 구했으면 이를 적용해서 배정한 최대 예산을 출력한다.

#### 시간 복잡도
- maximum 탐색(이분탐색) + 예산 배정 가능 여부 = O(logN) * O(N) = O(NlogN)

풀이 완료 : 2023-09-24 14:12 (풀이 시간 : 10분 소요)


메모리 | 32276KB
-- | --
시간 | 72ms
"""

import sys

input = sys.stdin.readline


def can_assign(maximum: int) -> bool:
    """
    예산의 상한을 maximum으로 했을 때 전체 예산을 배정 가능한지 여부를 반환한다.
    """
    total = 0
    for request in requests:
        total += min(maximum, request)

    return total <= M


N = int(input())
requests = list(map(int, input().rstrip().split()))
M = int(input())

low, high = 0, max(requests)

while low <= high:
    mid = (low + high) // 2

    if can_assign(mid):  # 예산을 배정 가능하면
        low = mid + 1  # 상한을 높혀서 탐색
    else:  # 배정 불가능 하면
        high = mid - 1  # 상한을 낮춰서 탐색

print(high)  # 예산의 상한이 문제의 해
