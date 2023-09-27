"""
풀이 시작 : 2023-09-27 10:28

#### 제한 사항
N <= 100,000 이므로 O(NlogN) 이하의 알고리즘을 설계해야 한다.

#### 풀이
- 투 포인터로 접근 (`low, high = 0, 0`)
- high 인덱스의 값이 현재 sub_set 집합에 없으면 
    - sub_set 집합에 high 인덱스의 값을 add
    - 이후 high를 넓혀서 탐색
    - 경우의 수 1 증가
- 집합에 이미 있는 경우 같은 수가 하나의 경우에 여러번 나타난 것
    - sub_set을 초기화 하고 low, high를 low+1로 초기화

풀이 중단 : 2023-09-27 11:00 (32분 경과)

#### 풀이 재개 : 2023-09-27 14:30
- 시간 초과, 메모리 초과 -> 

"""

import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().rstrip().split()))

answer = 0
sub_set = set()

low, high = 0, 0

while low < N:
    if high < N and S[high] not in sub_set:
        sub_set.add(S[high])
        answer += 1
        high += 1
    else:
        low += 1
        high = low
        sub_set.clear()

print(answer)
