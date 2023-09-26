"""
풀이시간: 30분

<input>
n : 수열의 길이 (1 ≤ N ≤ 100,000)
s : 수열 (1 ≤ 원소 ≤ 100,000)

<solution>
투포인터를 통해 연속된 부분 수열을 만들 수 있다.
수를 하나씩 확인하며 딕셔너리에 해당 숫자가 마지막으로 나온 인덱스를 보관해 중복되지 않은 부분 수열을 만든다.
예를 들어, [1, 2, 3, 2, 1]이라는 수열이 있을 때
각 수를 탐색하며 아직 나오지 않은 수라면 딕셔너리에 해당 수의 인덱스를 추가해준다.
이전에 등장한 적이 있고, 딕셔너리에 저장된 인덱스값이 left 보다 크다면 left 인덱스를 1 증가시켜서 이전에 등장한 수의 인덱스보다 한 칸 오른쪽으로 이동한다.
    left = 0, right = 0 -> {1: 0}, ans = 1
    left = 0, right = 1 -> {1: 0, 2: 1}, ans = 1 + 2
    left = 0, right = 2 -> {1: 0, 2: 1, 3: 2}, ans = 1 + 2 + 3
    left = 2, right = 3 -> {1: 0, 2: 3, 3: 2}, ans = 1 + 2 + 3 + 2
    left = 2, right = 4 -> {1: 4, 2: 3, 3: 2}, ans = 1 + 2 + 3 + 2 + 3

<시간복잡도>
O(n)
"""

import sys
input = sys.stdin.readline


n = int(input())
s = list(map(int, input().split()))

# 숫자의 등장 여부 및 인덱스를 저장하기 위한 딕셔너리
appeared = {}
left = 0  # 왼쪽 포인터(수열의 시작 인덱스)
result = 0

for right in range(n):
    cur_num = s[right]
    # 현재 숫자가 등장한 적이 있고, 앞서 나온 위치가 왼쪽 포인터보다 크거나 같은 경우
    if cur_num in appeared and appeared[cur_num] >= left:
        left = appeared[cur_num] + 1 # 이전에 등장했던 같은 수의 인덱스보다 한 칸 오른쪽으로 이동
    appeared[cur_num] = right # 딕셔너리에서 인덱스 갱신
    # 현재 부분 수열의 길이를 계산하여 결과에 더함
    result += (right - left + 1)

print(result)