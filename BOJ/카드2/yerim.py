"""
[백준: 카드2 (Silver 4)](https://www.acmicpc.net/problem/2164)

- 풀이 시간: 10분
- 접근 방법:
  - popleft 활용을 위해 deque으로 구현

"""

import sys
from collections import deque

input = sys.stdin.readline

cards = deque([n for n in range(1, int(input()) + 1)])

for _ in range(len(cards) - 1):  # N장의 카드를 (N-1)번 버려야 최종으로 1장이 남음
    cards.popleft()  # 제일 위에 있는 카드를 버림
    cards.append(cards.popleft())  # 제일 위에 있는 카드를 제일 아래로 옮김

print(cards[0])
