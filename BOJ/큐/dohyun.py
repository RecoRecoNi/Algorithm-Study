"""

풀이시간
- 약 10분

접근법
- 문제를 읽어보니 deque 에서 전부 구현가능
- 제출 전까진 시간 복잡도가 문제일까? 라는 생각을 하긴 했지만 size 연산 제외 그럴 여지는 딱히 보이지 않았음
    - 따라서 바로 deque 로 구현!

회고
- 나름 easy 했던 문제였던 것 같은데 그대로 따라가기만 한거라 다른 분들의 디테일이 궁금하네요!

"""

import sys
from collections import deque

question = sys.stdin.readline           # 문자열 입력받음

N = int(question())                     # 반복 횟수 N 입력받음
queue = deque()                         # 정수를 저장하는 빈 큐 정의

for _ in range(N):
    command = question().rstrip()       # 명령 입력받음
    
    if len(command.split())==2:         # push 명령일 경우 숫자도 함께 들어오므로 분리
        command, num = command.split()
        num = int(num)

    if command=='push':
        queue.append(num)
    
    elif command=='front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif command=='back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    
    elif command=='pop':
        if not queue:
            print(-1)
        else:
            out = queue.popleft()
            print(out)
    
    elif command=='size':
        print(len(queue))
    
    elif command=='empty':
        if not queue:
            print(1)
        else:
            print(0)


