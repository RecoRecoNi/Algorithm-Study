"""
풀이 시작 : 2023-09-26 12:55

풀이 참고 : 2023-09-26 14:35 (1시간 40분 경과)
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
S = list(map(int, input().rstrip().split()))


def get_odd_len(low: int, high: int) -> int:
    """
    홀수 개수의 누적합을 이용해 low~high 내 홀수의 개수를 반환한다.
    """
    return (
        weighted_odd_len[high] - weighted_odd_len[low]
        if S[low] % 2 == 0
        else weighted_odd_len[high] - weighted_odd_len[low] + 1
    )


weighted_odd_len = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    if S[i] % 2 != 0:
        cnt += 1
    weighted_odd_len[i] = cnt

low, high = 0, N - 1
dsc_K_cnt = 0

while get_odd_len(low, high) > K and low < high:
    low_tmp, high_tmp = low, high

    while low + 1 <= high and S[low] % 2 == 0:
        low += 1
    while high - 1 >= low and S[high] % 2 == 0:
        high -= 1

    if (low - low_tmp) < (high_tmp - high):
        high = high_tmp
        low += 1
    else:
        low = low_tmp
        high -= 1

    dsc_K_cnt += 1

print(high - low + 1 - dsc_K_cnt)
print(low, high, dsc_K_cnt)
