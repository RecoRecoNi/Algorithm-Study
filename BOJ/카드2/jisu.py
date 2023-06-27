'''
16:30 -> 16:35

1 <= N <= 500,000 이므로 O(N) 안에 해결
'''

import sys
from collections import deque

input = sys.stdin.readline

def main():

    N = int(input())
    deq = deque(range(1, N+1))              # N(1~N)장의 카드 구성

    while len(deq) > 1:                     # 카드가 1장 남을 때까지 아래 반복
        deq.popleft()                       # 제일 위에 있는 카드 바닥에 버리기
        deq.append(deq.popleft())           # 제일 위에 있는 카드를 제일 아래 있는 카드 밑으로 옮기기

    print(deq[0])                           # 제일 마지막에 남게 되는 카드

if __name__ == '__main__':
    main()

