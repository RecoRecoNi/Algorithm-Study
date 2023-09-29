"""
    싸이버개강총회
    https://www.acmicpc.net/problem/19583

    풀이시간 
    11:20 ~ 12:10 (50분)
    
    문제 조건
    (00:00 ≤ S < E < Q ≤ 23:59)
    0 < 채팅 기록 < 10만

    시간 복잡도 :
    strptime은 N 길이의 문자열의 길이를 파싱할 때 O(N) - O(5)
    O(100,000)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 해시 테이블

    시간을 datetime 객체로 변환 후 조건의 시간들과 비교하여 
    출석부에 삽입 혹은 제거 연산을 시행하고 그 횟수를 남긴다.
"""
import sys
from datetime import datetime

input = sys.stdin.readline

S,E,Q = input().split()

# S,E,Q를 Datatime 객체로 변환
S = datetime.strptime(S, "%H:%M")
E = datetime.strptime(E, "%H:%M")
Q = datetime.strptime(Q, "%H:%M")

# 출석부 이름을 저장할 집합 생성
name_table = set()

# 출석 인정된 사람 수
count = 0

while True:
    log = input().split()
    
    # log가 입력되지 않으면 break
    if not log:
        break
    
    time = datetime.strptime(log[0], "%H:%M")

    # 개강총회 시작전에 채팅을 남겼다면 출석부에 이름 추가
    if time <= S:
        name_table.add(log[1])
    
    # 개강 총회가 끝나고 스트리밍 종료 전에 채팅을 남겼다면 출석부에서 이름 확인 후 제거 및 출석 인정
    elif E <= time <= Q:
        if log[1] in name_table:
            name_table.remove(log[1])
            count += 1

print(count)