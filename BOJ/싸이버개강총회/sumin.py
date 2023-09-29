"""
풀이시간: 20분

<input>
- s: 개강총회 시작 시간
- e: 개강총회를 끝낸 시간
- q: 스트리밍을 끝낸 시간
(00:00 ≤ S < E < Q ≤ 23:59)

최대 10만개의 채팅 기록이 주어진다.

<solution>
문제에 주어진대로
1) 개강총회를 시작하기 전, 입장 확인
2) 개강총회를 끝내고 나서 스트리밍을 끝날 때, 퇴장 확인

두 경우를 set자료형을 통해 확인한다.
채팅 기록이 시간 순서대로 주어지기 때문에 입장 확인이 됐다면 set에 추가하고, 입장확인된 학회원이 제대로 퇴장했다면 해당 이름을 제거한다.

<시간복잡도>
O(채팅 기록의 수): 최대 10만
"""
import sys
input = sys.stdin.readline


attend = set() # 출석 여부를 확인하기 위한 set
ans = 0 # 출석이 확인된 학회원의 인원수

# 개강총회 시작 시간, 끝낸 시간, 스트리밍 끝낸 시간
s, e, q = input().split()
while True:
    try:
        time, nickname = input().split()
        # 1) 입장 여부 확인
        if time <= s:
            attend.add(nickname)
        # 2) 퇴장 여부 확인
        elif e <= time <= q and nickname in attend:
            attend.remove(nickname)
            ans += 1
    except:
        break
print(ans)