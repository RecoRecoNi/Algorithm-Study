"""

풀이시간
- 약 30분

접근법
- 입력으로 주어지는 수의 길이 <= 50 -> 구현에 집중
- 값을 최소로 만들어야 한다 -> - 뒤의 값을 괄호를 통해 최대한 크게 만들어야 함 -> 그리디

회고
- 처음에는 str, int 가 섞인 상태로 진행했는데 같은 자료형(정수)로 한꺼번에 변환하는 방법이 훨씬 효율적인 것 같음
- 정수로 반환하는 과정에서 최대한 내장함수를 쓰려다가 조금 버벅거림 ...
    - 풀고나서 드는 생각이 한꺼번에 정수로 변환해놓고 시작하지말고 반복문으로 변환해가면서 연산하는 방법이 조금 더 빠르긴 할 것 같다

"""

import sys

inputs = sys.stdin.readline

example = inputs().rstrip()
arr = []
temp_num = ""
for item in example: # 문자열을 정수로 변환하여 리스트화 (-> [55, -50, 40])
    if item in ["-", "+"]:
        arr.append(int(temp_num))
        temp_num = item
    else:
        temp_num += item

arr.append(int(temp_num)) # 맨 마지막 숫자 추가
arr.append(0) # 인덱스에러가 나지 않도록 연산에 영향을 주지 않는 0 하나 추가

answer = 0

for i in range(len(arr)-1):
    answer += arr[i]
    if (arr[i] < 0) and (arr[i+1] > 0): # 현재 수가 음수인데 다음 수가 양수이면 괄호처리
        arr[i+1] *= -1

print(answer)