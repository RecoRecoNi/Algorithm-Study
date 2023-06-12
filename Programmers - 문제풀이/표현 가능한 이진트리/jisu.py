'''
`12:35 -> 1시간 가량 고민 후 풀이 참고`

numbers의 길이 <= 10000
numbers의 원소의 크기 <= 1,000,000,000,000,000
무조건 logn

1. 2진수로 변환 후 앞단에 0을 붙여 포화 이진 트리 크기(1, 3, 7, 15, ..., 2^n - 1)로 만들기
2. 재귀적으로 중위 순회 결과가 정상적인 포화 이진 트리를 만들어내는지 검사 => 여기서 부터 막힘

KEY : 이진 트리를 만족하기 위해서 자식 노드 위에는 항상 부모 노드가 존재해야 한다.
**이진수[mid] == '1'**
'''

import math

def de2bi(n):
    return bin(n)[2:]
        
def check(bi, prev_parent):
    mid = len(bi)//2                # 해당 부분 트리의 루트 노드
    if bi:
        son = (bi[mid] == '1')      # 부모노드 존재 여부
    else:               
        return True                 # 리프 노드에 도달하면 True 반환하고 재귀 탈출
    
    if son and not prev_parent:     # KEY : 자식 노드는 있는데 부모 노드가 없다 => 이진 트리 자체를 못만들게 된다.
        return False
    else:
        return check(bi[mid+1:], son) and check(bi[:mid], son)      # 해당 부분 트리의 루트 기준 왼쪽 부분트리와 오른쪽 부분 트리를 재귀적으로 탐색

def solution(numbers):
    result = []

    for number in numbers:

        if number == 1:                                         # 숫자 1이 들어오면 조건 만족
            result.append(1)
            continue

        bi = de2bi(number)                                      # 2진수로 변환
        digit = 2 ** (int(math.log(len(bi), 2)) + 1) - 1        # 포화 이진 트리 크기는 각 level에 대해서 2^(level)+1 의 크기를 가진다.
        bi = "0" * (digit - len(bi)) + bi                       # 포화 이진 트리 크기(1, 3, 7, 15, ..., 2^n - 1)로 만들기 위해서 앞단에 차이 만큼 0 붙이기

        if bi[len(bi)//2]=='1' and check(bi, True):             # 루트 노드가 0이면 초장부터 글러먹음, 모든 자식 노드 위에 부모 노드가 있는지 검사
            result.append(1)
        else:    
            result.append(0)

    return result

case1 = [7, 42, 5]          # [1, 1, 0]
case2 = [63, 111, 95]       # [1, 1, 0]

print(solution(case1))
print(solution(case2))