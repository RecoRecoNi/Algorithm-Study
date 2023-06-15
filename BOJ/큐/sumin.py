"""
풀이시간: 3분

<input>
n: 명령의 수 (1 ≤ N ≤ 10,000)

시간복잡도: O(N)
"""
import sys
input = sys.stdin.readline
from collections import deque


n = int(input()) # 명령의 수
q = deque()
for _ in range(n): # n번의 연산 명령 입력받기
    op = input().split()
    if op[0] == 'push': # 정수 x를 큐에 넣는 연산 -> O(1)
        q.append(op[1])
    elif op[0] == 'pop': # 큐에 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력 -> O(1)
        print(q.popleft() if q else -1)
    elif op[0] == 'size': # 큐에 들어있는 정수의 개수를 출력 -> O(1)
        print(len(q))
    elif op[0] == 'empty': # 큐가 비어있으면 1, 아니면 0을 출력 -> O(1)
        print(0 if q else 1)
    elif op[0] == 'front': # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력 -> O(1)
        print(q[0] if q else -1)
    else: # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력 -> O(1)
        print(q[-1] if q else -1)