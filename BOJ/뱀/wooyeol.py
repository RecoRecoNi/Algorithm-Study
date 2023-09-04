"""
    뱀
    https://www.acmicpc.net/problem/3190

    풀이시간 
    13:00 ~ 14:10 (1시간 10분)
    
    문제 조건
    2 <= N <= 100
    0 <= K <= 100
    1 <= L <= 100
    1 <= X <= 10,000

    시간 복잡도 : 
    K개의 데이터 입력 - O(K)
    L개의 데이터 입력 - O(L)
    최대 게임 시간 - O(99(한 행의 최대 이동 횟수) * (4 * 25) + 99) = O(10,100) = O(N * L + N) = O(NL)
    O(K + L + NL)


    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 구현

    - 문제들의 조건들을 하나씩 코드로 나타내니 구현이 되는 문제였습니다.
    
    - 데이터 입력 및 변수 선언
        - 사용되는 변수
            - 뱀의 몸통과 길이 선언
            - 방향을 확인하기 위해서 현재 방향을 나타내는 변수 direction과 현재 direction이 의미하는 방향을 담은 directions를 선언
            - 게임 경과시간
            - 사과의 위치를 담는 defaultdict(set)
            - 뱀의 방향 변환 시점과 방향 List[tuple]
        
        - 보드의 크기 N
        - 사과의 갯수 K : 탐색이 용이할 수 있게 딕셔너리 와 value에는 집합 자료구조를 사용
        - 뱀의 방향 변환 횟수 L : 입력받은 X초 +1을 해주어 조건을 사용이 용이하게 변경

    - 시뮬레이션
        1. 게임 시간 증가
        2. 이동 방향 업데이트
            - 뱀의 방향 변환 시점과 방향 List를 확인하여 이동 방향 업데이트
        3. 이전 위치를 기준으로 현재 위치 업데이트
        4. 현재 위치에 사과 존재 여부 확인 및 뱀 길이 제한 업데이트
        5. 뱀의 몸통 조정
        6. 게임 종료 조건 확인
            - 벽에 부딪히거나
            - 자신의 몸톰에 부딪힌 경우

"""
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 변수 선언
## 뱀의 몸통과 길이 선언
snake: deque = deque([(1, 1)])
limit: int = 1

## 방향을 확인하기 위해서 현재 방향을 나타내는 변수 direction과 현재 direction이 의미하는 방향을 담은 directions를 선언
direction: int = 1
directions: tuple = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 상 우 하 좌

## 게임 경과시간
timer: int = 0

# 데이터 입력
## 보드의 크기 N
N = int(input())

## 사과의 갯수 K : 탐색이 용이할 수 있게 딕셔너리 와 value에는 집합 자료구조를 사용
K = int(input())
apples = defaultdict(set)
for _ in range(K):
    r, c = tuple(map(int, input().split()))
    apples[r].add(c)

## 뱀의 방향 변환 횟수 L : 입력받은 X초 +1을 해주어 조건을 사용이 용이하게 변경
L = int(input())
changes = deque([])
for _ in range(L):
    seconds, direction = input().split()
    changes.append((int(seconds) + 1, direction))


# 시뮬레이션 실행 (최대 100 + 99)
while True:
    # 게임 시간 증가
    timer += 1

    # 이동 방향 업데이트
    if changes and changes[0][0] == timer:
        _, direc = changes.popleft()
        if direc == "D":
            direction = (direction + 1) % 4
        elif direc == "L":
            direction = (direction + 3) % 4
        # print("방향 전환", timer, directions[direction])

    # 이전 위치
    x, y = snake[0]
    prev_snake = snake.copy()

    # 현재 위치 업데이트
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy

    # 현재 위치에 사과 존재 여부 확인 및 뱀 길이 업데이트
    if nx in apples and ny in apples[nx]:
        limit += 1
        # print("사과 먹음", limit, (nx, ny))
        apples[nx].remove(ny)

    # 뱀의 몸통 조정
    snake.appendleft((nx, ny))
    if len(snake) > limit:
        snake.pop()

    # print(timer, "초 뱀", limit, snake)

    # 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if (nx < 1 or nx > N) or (ny < 1 or ny > N) or ((nx, ny) in prev_snake):
        print(timer)
        break
