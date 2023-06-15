"""
[백준 10845번: 큐 (Silver 4)](https://www.acmicpc.net/problem/10845)
풀이 시간: 19분

[접근 방법]
- queue 구현 시 연산 속도가 더 빠른 deque 사용
- push의 경우 띄어쓰기 후 숫자가 입력됨 => input 값을 split 함수를 사용해 리스트로 저장
- queue의 길이를 계산해야 하는 경우가 빈번하므로 미리 계산해둠
- push, size, empty 연산을 제외한 나머지 연산은 큐가 비어있는 경우 공통으로 -1을 출력하므로 그에 따라 조건 분할

"""
from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
for _ in range(int(input())):
    cmd = input().split()  # 명령 입력
    len_q = len(queue)  # 큐 길이

    if cmd[0] == "push":
        queue.append(cmd[1])  # 큐에 숫자 삽입

    elif cmd[0] == "size":  # 큐 길이 출력
        print(len_q)

    elif cmd[0] == "empty":  # 큐 길이가 0이면 1 반환, 아니면 0 반환
        print(int(len_q == 0))

    else:
        if len_q == 0:  # 큐가 비어있으면 -1 출력
            print(-1)
            continue

        elif cmd[0] == "pop":  # 가장 앞에 있는 원소 삭제하며 출력
            print(queue.popleft())

        elif cmd[0] == "front":  # 가장 앞에 있는 원소 출력
            print(queue[0])

        elif cmd[0] == "back":  # 가장 뒤에 있는 원소 출력
            print(queue[-1])
