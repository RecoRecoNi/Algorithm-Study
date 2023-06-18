"""

풀이시간
- 약 5분

접근법
- 모든 동작 방식이 deqeue 로 구현가능
- 특정 조건 만족까지 반복되는 행위 -> 반복문/재귀로도 풀이 가능

회고
- 쉬웠던 것 같아서 재귀 풀이도 하나 넣어봤습니다!!
    - 재귀문이 시간이 2배 이상 걸리는데 원래 그런걸까용?

"""    

### 반복문 풀이
from collections import deque

N = int(input())                                # 정수 N 입력받음
queue = deque([i for i in range(1, N+1)])       # 카드 덱 구성

while True:
    if len(queue)==1:
        print(queue[0])
        break
    queue.popleft()         # 맨 위에 있는 카드 버림
    out = queue.popleft()   # 그 다음 위에 있는 카드를 선택
    queue.append(out)       # 해당 카드를 맨 밑으로 옮김


### 재귀 풀이
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한을 풀어줌 (재귀문제에서 필수라고 함)
from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

def run(cards):
    if len(cards) == 1:
        print(cards[0])
    else:
        cards.popleft()
        out = cards.popleft()
        cards.append(out)
        run(cards)

run(queue)