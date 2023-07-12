"""
풀이 시간: 6분

<solution>
주어진 대로 구현하면 된다.
문제의 이름처럼 deque 라이브러리를 사용해서 구현하면 앞, 뒤에 숫자를 넣고 빼는 작업을 O(1)에 할 수 있다.

시간복잡도: o(n)
"""

import sys
input = sys.stdin.readline
from collections import deque


q = deque()
n = int(input()) # 명령의 수 입력받기
for _ in range(n): # 명령 입력받기
    op, *x = input().split()
    if op == 'push_front':
        q.appendleft(x[0])
    elif op == 'push_back':
        q.append(x[0])
    elif op == 'pop_front':
        print(q.popleft() if q else -1)
    elif op == 'pop_back':
        print(q.pop() if q else -1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        print(1 if not q else 0)
    elif op == 'front':
        print(q[0] if q else -1)
    else: # back
        print(q[-1] if q else -1)
