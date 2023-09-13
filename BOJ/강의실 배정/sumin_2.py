import sys
input = sys.stdin.readline

# 수업 개수
n = int(input())

# 수업 시작시간, 종료시간
start, end = [], []
for _ in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)

# 각각 오름차순 정렬
start.sort()
end.sort()

e = 0 # 현재까지 끝난 수업 중 가장 빨리 끝난 수업의 인덱스
for s in start:
    # 종료 시간 <= 시작 시간이면(현재 수업이 이전 수업과 겹치지 않는다면)
    if end[e] <= s: # 현재 끝난 수업 중 가장 빨리 끝난 강의실을 이어서 사용하면 된다.
        e += 1 # 끝나는 시간이 가장 빠른 강의실의 인덱스를 업데이트 해준다.
        n -= 1 # 예약했던 강의실의 개수에서 하나 빼주면 된다.
print(n)