"""
풀이시간: 30분

<input>
n : 1 ≤ n ≤ 100,000
-> 최대 O(nlogn)으로 설계 가능

<solution>
1. 주어진 수열의 수를 순서대로 하나씩 확인한다.
2. 확인하고 있는 수와 지금까지 스택에 넣은 가장 큰 수를 비교한다.
2-1) 확인하고 있는 수가 현재까지 스택에 넣은 가장 큰 수보다 큰 경우
    - 수열에 '지금까지 넣은 가장 큰 수+1'부터 '현재 확인하고 있는 수'까지 스택에 push한다. ans에 +를 추가한다.
    - 스택의 top(현재 확인하고 있는 수와 동일)을 pop하고, ans에 -를 추가한다.
2-2) 확인하고 있는 수가 현재까지 스택에 넣은 가장 큰 수보다 작거나 같은 경우
    - 스택의 top이 현재 확인하고 있는 수와 같다면, top을 pop하고 ans에 -를 추가한다.
    - 스택의 top이 현재 확인하고 있는 수와 같지 않다면, 더 이상 수열을 만들 수 없으므로 'NO'를 출력하고 종료한다. <- '스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자' 규칙 때문에
3. 최종적으로 만들어진 연산을 한 줄에 한 개씩 출력한다. 
"""

import sys
input = sys.stdin.readline

n = int(input()) # 1 ≤ n ≤ 100,000
sequence = [int(input()) for _ in range(n)] # 1~n의 정수로 이루어진 수열(같은 정수가 두 번 나오지 않음)

max_num = 0
ans = []
stack = []
for x in sequence: # 주어진 수열의 수를 순서대로 하나씩 확인
    if x > max_num: # 현재 확인하고 있는 수가 지금까지 나온 수보다 크다면
        while x > max_num: # max_num+1부터 x까지 stack에 push
            max_num += 1
            stack.append(max_num)
            ans.append('+')
        stack.pop() # stack의 top에 있는 x를 pop
        ans.append('-')
    else: # x <= max_num
        if stack[-1] == x: # stack의 top이 현재 확인하고 있는 수와 같다면
            stack.pop() # pop
            ans.append('-')
        else: # 현재 stack의 top이 x와 같지 않고 x가 max_num보다 작거나 같으면 더 이상 주어진 수열을 만들 수 없음
            print('NO') # NO를 출력하고
            sys.exit(0) # 종료

print('\n'.join(map(str, ans)))