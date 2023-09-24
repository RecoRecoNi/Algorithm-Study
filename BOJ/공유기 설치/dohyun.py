"""

풀이시간
- 약 1시간 풀이 후 실패로 답지 참조

접근법
- N이 20만 -> O(NlogN) 수준에서 해결
    - 완전탐색은 절대 불가
    - 가능한 좌표는 최대 10억? -> DP 각?
        - 상위의 문제가 하위의 문제를 포함하냐? -> ㄴㄴ 새로운 문제가 들어오면 배열이 아예 달라질 수 있음
- 좌표가 정렬되어 들어오는 것이 아니기 때문에 꽤나 복잡 -> 정렬을 하면 편리할 듯함
- 가장 인접한 두 공유기의 거리를 가장 멀리 해야함
    - 각 좌표들이 떨어져있는 거리가 모두 비슷하다면 가장 인접한 공유기들의 거리가 최대일듯함 (젤 좋은건 거리가 다 똑같을 때)
    - 그렇다면 처음과 끝의 공유기들을 고정하고 그 중점을 반환 -> 이 작업을 공유기를 다 설치할 때 까지 반복하면 될 것같다!
    - 이진탐색의 느낌?

- 풀이 실패로 답지 참조
    - 설치 거리를 이진탐색의 target 으로 설정한 후, 공유기의 개수를 기준으로 이진탐색의 범위를 좁혀나갔음 (자세한 내용은 주석참조)

회고
- "설치 거리" 를 이진탐색의 target 으로 잡아야 했었는데, "설치 지점" 을 잡은것이 문제를 복잡하게 만들었던 것 같음
- 이진 탐색의 target 값이 꼭 인덱스가 될 필요가 없고 다양할 수 있음을 인지하기
    - 이진 탐색의 목적(?)을 더 깊이 이해하고 풀이 시작하기

"""

import sys

def install_wifi(N, C, houses):
    houses.sort()  # 이진 탐색을 위해 좌표를 정렬
    start = 1  # 최소 거리
    end = houses[-1] - houses[0]  # 최대 거리
    result = 0

    while start <= end:
        mid = (start + end) // 2  # 중간 거리 설정
        count = 1  # 공유기 설치 개수 초기화
        prev_house = houses[0] # 처음 집과 비교 시작

        for house in houses:
            if house - prev_house >= mid: # 두 공유기 사이의 거리가 중간 거리보다 크면 설치해보기
                count += 1 # 공유기 설치
                prev_house = house

        if count >= C:  # 공유기 설치 개수가 C 이상인 경우 -> 두 공유기 사이의 거리를 더 넓게 설정할 수 있다는 뜻
            result = mid  # 최대 거리 후보군을 업데이트 (이 값이 최대 간격인지는 확실하지 않으므로)
            start = mid + 1  # 거리를 늘려서 설치 개수를 줄여야 함
        else:
            end = mid - 1  # 공유기 설치 개수가 C 미만인 경우, 거리를 줄여 더 많은 공유기를 설치해야 함

    return result

# 입력 받기
inputs = sys.stdin.readline
N, C = map(int, inputs().split())
houses = []
for _ in range(N):
    houses.append(int(inputs()))

# 결과 출력
print(install_wifi(N, C, houses))
