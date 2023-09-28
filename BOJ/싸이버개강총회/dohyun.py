"""

풀이시간
- 약 15분

접근법
- 채팅 기록은 10만 이하 -> O(NlogN)
- HH:MM 단위를 분 단위로 변환하면 편리할듯함
- 채팅 기록이 몇 개인지 입력으로 안 주어진다..?
    - try except 으로 수동 처리
- 시간은 정렬되어 입력되므로, 퇴근 시 출근 기록이 있는지 확인해야함
    - 즉 in, not in 연산 필요 -> set 자료형 사용하여 시간복잡도 개선

회고
- set 을 자주 활용하다보니 어려움없이 풀어낼 수 있었음!

"""

import sys

inputs = sys.stdin.readline

def hour_to_minute(x): # 분 단위로 변환
    return int(x[:2])*60 + int(x[3:])

S, E, Q = map(hour_to_minute, inputs().split())
answer = 0
check = set()

while True:
    try:
        time, name = inputs().split()
        time = hour_to_minute(time)

        if time <= S: # 출근 찍어진다면
            check.add(name) # 출석부에 추가

        elif E <= time <= Q: # 퇴근 찍어진다면
            if name in check: # 출석도 한 친구라면
                answer += 1 # 정답 +1
                check.discard(name) # 퇴근 가능 시간대에 여러 번 채팅친 경우를 방지
    except:
        break

print(answer)