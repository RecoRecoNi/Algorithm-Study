"""
    스택 수열
    https://www.acmicpc.net/problem/1874
    
    문제 해석
    1. 잘못한 해석
    스택을 사용하여 오름차순의 수열을 만들 수 있는가?
    요소는 1~N까지의 정수

    2. 1~N의 값이 순서대로 주어졌을 때 스택을 사용하여 주어진 수열을 구할 수 있는가?
    - 현재 순서의 값이 입력값보다 작거나 같아질 때까지 'Push' 연산
    - 이후 stack의 마지막 값이 입력값과 같아지면 'Pop' 연산
        - 다음번 num을 입력받았으나 num 값이 target 보다 클 경우 수열 생성이 불가능 하기 때문에 'NO' 출력


    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 스택을 사용한 구현
    
    고찰
    'NO'를 'No'로 써놓고 30분동안 디버깅을 하였다. 피곤할 때는 자는게 좋을 것 같다.
"""
############## 2번 풀이 ##############

import sys

global FLAG

N = int(input())

stack = []
operations = []
target = 1
FLAG = True

for _ in range(N):
    num = int(input())

    # 현재 순서의 값이 입력값보다 작거나 같아질 때까지 반복
    while target <= num:
        # 'Push' 연산
        stack.append(target)
        target += 1
        operations.append("+")

    # stack의 마지막 값이 입력값과 같다면
    if stack[-1] == num:
        # 'Pop'
        operations.append("-")
        stack.pop()
    # stack의 마지막 값이 입력값보다 클 경우는 해당 수열을 만들 수 없는 상황이다.
    else:
        print("NO")
        FLAG = False
        break

# 결과 출력
if FLAG:
    for oper in operations:
        print(oper)


############## 1번 잘못된 풀이 ##############

# import sys

# input = sys.stdin.readline

# N = int(input())

# stack = []
# operations = []

# target = N

# for i in range(N):
#     num = int(input())

#     if num == target:
#         # 입력받은 문자가 현재 출력돠어야 하는 target일 경우 push(),pop() 연산
#         operations.append("+")
#         operations.append("-")

#         # 다음 target 설정 # 후 검사를 위한 num 값 업데이트
#         target -= 1

#         # target의 값이 바뀌었기 때문에 target에 조건이 부합한지 확인
#         while stack and stack[-1] == target:
#             val = stack.pop()
#             operations.append("-")
#             target -= 1
#     else:
#         stack.append(num)
#         operations.append("+")
#     print(f"{i} {num} : {operations}")

# print(*operations)

# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

# + + + + - + - - + - + +
