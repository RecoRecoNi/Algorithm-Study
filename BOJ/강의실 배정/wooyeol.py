"""
    강의실 배정
    https://www.acmicpc.net/problem/11000

    풀이시간
    13:18 ~ 13:34(16분)
    
    문제 조건
    과목 갯수 1 <= N <= 200,000
    
    시간 복잡도 : O(NlogN)
    O(NlogN + NlogN) = O(NlogN)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> heap 문제
    
    - 입력받는 과목의 시작 시간 순으로 정렬
    - 입력받은 과목를 하나씩 확인하며 강의실에 push
        - 현재 강의가 시작하는 시간 전에 강의가 끝났을 경우 모두 pop
        - 현재 사용하는 강의실이 최대값보다 많다면 업데이트
"""
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

# 과목의 시작 순서로 정렬할 최소 힙 subjects
subjects = []

# 현재 강의중인 강의의 끝나는 시간을 정렬할 최소 힙 classes
classes = []

# 사용된 강의실의 최대 갯수를 업데이하기 위한 answer
answer = 0

# 과목의 시작 시간을 순서로 최소 힙 생성
for _ in range(N):
    heappush(subjects, tuple(map(int, input().split())))

while subjects:
    # 현재 수업을 해야하는 강의 pop
    c_start, c_end = heappop(subjects)

    # 현재 시간 업데이트
    time = c_start
    
    # 현재 강의중인 클래스에 해당 강의의 끝나는 시간 push
    heappush(classes, c_end)

    # 현재 시간에 강의가 끝나는 경우 모두 pop
    while classes[0] <= time:
        heappop(classes)
    
    # 현재 강의중인 강의실 갯수를 통해 최대값 갱신
    if answer < len(classes):
        answer = len(classes)

print(answer)