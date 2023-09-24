"""
풀이 시작 : 2023-09-24 13:14

#### 제한 사항
- x_i <= 1,000,000,000 이므로, 가능한 좌표를 완전 탐색하는 방법으로는 x
- 2 <= N <= 200,000 이므로 집을 순회하며 O(NlogN) 알고리즘을 설계해야 한다.
- 집들의 좌표는 정렬되어 주어지지 않음에 주의

#### 풀이
- 간격을 interval로 설정했을 때 C개의 공유기를 모두 설치할 수 있는지 여부를 판단
- 설정 가능한 간격 중 최소는 1, 최대는 첫 번째 집과 마지막 집의 간격
    - 이분탐색을 위해 `low, high = 1, 첫 번째 집과 마지막 집의 간격` 으로 설정
    - 집의 좌표가 정렬되어 주어지지 않으므로 정렬이 필요하다.
    - mid를 interval로 설정하여 공유기를 설치할 수 있는지 여부를 판단
- 결정 문제 -> 최적화 문제 : 파라메트릭 서치

#### 시간 복잡도
- 정렬 : O(NlogN)
- 이분탐색 + 설치 여부 판단 = O(logN) * O(N) = O(NlogN)

풀이 완료 : 2023-09-24 13:39 (풀이 시간 : 25분 소요)


메모리 | 40548KB
시간 | 272ms
-- | --

"""

import sys

input = sys.stdin.readline


def can_install(interval: int) -> bool:
    """
    설치 시 인접한 공유기의 간격을 interval로 설정했을 때 C개의 공유기를 설치할 수 있을지 여부를 반환한다.
    """
    x = houses[0]
    num_wifi = C - 1
    for house_x in houses[1:]:
        if house_x - x >= interval:  # 마지막으로 설치된 공유기 위치와 다음 공유기 위치의 간격이
            num_wifi -= 1  # interval보다 짧으면 공유기 설치
            x = house_x  # 마지막 공유기 위치 업데이트

        if num_wifi == 0:  # C개의 공유기 설치 성공
            return True

    return False


N, C = map(int, input().rstrip().split())
houses = sorted([int(input().rstrip()) for _ in range(N)])

low, high = 1, houses[-1] - houses[0]

while low <= high:
    mid = (low + high) // 2

    if can_install(mid):  # interval을 mid로 설정했을 때 C개를 설치할 수 있으면
        low = mid + 1  # 간격을 더 넓혀서 탐색해보기
    else:  # 설치하지 못하면
        high = mid - 1  # 간격을 더 좁혀서 탐색해보기

print(high)  # 설치 가능한 최대 간격은 high에 담겨있음
