"""
풀이 시작 : 2023-09-28 16:20

#### 풀이
- 스트리밍 시작 -> 개강총회 시작 -> 개강총회 끝 -> 스트리밍 끝
    - 스트리밍 시작 -> 개총(S) : 개강총회 시작 정시까지 채팅 기록 체크
    - 개강총회 끝(E) -> 스트리밍 끝(Q) : 채팅 기록 체크
- 시간에 대한 문자열을 모두 datetime.datetime.strptime() 으로 파싱
- 시간에 대한 대소 비교를 수행하며
    - 개총 이전 시간의 기록 : set에다가 이름 기록
    - 개총 ~ 개총끝 : 패스
    - 개총끝 ~ 스트리밍 끝 : 기록된 이름이 있는 경우 카운트
        - 이때 중복해서 채팅 치는 경우를 고려해 또 다른 set에다 넣어서 개수를 센다.
- 시간에 대한 대소 비교 수행 시 부등호(이상, 초과) 조심해야 함!

풀이 완료 : 2023-09-28 17:10 (풀이 시간 : 50분 소요)

메모리 | 시간
-- | --
59568KB | 824ms

"""

import sys
import datetime

input = sys.stdin.readline

S, E, Q = map(
    lambda x: datetime.datetime.strptime(x, "%H:%M").time(), input().rstrip().split()
)  # datetime time객체 parsing

student_in = set()  # 출석 가능한 입장 기록
student_out = set()  # 출석 가능한 퇴장 기록

records = sys.stdin.readlines()
# records = []  # IDE에서 테스트 용
# while True:
#     s = input().rstrip()

#     if s == "!":
#         break

#     records.append(s)

idx = 0
count = 0

while idx < len(records):
    t, name = records[idx].split()
    # datetime time객체 parsing
    t = datetime.datetime.strptime(records[idx][:5], "%H:%M").time()
    if t <= S:  # 부등호 조심! 개총 시작하자마자 채팅 친 경우도 출석 인정
        student_in.add(name)
    elif t < E:  # 부등호 조심! 개총 끝나자마자 채팅 친 경우도 출석 인정
        pass
    elif t <= Q:
        if name in student_in:
            student_out.add(name)  # 중복 채팅 고려

    idx += 1

print(len(student_out))
