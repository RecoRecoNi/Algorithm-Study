"""
    k진수에서 소수 개수 구하기
    https://school.programmers.co.kr/learn/courses/30/lessons/92335

    풀이시간 
    24:01 ~ 01:31

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 문자열 내장 함수 / n진수 변환 법

    1. 10진수 to N 진수 변환
    2. 0을 기준으로 split() 진행
    3. split된 데이터를 기준으로 10진수로 변환 후 
        3-1. 소수인지 검사하는 함수

    3. split된 데이터를 기준으로 10진수로 변환 후 을 계속 n진수로 표기된 값을 다시 10진수로 변환해서 
    그 값이 소수인지 판단하는지 검사하는 삽질을 시행하여 문제가 풀리지 않는 문제가 있었다.
"""


def covert_to_notation(n: int, k: int) -> str:
    # 거꾸로 계산된 n 진수
    rev_output: str = ""

    # n진수 변환
    while n > 0:
        n, mod = divmod(n, k)
        rev_output += str(mod)

    # 뒤집기
    return rev_output[::-1]


def is_primary_number(target: int):
    for idx in range(2, int(target**0.5) + 1):
        if target % idx == 0:
            print(idx)
            return False
    return True


def solution(n: int, k: int):
    answer: int = 0

    # 1. 10진수 to N 진수 변환
    notation_output = covert_to_notation(n, k)

    # 2. 0을 기준으로 split() 진행
    for primary_num in notation_output.split("0"):
        if primary_num not in ["", "1"]:
            # print("num :", primary_num)

            # 3. split된 데이터를 기준으로 10진수로 변환 후
            # decimal = convert_to_decimal(primary_num, k)
            decimal = int(primary_num)

            # 3-1. 소수인지 검사하는 함수
            if is_primary_number(decimal):
                # print("Decimal :", decimal)
                answer += 1

    return answer


print(solution(437674, 3))  # 3
print(solution(110011, 10))  # 2
