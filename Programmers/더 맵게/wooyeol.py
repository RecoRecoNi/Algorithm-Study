"""
    더 맵게
    https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

    풀이시간 
    21:06 ~ 21:32(26분)

    문제 조건
    2 <= len(scoville) = L <= 1,000,000
    0 <= K <= 1,000,000,000

    시간 복잡도 : 
    O(L + (L-1) * 2 * logL) = O(1,000,000 + 999,999 * 2 * 1000) = O(2,000,998,000)
    O(LlogL)


    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 힙
    1. 최소힙을 구현하고 O(N)
    2. 힙의 root가 K 이상인지 확인하고 맞다면 섞은 횟수 반환
        3. 음식의 갯수가 2이상이면 스코빌 지수 섞기 연산 진행
            - 스코빌 지수 섞기 연산 => 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        4. 음식이 하나만 있을 경우 불가능하기 때문에 -1 반환
"""
from typing import List

import heapq


def solution(scoville: List, K: int):
    count: int = 0

    # 최소 힙 정렬
    heapq.heapify(scoville)

    while scoville:
        # 가장 작은 값이 K 이상일 경우 return
        if scoville[0] >= K:
            return count

        # 음식이 2개 이상인 경우 힙 연산
        if len(scoville) >= 2:
            heapq.heappush(
                scoville,
                heapq.heappop(scoville) + heapq.heappop(scoville) * 2,  # 스코빌 지수 섞기 연산
            )
        # 음식이 하나만 있는 경우 불가능
        else:
            return -1

        count += 1


case1 = [[1, 2, 3, 9, 10, 12], 7]
case2 = [[2, 3], 7]
case3 = [[1, 2, 3, 9, 10, 12], 100000000]
print(solution(*case1))
print(solution(*case2))
print(solution(*case3))
