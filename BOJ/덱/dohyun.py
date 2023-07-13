"""

풀이시간
- 5분

접근법
- deque 자료구조로 모두 풀이 가능
- 최대한 간단하게 쓰고 싶어 이항 연산자 사용

회고
- 덱 문제 계속 나오니까 뭔가 계속 똑같은 문제를 푸는 느낌이네요 ... ㅎ

"""

import sys
from collections import deque

question = sys.stdin.readline           # 문자열 입력받음

N = int(question())                     # 반복 횟수 N 입력받음
queue = deque()                         # 정수를 저장하는 빈 큐 정의

for _ in range(N):
    command = question().rstrip()       # 명령 입력받음
    
    if len(command.split())==2:         # push 관련 명령일 경우 숫자도 함께 들어오므로 분리
        command, num = command.split()
        num = int(num)

    if command=='push_front':
        queue.appendleft(num)
    
    elif command=='push_back':
        queue.append(num)

    elif command=='pop_front':
        print(queue.popleft() if len(queue)!=0 else -1)
    
    elif command=='pop_back':
        print(queue.pop() if len(queue)!=0 else -1)

    elif command=='size':
        print(len(queue))

    elif command=='empty':
        print(1 if len(queue)==0 else 0)
    
    elif command=='front':
        print(queue[0] if len(queue)!=0 else -1)

    elif command=='back':
        print(queue[-1] if len(queue)!=0 else -1)