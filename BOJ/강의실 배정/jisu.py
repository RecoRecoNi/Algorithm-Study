"""
풀이 시작 : 2023-09-13 13:44

#### 제한 사항 
- N <= 200,000 이므로, O(NlogN) 알고리즘을 설계해야 한다.

#### 풀이
- 일단 강의 시작 순서대로 주어진다는 조건이 없으므로 정렬 O(NlogN)
- 모든 배치된 강의실 중 가장 빨리 끝나는 강의실보다 현재 진행되어야 하는 강의가 더 빠르면 강의실을 추가해야 함
    - 강의가 끝나는 시간을 담은 heap으로 강의실 배정 리스트를 관리한다.
    - 모든 강의를 순회하며 해당 강의의 시작하는 시간이 가장 빨리 끝나는 강의실(heap의 root)의 끝나는 시간보다 더 빠른지 체크
        - 더 빠르다면 힙에 해당 강의의 끝나는 시간 삽입 : 강의실을 추가한다는 의미
        - 가장 빨리 끝나는 강의실의 강의가 더 빨리 끝난다면 heappop 후, 삽입 : 해당 강의실에 강의를 교체한다는 의미
    - 순회 : O(N), heappush: O(logN) -> O(NlogN)
- 최종적으로 O(2NlogN)으로 풀이 가능

풀이 완료 : 2023-09-13 14:50 (1시간 6분 소요)
"""

import sys
from heapq import heappush, heappop


input = sys.stdin.readline

N = int(input())

classes = sorted(
    list(tuple(map(int, input().rstrip().split())) for _ in range(N))
)  # 시작 시간 기준으로 정렬
assigned = []  # min heap으로 사용

for st, en in classes:
    if not assigned or assigned[0] > st:  # 가장 빨리 끝나는 강의의 끝나는 시간보다 현재 강의 시작이 빠름
        heappush(assigned, en)  # 그럼 강의실 추가해야 됨
    else:  # 아니면
        heappop(assigned)  # 기존 강의 끝내고
        heappush(assigned, en)  # 현재 강의 배정

print(len(assigned))  # 최종 배정한 강의실 개수 반환
