"""
    공유기 설치
    https://www.acmicpc.net/problem/2110

    풀이시간 
    00 : 25 ~ 01 : 20 (55분)
    
    문제 조건
    2 <= N <= 200,000
    2 <= C <= N
    0 <= x <= 1,000,000,000

    시간 복잡도 : 
    O(NlogN + logx * N)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 이진 탐색

    절대 이진 탐색을 떠올릴 수 없는 문제 설명이지만 과거 풀었던 기억을 통해서 문제를 풀이하였습니다.
    (일단 문제 설명이 너무 이상합니다. 가장 인접한 두 공유기 사이의 거리를 최대로... 화가 납니다. 내 자소서가 나을듯)

    1,000,000,000(10억)이 탐색해야할 영역이기 때문에 logN으로 풀이를 해야하고 이진 탐색을 사용하여 최단 거리를 찾아낼 수 있습니다.
"""
import sys

input = sys.stdin.readline

# 거리 이진탐색
def binary_search(start, end, houses):
    minmum_max_distance = 0

    while start <= end: 
        mid = (end + start) // 2

        prev_house = houses[0]
        count = 1

        # 설정된 mid 값이라면 몇 개의 공유기를 설치 할 수 있는지 확인
        for i in range(1, N):
            if houses[i] - prev_house >= mid:
                count += 1
                prev_house = houses[i]

        # 만약 설치된 공유기의 갯수가 C 보다 적다면
        if count < C:
            # 간격 감소시키기
            end = mid - 1
        # 만약 설치된 공유기의 갯수가 C 보다 크다면
        elif count >= C:
            # 간격 증가시키기
            start = mid + 1
            minmum_max_distance = mid
            
    return minmum_max_distance


N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]

houses.sort()

print(binary_search(0, houses[-1] - houses[0], houses))