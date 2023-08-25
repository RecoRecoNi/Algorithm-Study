"""

풀이시간
- 약 30분 고민해보고 도저히 손도 안 떨어져서 레퍼런스를 참고해서 공부해보자고 생각

접근법
- numbers 의 원소의 크기가 10^15 -> 시간복잡도 무조건 고려
    - 라고 생각했지만 이진수로 변환을 하기 때문에 생각보다 별로 안될 것이라고 생각
- Python 내장 bin 함수를 이용하면 십진수 값을 이진수 문자열로 돌려줌!

회고
- 진짜진짜 도저히 모르겠어서 레퍼런스 풀이를 여러 개 찾아봐도 도저히 모르겠음
- 코딩테스트 문제 풀면서 아예 문제 자체가 낯선 개념인게 처음이라 당황스럽다 ... 자료구조/알고리즘 개념이 없어서 그런가 ...

"""

import math

def check_tree(s):
    l_s = len(s)
    if l_s <= 1:
        return s
    center = l_s // 2
    if s[center] == '1':
        return check_tree(s[:center]) + s[center] + check_tree(s[-center:])
    else:
        return '0' * l_s
    
def solution(numbers):
    answer = []

    for n in numbers:
        s = bin(n)[2:]
        l = len(s)
        new_l = 2 ** int(math.log2(l) + 1) - 1
        s = '0' * (new_l - l) + s
        if s == check_tree(s):
            answer.append(1)
        else:
            answer.append(0)

    return answer