"""
풀이 시작 : 2023-09-05 13:10

#### 제한 조건
- scovile의 길이 <= 1,000,000 이므로 O(NlogN) 이하의 알고리즘을 설계해야 함.

#### 풀이
- 계속 스코빌 지수가 가장 낮은 2개를 알아야 하므로 항상 오름차순으로 정렬 되어있어야 한다.
- min heap을 활용해서 root(min)원소가 K보다 작으면 다음 원소를 pop해서 섞기
- heap의 원소가 하나밖에 없는데 해당 원소가 K보다 작은 경우 -1 반환
- min heap으로 변환(O(N)) + 모든 경우 순회할 경우 O(N) * heappush O(logN) => O(NlogN) 설계 가능

풀이 완료 : 2023-09-05 13:20(10분 소요)
"""

from typing import List
from heapq import heappush, heappop, heapify


def solution(scoville: List[int], K: int) -> int:
    """
    모든 요리의 스코빌 지수가 k를 넘을 때까지 최소 몇 번 섞어야 하는지를 반환한다.
    모두 k를 넘길 수 없을 경우 -1을 반환한다.
    """
    heapify(scoville)  # 기존 리스트를 min heap으로 변환
    cnt = 0
    while scoville[0] < K:  # root(min)가 K를 넘을 때까지 반복
        if len(scoville) < 2:  # root가 K보다 작은데 섞을 다음 요리가 없는 경우
            return -1

        one, two = heappop(scoville), heappop(scoville)  # 가장 안 매운 두 개 뽑아서
        heappush(scoville, one + two * 2)  # 섞기
        cnt += 1
    return cnt


def main() -> None:
    case1 = [[1, 2, 3, 9, 10, 12], 7]

    print(solution(*case1))  # 2


main()
