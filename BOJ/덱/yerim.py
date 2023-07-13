"""
[백준 10866번: 덱 (Silver 4)](https://www.acmicpc.net/problem/10866)
- 풀이 시간: 10분
- 접근 방법
 - 덱 자료형 사용
 - 문제 그대로 구현
"""

from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            x = deq.popleft()
            print(x)
    elif cmd[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            x = deq.pop()
            print(x)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
