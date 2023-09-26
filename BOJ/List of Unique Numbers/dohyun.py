"""

풀이시간
- 약 1시간

접근법
- N 십만 이하 -> O(NlogN)
- 연속된 수의 개수를 1개, 2개, ... , N 개 뽑기, 최소값은 연속한 1개의 수를 뽑았을 때 -> N
    - 이를 투포인터로 구현 가능
- 집합 자료형을 통해 고유값만을 갖는 수열을 구해놓고, 해당 수열의 길이만큼 빼주면 됨
    - ex: [1,2,3,4,5]
    - cnt += end - start (5-0 = 5)
    - tmp_set = [1,2,3,4,5] -> [1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] (cnt 개수 = 경우의 수)
    - 이후에 start 포인트를 제거 -> tmp_set = [2,3,4,5]
    - cnt += end - start (5-1 = 4)
    - tmp_set = [2,3,4,5] -> [2], [2,3], [2,3,4], [2,3,4,5]
    - ...
    - cnt += end - start (5-4 = 1)
    - tmp_set = [5] -> [5]
    - start 포인트 제거 -> tmp_set = []
    - cnt += end - start (5-5 = 0)
    - 종료

회고
- 좀 더 많이 푸는 연습을 해서 버벅거리는 시간 줄이기

"""

import sys

inputs = sys.stdin.readline

N = int(inputs().rstrip())
arr = list(map(int, inputs().split()))

cnt, end = 0, 0
tmp_set = set()

for start in range(N):    
    while (end < N) and (arr[end] not in tmp_set): # end 인덱스가 범위 내이고, arr[end] 값이 unique 값일 때
        tmp_set.add(arr[end])
        end += 1

    cnt += end - start # end 와 start 의 차이만큼이 고유값을 갖는 리스트의 개수
    tmp_set.discard(arr[start])

print(cnt)