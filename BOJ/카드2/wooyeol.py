"""
    카드2
    https://www.acmicpc.net/problem/2164
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> deque을 사용하여 O(1)연산을 반복 실행한다.

    50만회가 최대이기 때문에 단순 구현이 가능하였고 이때에 pop, append 연산이 O(1)이어야한다.
    따라서 deque를 사용하여 구현한다면 시간 초과가 걸리지 않는다.

    len() 함수를 매번호출하지 않고 length를 기억하는 변수를 사용하였더니 시간이 (240 -> 212 ms)로 단축되었습니다.
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 1 ~ N의 카드를 담은 cards 행렬을 deque로 구현한다.
cards = deque([num for num in range(1, N + 1)])
cards_length = len(cards)

# cards의 갯수가 1개가 될 때 까지 다음의 과정을 반복한다.
while cards_length > 1:
    # 1. cards의 가장 왼쪽의 값을 제거한다.
    cards.popleft()
    # 2. cards의 가장 왼쪽의 값을 제거하여 우측의 끝에 삽입한다.
    cards.append(cards.popleft())
    cards_length -= 1

print(cards[0])
