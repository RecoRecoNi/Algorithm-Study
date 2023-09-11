"""
풀이 시작 : 2023-09-11 14:20

#### 제한 조건
- 주어지는 식의 길이는 최대 50

#### 풀이 방법
- 연산자는 '+' 아니면 '-'
- 맨 앞에 -가 오는 경우는 없으므로 여는 괄호는 연산자 뒤, 닫는 괄호는 다음 연산자 앞에 올 수 있음
- 최소 값을 만들기 위해 '-' 다음에 오는 구간을 최대로 만들어줘야 함
    - '-'연산자 뒤에 괄호를 열고 다음 '-'가 나오기 전에 괄호를 닫으면 '-' 구간을 최대로 묶을 수 있음
    - 55-50+40-10+20+30+40 -> 55-(50+40)-(10+20+30+40)

풀이 완료 : 2023-09-11 14:58 (풀이 시간 : 38분)
"""

import sys
from collections import deque

input = sys.stdin.readline

equation = deque(input().rstrip())  # 숫자 문자열 파싱을 위해 큐를 활용(연산자 등장 전까지 popleft())
braket_state = False  # 현재 괄호가 열려있는지 여부
after = ""  # 괄호 추가 후 문자열
tmp = ""  # 유효한 숫자 문자열을 파싱할 임시 변수

while equation:
    while equation and equation[0] not in ["+", "-"]:  # 다음 문자가 연산자일 때까지
        tmp += equation.popleft()  # 문자 파싱
    after += str(int(tmp))  # 유효한 숫자 문자열로 변환 (00009 -> 9)
    tmp = ""

    if not equation:  # 다음 문자가 남아있지 않으면 break
        break

    if equation[0] == "-":  # 다음 문자가 남아있다면 연산자임, '-'인 경우
        if braket_state:  # 괄호가 열린 상태에서
            after += (
                ")" + equation.popleft() + "("
            )  # 닫고 '-' 추가 후 다시 열어줌(연산자가 마지막일 순 없음)
        else:  # 괄호가 닫혀 있는 상태에서는
            after += equation.popleft() + "("  # '-' 추가 후 열어줌
            braket_state = True  # 괄호 열림 표시
    else:  # 다음 연산자가 '+'인 경우
        after += equation.popleft()  # 그냥 추가해주면 됨

if braket_state:  # 위 로직대로라면 한 번 괄호 열렸으면 닫히지 않으므로 해당 과정 추가
    after += ")"

print(eval(after))
