"""
    롤케이크 자르기
    https://school.programmers.co.kr/learn/courses/30/lessons/132265

    풀이시간 
    16:28 ~ 17:07 (46분)
    23:39 ~ 23:46
    
    문제 조건
    1 <= len(topping) <= 1,000,000

    시간 복잡도 :
    O(T + T) = O(2,000,000)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> dictionary
    
    - 토핑을 하나씩 검사하며 동생의 조각에 추가하고 나의 조각에서 제거하기

    - 이때에 토핑 종류가 사라졌는지 여부를 확인
        1. 동생의 조각에 현재 토핑 추가
        2. 나의 조각에 현재 토핑 제거
            - 토핑이 사라졌을 경우 현재 토핑 완전히 제거

    - 현재 토핑의 종류의 개수를 확인하여
        - 나와 동생의 토핑이 같다면 정답 개수 추가
        - 동생의 토핑이 더 커졌다면 break
"""
from collections import defaultdict

def solution(topping):
    answer = 0

    # 나의 조각에 있는 토핑의 종류와 개수
    me = defaultdict(int)
    for cur_top in topping:
        me[cur_top] += 1

    # 동생의 조각에 있는 토핑의 종류와 개수
    brother = defaultdict(int)

    while topping:
        # 현재 넘기는 토핑
        cur_topping = topping.pop()

        # 1. 동생의 조각에 현재 토핑 추가
        brother[cur_topping] += 1

        # 2. 나의 조각에 현재 토핑 제거
        me[cur_topping] -= 1
        
        # 토핑이 사라졌을 경우 현재 토핑 완전히 제거
        if me[cur_topping] == 0:
            del me[cur_topping]
        
        # 나의 토핑 종류 세기
        my_topping_count = len(me)
        # 동생의 토핑 종류 세기
        brother_topping_count = len(brother)

        # 나와 동생의 토핑 종류의 개수가 같다면 정답 증가
        if brother_topping_count == my_topping_count:
            answer += 1
        
        # 동생의 토핑 종류의 개수가 더 크다면 Break
        elif brother_topping_count > my_topping_count:
            break
    
    return answer

case1 = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(case1)) #2

case2 = [1, 2, 3, 1, 4]
print(solution(case2)) #0