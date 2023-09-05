"""
    n진수 게임
    https://school.programmers.co.kr/learn/courses/30/lessons/17687

    풀이시간 
    22:25 ~ 11:30 (1시간 5분)
    
    문제 조건
    2 ≦ n ≦ 16
    0 < t ≦ 1000
    2 ≦ m ≦ 100
    1 ≦ p ≦ m

    시간 복잡도 : 
    O()

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 구현
"""


def base_num(decimal: int, n: int) -> list:
    """
    10진수의 decimal를 n 진수로 변환해주는 함수

    Args:
        decimal (int): 10진수 타겟 정수
        n (int): 변환할 n진수
    """
    answer: list = []

    if decimal == 0 or decimal == 1:
        answer.append(str(decimal))
        return answer

    while decimal > 0:
        decimal, remain = divmod(decimal, n)
        if remain >= 10:
            remain += ord("A") - 10
            remain = chr(remain)
        answer.append(str(remain))

    return answer


def solution(n: int, t: int, m: int, p: int):
    # 정답을 출력하기 위한 변수 선언
    answer = ""

    # 순서, 변환할 정수
    order, number = 0, 0

    # 변환된 n 진수의 리스트
    target: list = []

    # 출현 횟수와 t보다 커질 때까지
    while len(answer) < t:
        # 만약 해당 변환된 n 진수 검사가 다 끝났다면 다음 정수 변환
        if not target:
            target = base_num(number, n)
            number += 1

        # n 진수 변환된 숫자의 자리 수를 pop하기
        digit = target.pop()

        # 튜브의 순서에 해당 pop한 숫자를 answer에 추가하고 계산
        if order == p - 1:
            answer += digit

        # 순서 변경
        order = (order + 1) % m

    return answer


case1 = (2, 4, 2, 1)
case2 = (16, 16, 2, 1)
case3 = (16, 16, 2, 2)

print(solution(*case1))
print(solution(*case2))
print(solution(*case3))
