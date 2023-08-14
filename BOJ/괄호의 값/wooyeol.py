"""
    괄호의 값
    https://www.acmicpc.net/problem/2504
    
    풀이시간
    21:24

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? 스택
    
    조건 1: ‘()’ 인 괄호열의 값은 2이다.
    조건 2: ‘[]’ 인 괄호열의 값은 3이다.
    조건 3: ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
    조건 4: ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
    조건 5: 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

    접근 1 : 괄호를 검사하여 사칙연산의 표현식으로 변환을 진행하고 해당 표현식을 적절한 타이밍에 연산을 진행하여 정답을 도출

    접근 2 : 연산식에 분배법칙을 적용하여 전개하였을 때 하나의 항들을 우선적으로 계산하는 방식으로 괄호 표현식을 풀이
        - 여는 괄호 종류에 따라 res 항에 2,3을 곱해주어 분배법칙이 적용된 값을 계산합니다. 
        - 괄호가 닫힐 경우 한 쌍의 연속된 경우였는지 확인 후 맞다면 분배법칙이 적용된 값을 answer 항에 더해주고 아니라면 res에 다시 해당 2,3 값을 나눠줍니다.

        - 분배법칙 예시) (2+3x3)x2 + 2x3 = 2x2 + 2x3x3 + 2x3
            1. 2x2
            2. 2x3x3 (2를 한 번 나눠주고 3을 두번 더 곱해줌)
            3. 2x3 (3을 한 번 나눠줌)
"""
import sys

input = sys.stdin.readline

def solution_fail(parentheses_expression: str):
    bucket: list = list()
    answer: int = 0
    sub_expression: str = ""
    last_parentheses: str = " "

    # 예외처리 : 만약 시작하는 괄호 표현식이 닫는 괄호이면 0 반환
    if parentheses_expression[0] in (")","]"):
        return 0

    # 괄호 표현식의 괄호를 하나씩 검사하며 풀이
    for parentheses in parentheses_expression:
        
        # 만약 버킷이 비어있다면 (첫번째 iter or 하나의 항에 대한 연산 종료)
        if not bucket:
            # sub_expression도 비어있지 않다면 하나의 전체 계산된 항이다.
            if sub_expression:
                # 지금까지 기록된 sub_expression 연산 진행 후 sub_expression 초기화
                answer += eval(sub_expression)
                sub_expression = ""

        # 여는 괄호의 경우 bucket에 담기
        if parentheses == "(" or parentheses == "[":
            bucket.append(parentheses)

            # 조건 5 : 여는 괄호 직전 닫는 괄호가 존재한다면 + 연산
            if last_parentheses in (")","]"):
                sub_expression += "+"

        # 닫는 괄호의 경우 버켓의 상단을 검사하고 올바른 경우 pop()
        elif parentheses == ")" and bucket and bucket[-1] == "(":
            bucket.pop()

            # 조건 1: 직전 괄호가 같은 종류의 여는 괄호일 경우 2를 sub_expression에 삽입
            if last_parentheses == "(":
                sub_expression += "2"

            # 조건 3: 직전 괄호가 다른 종류일 경우 *2를 sub_expression에 삽입 후 연산 진행
            else:
                # 버켓이 비어있다면 사칙연산의 괄호가 닫힌 것으로 우선순위를 주어 먼저 계산을 진행
                if not bucket:
                    sub_expression = str(eval(sub_expression))
                sub_expression += "*2"
                sub_expression = str(eval(sub_expression))


        # 닫는 괄호의 경우 버켓의 상단을 검사하고 올바른 경우 pop()
        elif parentheses == "]" and bucket and bucket[-1] == "[":
            bucket.pop()
            # 조건 2: 직전 괄호가 같은 종류의 여는 괄호일 경우 3를 sub_expression에 삽입
            if last_parentheses == "[":
                sub_expression += "3"

            # 조건 4: 직전 괄호가 다른 종류일 경우 *3를 sub_expression에 삽입 후 연산 진행
            else:
                # 버켓이 비어있다면 사칙연산의 괄호가 닫힌 것으로 우선순위를 주어 먼저 계산을 진행
                if not bucket:
                    sub_expression = str(eval(sub_expression))
                sub_expression += "*3"
                sub_expression = str(eval(sub_expression))

        # 예외처리 : 닫는 괄호이지만 버켓의 상단과 다른 종류일 경우 혹은 주어진 괄호 이외의 기호가 주어졌을 때
        else:
            return 0
        
        # 직전 괄호를 기억하기 위한 대입 연산
        last_parentheses = parentheses

    if bucket:
        return 0

    return eval(sub_expression) + answer

def solution(parentheses_expression: str):
    # 괄호 검사를 위한 스택 자료구조
    bucket: list = list()

    # 더하기 전까지 곱해지는 값을 저장하는 임시 변수
    res: int = 1
    
    # 정답 변수
    answer: int = 0

    # 직전 괄호 저장
    last_parenthesis = None

    for parenthesis in parentheses_expression:
        
        # 여는 괄호는 버킷에 추가
        if parenthesis in ("(","["):
            bucket.append(parenthesis)
            
            # 여는 괄호 종류에 따라 2 or 3 값을 곱해주기
            if parenthesis == "(":
                res *= 2
            else:
                res *= 3
        
        # 닫는 괄호 종류를 검사하고 유효하다면 괄호 제거
        elif parenthesis == ")" and bucket and bucket[-1] == "(":
            bucket.pop()
            
            # 한 쌍의 괄호라면 계산된 res 값을 더해주기
            if last_parenthesis == "(":
                answer += res
            
            # 괄호가 제거되었다면 res는 다시 2로 나눠주기
            res //= 2

        # 닫는 괄호 종류를 검사하고 유효하다면 괄호 제거
        elif parenthesis == "]" and bucket and bucket[-1] == "[":
            bucket.pop()

            # 한 쌍의 괄호라면 계산된 res 값을 더해주기
            if last_parenthesis == "[":
                answer += res

            # 괄호가 제거되었다면 res는 다시 3으로 나눠주기
            res //= 3

        # 예외처리 : 닫는 괄호이지만 버켓의 상단과 다른 종류일 경우 혹은 주어진 괄호 이외의 기호가 주어졌을 때
        else:
            return 0
        
        # 직전 괄호 값 업데이트
        last_parenthesis = parenthesis

        # print(parenthesis, bucket)
        # print(answer, res)
        # print()

    if bucket:
        return 0

    return answer

def main():
    print(solution(input().rstrip()))
    # print(solution("[([[]](()))]")) # 78
    # print(solution("([[]]())")) # 22

    # print(solution("[[()][]]")) # 27
    # print(solution("((())[])")) # 14

    # print(solution("()[[]]")) # 11
    # print(solution("([])")) # 6
    # print(solution("()[]()")) # 7
    # print(solution("(()[[]])([])")) # 28
    # print(solution("[][]((])")) # 0
    # print(solution(")()(")) # 0
    # print(solution("[[[[[]]]]]")) # 243
    # print(solution("(((()))))")) # 0
    # print(solution("(")) # 0
    # print(solution(")")) # 0
    # print(solution(")()")) # 0
    # print(solution("(8)")) # 0
    # print(solution("()()()()()()()()()()()()()()()")) # 30
    # print(solution("[][][][][][][][][][][][][][][]")) # 45
    # print(solution("[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]")) #14348907

main()
