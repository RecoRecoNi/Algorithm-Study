"""
풀이 시간: 10분

<input>
- n(1 ≤ n ≤ 100,000)
- n개의 정수로 이루어진 수열(수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수)

<solution>
D[i] : i번째 수로 끝나는 가장 큰 연속합
1) i-1번째 수의 연속합에 포함되는 경우
- D[i-1] + A[i]
2) 새로운 연속합을 시작하는 경우
- A[i]

D[i] = max(D[i-1]+A[i], A[i])

<시간복잡도>
O(N)
"""
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d[0] = a[0]
for i in range(1, n):
    d[i] = a[i]
    if d[i] < d[i-1] + a[i]:
        d[i] = d[i-1] + a[i]
print(max(d))