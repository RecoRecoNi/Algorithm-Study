"""
    덱
    https://www.acmicpc.net/problem/10866
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 덱을 사용한 구현
    
    고찰
    python collections의 deque을 사용하여 각 명령어와 내장 메소드를 매핑해줌으로써 해결 할 수 있었습니다.
    input 데이터를 입력 받을 때 '변수, *변수 = input().split()'을 사용한다면 커맨드와 인자를 받는 경우를 구분 할 수 있어 좋은 것 같습니다.

"""
import sys
from collections import deque

input = sys.stdin.readline

# 입력받을 명령어 갯수
N = int(input())

# 업데이트 할 덱 구현
D = deque()


for idx in range(N):
    cmd, *args = input().split()
    # 각 케이스에 맞는 메소드 매핑 후 모든 예외에 대해서는 -1이 반환되어야하기 때문에 else문을 통해 한 번에 예외처리를 진행
    if cmd == "push_front":
        D.appendleft(*args)
    elif cmd == "push_back":
        D.append(*args)
    elif cmd == "pop_front" and D:
        print(D.popleft())
    elif cmd == "pop_back" and D:
        print(D.pop())
    elif cmd == "size":
        print(len(D))
    elif cmd == "empty":
        print(0 if D else 1)
    elif cmd == "front" and D:
        print(D[0])
    elif cmd == "back" and D:
        print(D[-1])
    else:
        print(-1)
