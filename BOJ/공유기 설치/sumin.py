"""
풀이시간: 25분

<input>
n: 집의 개수(2 ≤ N ≤ 200,000)
c: 공유기의 개수(2 ≤ C ≤ N)
집의 좌표 xi (0 ≤ xi ≤ 1,000,000,000)가 주어짐

<solution>
1. 가장 인접한 두 공유기 사이의 거리를 이분탐색한다.
2. 가장 인접한 집 간의 거리를 유지하면서 최대한 많은 공유기를 설치했을 때, C개 이상 설치할 수 있으면 정답의 후보가 된다.
- 가능한 경우면, 거리를 더 크게 -> 더 적은 공유기 설치 가능
- 불가능한 경우면, 거리를 더 작게 -> 더 많은 공유기 설치 가능

<시간복잡도>
O(nlogn)
"""
import sys
input = sys.stdin.readline

# 집, 공유기의 개수
n, c = map(int, input().split())
# 집 좌표
homes = [int(input()) for _ in range(n)]
homes.sort() # 가장 인접한 집을 확인하기 위해 정렬


def possible(diff: int) -> bool:
    """
    diff: 가장 인접한 두 공유기 사이의 거리
    """
    cnt = 1 # 첫 번째 집부터 설치
    last = homes[0]
    for home in homes: # 인접한 집들 확인
        if home - last >= diff: # 가장 인접한 두 공유기 사이의 거리가 diff 이상이면
            cnt += 1 # 공유기 설치 개수 업데이트
            last = home # 현재 집 좌표로 갱신
    return cnt >= c # 최대한 많은 공유기를 설치했을 때의 개수가 c개 이상이라면 true

ans = 1
left = 1
right = homes[-1] - homes[0] # 가능한 가장 먼 거리

while left <= right:
    mid = (left+right) // 2 # 가장 인접한 두 공유기 사이의 거리를 이분탐색
    if possible(mid): # c개의 공유기가 설치 가능하다면 ans 값 업데이트
        ans = mid
        left = mid + 1
    else: # 설치가 불가능하면 오른쪽 포인터를 이동시켜 인접한 두 공유기 사이의 거리를 줄이고 다시 탐색
        right = mid - 1
print(ans)