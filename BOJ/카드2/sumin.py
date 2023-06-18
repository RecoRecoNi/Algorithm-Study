"""
풀이 시간: 3분

<input>
N: 정수 N(1 ≤ N ≤ 500,000)

<solution>
시간 복잡도: O(N) <- while문이 최대 n-1번 반복되기 때문에
문제 조건대로 구현하면 된다.
"""
from collections import deque


n = int(input())
q = deque(range(1, n+1)) # 큐

while True:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft() # 1. 맨 위의 카드를 뽑는다.
    q.append(q.popleft()) # 2. 그 다음 위의 카드를 뽑는다.