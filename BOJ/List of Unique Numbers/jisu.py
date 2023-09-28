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

#### 풀이(스터디 이후)
- low번째 인덱스부터 중복 없는 high인덱스까지의 경우의 수는 그 구간의 길이임
    - 예를 들어 1 2 3 1 2 에서 중복 없는 1 2 3 구간에서 1부터 시작하는 경우의 수는 1, 12, 123 => 3가지이므로 구간의 길이
- 따라서 low로 순회하면서, high를 low와 중복되지 않는 인덱스까지 넓히며 탐색을 반복하면 된다.
    - 1 2 3 -> 2 3 1 -> 3 1 2 -> 1 2 -> 2 : 12개의 경우의 수

메모리 | 시간
-- | --
44844KB | 152ms


"""

import sys

input = sys.stdin.readline

N = int(input())
S = input().rstrip().split()

answer = 0
sub_set = set()

low, high = 0, 0

while low < N:
    if high < N and S[high] not in sub_set:  # 중복 발생 전까지 high 넓히기
        sub_set.add(S[high])  # 중복을 고려하기 위함
        high += 1
    else:
        answer += high - low  # 중복 발생 or high 인덱스 초과 시 구간의 길이가 경우의 low부터 시작하는 경우의 수
        if high < N:  # 중복 발생 시
            sub_set.remove(S[low])  # low의 수를 제거해 다음 인덱스 순회
        low += 1

print(answer)
