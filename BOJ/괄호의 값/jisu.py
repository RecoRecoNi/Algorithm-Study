'''
풀이 시작 : 2023.08.13 23:31

- 문자열 길이는 최대 30이므로 O(N^2)이상도 가능할 듯함
- 열린 괄호('(', '[']))가 나오면 반환 값에 (2, 3) 을 곱해서 다시 재귀를 반복하는 방식으로 구현하면 될 듯 함

풀이 정지 : 2023.08.14 01:00
풀이 재개 : 2023.08.14 10:40
- 풀이 변경 : 재귀 없이 순회로, 괄호가 열렸을 때 값을 저장해서 풀이
    - 닫힌괄호는 직전이 동일 열린괄호가 아닌 이상 배율을 적용하는 역할을 함 
    - 열린 괄호가 중첩해서 나오면 배율 적용
    - 닫힌 괄호가 나오면 
        - 이전 braket이 올바른 열린 괄호이면 현자깨지 배율을 값에 더해줌 (곱의 법칙 활용)
        - 배율 조정
    - 올바른 괄호열인지 판단이 필요하므로, 스택을 활용해서 매번 올바른 괄호열인지 판단 후 예외처리
- 풀이 완료 : 2023.08.14 11:40 (풀이시간 : 2시간 30분)

'''

import sys
from typing import List, Dict

input = sys.stdin.readline

def solution():
    brakets: str = input().rstrip()                 
    score: Dict[str:int] = {'(' : 2, '[' : 3}       # 각 braket에 따른 배율 정의
    mul = 1                                         # default 배율
    stack: List[str] = list()                       # 예외 처리를 위한 스택
    answer: int = 0                                 # 정답을 담을 변수

    for i in range(len(brakets)):
        if brakets[i] in {'(', '['}:                # 열린 괄호의 경우
            mul *= score[brakets[i]]                    # 중첩해서 배율 적용
            stack.append(brakets[i])                    # 스택에 append
        else:   # brakets[i] in {')', ']'}          # 예외 처리
            if not stack or (brakets[i]==')' and stack[-1] == '[') or (brakets[i] == ']' and stack[-1] == '('):
                print(0)
                exit()
            else:                                   # 닫힌 괄호가 나왔을 때 올바른 괄호열인 경우
                if brakets[i] == ')':               
                    if brakets[i-1] == '(':         # 직전 괄호가 동일한 쌍의 열린 괄호인 경우에만
                        answer += mul                   # 지금까지의 배율을 더해주고 
                    mul //= 2                           # 배율 조정
                elif brakets[i] == ']':
                    if brakets[i-1] == '[':
                        answer += mul
                    mul //= 3
                stack.pop()                         # stack에서 동일한 쌍의 열린 괄호를 pop

    print(answer) if not stack else print(0)        # 괄호열 순회 후 stack에 값이 남아있으면 올바른 괄호열이 아님


solution()