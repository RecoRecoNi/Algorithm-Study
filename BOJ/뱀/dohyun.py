"""

풀이시간
- 약 1시간

접근법
- DFS/BFS 문제라고 해야하나?
    - 뱀의 움직임이 정해져있기 때문에 그냥 스택과 큐를 잘 이용하는 구현이라고 생각
- N 이 100 이하로 시간복잡도 충분하다고 생각됨
- 꼬리를 제거하는 과정 -> 큐와 같은 구조 (맨 처음 들어온거를 빼내야 함)
- 머리를 갱신하는 과정 -> 스택과 같은 구조 (스택을 이용하던 안하던 두 방식 다 같은 답이 나오긴 함)

회고
- 그래프 관련 문제에 예전보다는 익숙해진 느낌!!! ^-^
- 코드가 조금 복잡한 감이 있는 것 같아 다른 분들의 풀이 보고 수정할 점 꼭 짚고 가기

"""

import sys
from collections import deque

inputs = sys.stdin.readline

N = int(inputs())
K = int(inputs())

apple_idx = []
for _ in range(K):
    x, y = map(int, inputs().split())
    apple_idx.append([x-1, y-1]) # 사과 좌표 받기

L = int(inputs())

# 반시계 회전 움직임 정의 (좌표의 변화)
directions = [(-1,0), (0,-1), (1,0), (0,1)] * L

direction_info = deque()
for _ in range(L):
    sec, direction = inputs().split()
    direction_info.append([int(sec), direction]) # "초" 와 방향 전환 배열 받기

def game(start_x, start_y):
    body = deque()
    body.append([start_x, start_y])
    
    sec = 0
    angle = -1

    head_x, head_y = start_x, start_y

    while True:
        sec += 1
            
        # 방향을 고려한 머리의 움직임    
        head_x += directions[angle][0]
        head_y += directions[angle][1] 
        
        if (0 <= head_x < N) and (0 <= head_y < N): # 범위 내에서
            if [head_x, head_y] not in body: # 다음 칸에 자기 몸이 없는 경우
                body.append([head_x, head_y])
                
                if [head_x, head_y] not in apple_idx: # 사과가 아니라면
                    body.popleft() # 가장 먼저 들어온 body (즉 꼬리) 제거
                
                else: # 사과라면
                    apple_idx.remove([head_x, head_y]) # 사과를 먹었다고 처리
            
            elif [head_x, head_y] in body: # 다음 칸에 자기 몸이 있으면
                return sec # 종료
        
        else: # 범위 안에 안들면 (즉 벽 통과 시)
            return sec # 종료
        
        if direction_info: # 사전에 정의한 방향에 따라 방향 바꾸기
            if sec == direction_info[0][0]:
                if direction_info[0][1]=="L":
                    angle += 1
                else:
                    angle -= 1
                direction_info.popleft()

result = game(0,0)
print(result)
