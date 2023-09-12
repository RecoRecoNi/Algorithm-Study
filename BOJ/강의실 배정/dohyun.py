"""

풀이시간
- 1시간 풀이 후 실패로 답지 참조

접근법
- N <= 이십만 -> 최대 O(NlogN) 복잡도로 해결
- 최대한 겹치는 시간이 없게 해야 최소의 강의실을 사용

- 틀린 풀이
    - K 시간동안 강의실이 몇개 있는지를 딕셔너리에 담아보자
        - 메모리초과..?
- 정답 풀이
    - 정렬을 활용해서 수업의 시작과 끝을 체크하여 정답값을 갱신하는 형태
        - 시작하면 +1, 종료하면 -1, 정답값은 가장 많이 수업이 진행되고 있을 때 강의실 수

회고
- 그동안 공간복잡도문제(메모리초과)가 있었던 적이 없어서 당황 ...
    - 종료시간 범위가 10^9 이라 리스트가 아닌 딕셔너리를 활용해 더욱 메모리를 아꼈다고 생각했는데 턱없이 부족했던 것 같음
- 이런 유형(?)의 문제를 가끔 풀어봤던 것 같은데 항상 많이 취약했던 것 같음, 연습 하기!

"""

# 틀린 풀이
import sys
from collections import defaultdict

inputs = sys.stdin.readline

n = int(inputs())
arr = []
for _ in range(n):
    arr.append(list(map(int, inputs().split())))

times = defaultdict(int)

for time in arr:
    s, e = time # start, end
    for i in range(s, e): # 끝나는 시간에는 수업시작가능 (따라서 e+1 가 아닌 e)
        times[i] += 1

print(max(times.values()))

# 정답 풀이
import sys

inputs = sys.stdin.readline

n = int(inputs())
events = []

for _ in range(n):
    s, e = map(int, inputs().split())
    events.append((s, 1))  # 수업 시작 이벤트
    events.append((e, -1))  # 수업 종료 이벤트

events.sort()  # 이벤트를 시간 순서대로 정렬

classrooms = 0  # 현재 사용 중인 강의실 개수
max_classrooms = 0  # 최대로 필요한 강의실 개수

for _, event_type in events:
    if event_type == 1:  # 수업 시작 이벤트
        classrooms += 1
        max_classrooms = max(max_classrooms, classrooms)
    else:  # 수업 종료 이벤트
        classrooms -= 1

print(max_classrooms)