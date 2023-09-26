"""
풀이시간: 50분

<input>
n: 수열 s의 길이 (1 <= n <= 1,000,000)
k: 삭제할 수 있는 최대 횟수 (1 <= k <= 100,000)
s: 수열 (1 <= 원소의 값 <= 1,000,000)

<solution>
최대 K개의 수를 삭제할 수 있다면, 연속한 짝수 부분수열의 길이를 길게 하기 위해 홀수만 K번 삭제를 해야 한다.
-> 홀수를 K개 포함하는 부분수열 중에서 가장 긴 것을 찾는 문제
1. left와 right를 0부터 시작해 연속된 부분 수열을 탐색한다.
2. right를 이동하면서, 홀수가 나오면 해당 수를 제거한다(실제로 remove가 아니라 remove_cnt를 통해 개념적으로 제거)
3. 만약 remove_cnt가 제거할 수 있는 최대 개수인 K를 넘어선다면 left를 옮겨준다.
4. right를 끝까지 이동할 때까지, 가장 긴 연속된 짝수 부분 수열의 길이를 확인한다.

<시간복잡도>
O(n)
- 두 포인터는 한 번에 하나의 요소만 확인하므로 모든 요소를 확인하는데 O(N)
- while문에서 홀수를 삭제하려면 left 포인터를 최악의 경우 (remove_cnt - K)번 이동
"""
import sys
input = sys.stdin.readline


n, k = map(int, input().split()) # n: 수열의 길이, k: 최대 삭제 횟수
s = list(map(int, input().split())) # 수열 s

max_len = 0 # 가장 긴 연속된 짝수 부분 수열의 길이

left = 0 # 연속된 부분 수열의 왼쪽 포인터
remove_cnt = 0 # 현재 연속된 부분 수열에서 삭제한 홀수의 개수

for right in range(n): # 연속된 부분 수열의 오른쪽 포인터를 이동하며 검사
    # 현재 오른쪽 포인터가 가르키고 있는 수가 홀수라면, 해당 수를 제거
    if s[right] % 2 != 0:
        remove_cnt += 1
        # 제거한 홀수의 개수가 k를 넘으면, (홀수의 개수가 K개 이하가 될 때까지) left를 옮긴다.
        while remove_cnt > k:
            if s[left] % 2 != 0:
                remove_cnt -= 1
            left += 1

    max_len = max(max_len, right-left+1-remove_cnt) # 현재 연속된 부분 수열의 길이를 갱신

print(max_len)