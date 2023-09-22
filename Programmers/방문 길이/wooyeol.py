"""
    방문 길이
    https://school.programmers.co.kr/learn/courses/30/lessons/49994

    풀이시간 
    10:50 ~ 11:33 (43분)
    
    문제 조건
    1 <= len(dirs) : D <= 500

    시간 복잡도 : 
    O(D * (D + D)) = O(D^2)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 시뮬레이션(해쉬 테이블)
    
    - 방문했던 장소를 기억해야하는 해쉬 테이블 설계

    1. 좌표를 업데이트하는데 범위 밖으로 넘어가서 이동하지 않으면 거리 체크 X
    2. 이동한 좌표와 이동하기 전 좌표의 이동한 길을 방문한적 있는지 확인 후 없으면 중복이 제거된 이동한 거리 증가
        - 무방향성으로 길을 체크해야하기 때문에 (이동 전 좌표에서 이동 후 좌표)와 (이동 후 좌표에서 이동 전 좌표) 모두 체크
"""
from collections import defaultdict

def solution(dirs):
    # 중복이 제거된 이동한 거리
    answer = 0

    # 지나간 길 해쉬 테이블
    visited = defaultdict(list)

    # 현재 위치 초기화
    cur_x, cur_y = 0, 0

    # 주어진 방향에 따라 이동 시뮬레이션
    for d in dirs:
        prev_y, prev_x = cur_y, cur_x

        # 좌표 업데이트
        if d == "U":
            if -5 <= cur_y+1 <= 5:
                cur_y += 1
        elif d == "D":
            if -5 <= cur_y-1 <= 5:
                cur_y -= 1
        elif d == "R":
            if -5 <= cur_x + 1 <= 5:
                cur_x += 1
        elif d == "L":
            if -5 <= cur_x - 1 <= 5:
                cur_x -= 1
        
        # 이동했는지 여부 체크
        if (prev_x, prev_y) == (cur_x, cur_y):
            continue

        # 길 체크
        if ((prev_x, prev_y) not in visited[(cur_x, cur_y)]) and ((cur_x, cur_y) not in visited[(prev_x, prev_y)]):
            visited[(cur_x, cur_y)].append((prev_x, prev_y))
            visited[(prev_x, prev_y)].append((cur_x, cur_y))
            answer += 1
    
    return answer


case1 = "ULURRDLLU" # 7
case2 = "LULLLLLLU" # 7
case3 = "UDU" # 7

# print(solution(case1))
# print(solution(case2))
print(solution(case3))