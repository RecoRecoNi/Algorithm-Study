"""
18:10 -> 18:50 문제 이해를 잘못해서 삽질을 좀.. 
`메모리 : 39908KB / 시간 : 192 ms`


임시 스택(`stack`)과 우리가 가지고 있는 1 ~ n까지의 수(`one2n`)를 머리속으로 왼쪽, 오른쪽에 배치해놓고 생각하면 이해하기 편함
one2n의 가장 찻번째 원소부터 stack에 넣어다가 빼어서 nums를 만들어야함

1. nums를 순회하며 one2n의 가장 첫 번째 원소부터 nums의 0, 1, ..., n번째 원소보다 같거나 작은 수를 다 스택에 삽입 (one2n은 1~n까지 차례대로 있으므로)
2. 1번 과정 이후 스택의 마지막 원소에는 항상 우리가 원하는 nums의 원소가 있어야함. 
    2-1. stack[-1]이 nums의 n번째 원소와 같다면 pop 연산
    2-2. 같지 않다면 nums의 수열을 애초에 만들 수 없었던 것, flag 변수를 False로 만들어 준다.
3. nums의 마지막 원소까지 순회를 마쳤을 때 flag 변수가 True이면 저장했던 연산 순서를 출력, False이면 NO 출력

"""

import sys
from collections import deque

input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    result = []     # 연산 순서를 저장할 리스트
                    # 연산이 일어날 때 바로 출력하지 않고 리스트에 담아서 출력하는 이유는 실패하는 결과에 대해서 바로 NO라고 출력해야하기 때문
    
    
    nums = [int(input().rstrip()) for _ in range(n)]    # 만들어야 하는 수열
    stack = deque()                 # 스택 연산을 위한 임시 스택
    one2n = deque(range(1, n+1))    # 우리가 가지고 있는 수 -> 이 수들로 nums의 수열을 만들어야함 

    can_make = True                 # 수열 nums를 만들 수 있는지 없는지를 관리하는 flag 변수 

    for num in nums:                        # nums에서 앞에서 부터 하나씩 순회
        while one2n and one2n[0] <= num:    # 1. one2n의 가장 첫 번째 원소부터 nums의 n번째 원소보다 작은 수를 다 스택에 삽입 (1~n까지 차례대로 있으므로)
            result.append('+')
            stack.append(one2n.popleft())
                                            # 2. 1번 과정 이후 스택의 마지막 원소에는 항상 우리가 원하는 nums의 원소가 있어야함. (1~n까지 차례대로 연산해야하므로)
        if stack and stack[-1] == num:      # 2-1. stack[-1]이 nums의 n번째 원소와 같다면 pop 연산
            result.append('-')
            stack.pop()
        else:
            can_make = False                # 2-2. 같지 않다면 nums의 수열을 애초에 만들 수 없었던 것, flag 변수를 False로 만들어 주고 반복문 탈출
            break
    
    if can_make:                            # nums의 마지막 원소까지 순회를 마쳤을 때 flag 변수가 True이면 저장했던 연산 순서를 출력, False이면 NO 출력
        for op in result:
            print(op)
    else:
        print('NO')

main()
