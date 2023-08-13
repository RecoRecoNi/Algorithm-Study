"""
    쇠막대기
    https://www.acmicpc.net/problem/10799
    
    풀이시간
    20:37 ~ 21:17(40분)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? 스택

    괄호 표현식을 상대할 때는 닫힘 연산이 나오기 까지 현재 괄호를 bucket에 담아 두었다가 꺼내는 Stack을 자주 사용해왔습니다.
    그래서 이번 문제도 동일하게 괄호 표현식의 괄호를 검사하며 풀이를 하기 위해 bucket(stack 자료구조)을 사용하여 풀이하였습니다.
    하지만 이번에는 한 쌍의 "()" 괄호인지 "(", ")" 인지에 따라서 연산이 달라져야했기에
    직전의 기호를 기억하는 state 라는 bool 변수를 사용하여 기록하는 방식을 통해서 구현 할 수 있었습니다.
    
    이후 닫힘 괄호를 맞이하였을 때 state를 확인하여 현재 bucket에 담긴 쇠 막대기의 수를 더하거나 절단되고 남은 하나의 쇠 막대기를 더해주거나 둘 중에 하나의 연산을 해주었습니다.
"""

import sys

input = sys.stdin.readline

def solution(parentheses_expression: str):
    bucket: list = []
    answer: int = 0

    # 연속된 값이었는지 확인하기 위한 State 변수
    # 만약 직전에 여는 괄호여서 True였는데 닫는 괄호일 경우는 레이저 연산
    # 하지만 직전에 닫힌 괄호여서 False였다면 이는 한 쇠 막대기가 다 잘린 것이기 때문에 마지막 꼬투리 부분을 하나 더 더해주기
    state: bool = True
    
    # 괄호를 하나씩 검사하며 
    for parentheses in parentheses_expression:
        # 여는 괄호일 경우 bucket에 추가
        if parentheses == "(":
            bucket.append(parentheses)

            # 현재 bucket에는 여는 괄호가 추가 된 사실을 기록
            state = True
        else: 
            bucket.pop()
            # 직전에 여는 괄호여서 True였다면 bucket 내의 괄호 갯수 만큼 덧셈
            if state:
                answer += len(bucket)

            # 직전에 닫는 괄호여서 False였다면 하나의 쇠 막대기 절단이 완료된 것 임으로 마지막 조각 하나를 더해줌
            else:
                answer += 1

            # 현재 연산은 여는 괄호를 삭제하는 연산이었다는 사실을 기록
            state = False
    return answer

def main():
    # 괄호 표혁식 입력 받기
    parentheses_expression = input().rstrip()
    print(solution(parentheses_expression))

main()

# parentheses_expression = "()(((())))" # 3

# parentheses_expression = "()(((()())(())()))(())" # 17
# parentheses_expression = "(((()(()()))(())()))(()())" # 24