"""
    큐
    https://www.acmicpc.net/problem/10845
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 단순 구현

    queue 자료형을 이해한다면 python deque을 사용하여 구현이 가능하다.
    
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

result = deque()

for _ in range(N):
    # input commands
    commands = input().rstrip().split()
    # 각 케이스 별로 데이터 처리
    if commands[0] == "push":
        result.append(commands[1])
    elif commands[0] == "size":
        print(len(result))
    elif commands[0] == "empty":
        print(0 if result else 1)
    elif commands[0] == "back" and result:
        print(result[-1])
    elif commands[0] == "front" and result:
        print(result[0])
    elif commands[0] == "pop" and result:
        print(result.popleft())
    else:
        print(-1)
