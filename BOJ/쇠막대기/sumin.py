"""
풀이시간: 25분

<input>
괄호 문자의 개수는 최대 100,000개 -> O(NlogN)내로 해결해야 함

<solution>
- 레이저와 쇠막대기를 구분해줘야 한다.
    1) 여는 괄호의 경우 -> stack에 현재 인덱스+1을 추가
    2) 닫는 괄호의 경우(레이저 or 쇠막대기인지 구분 가능)
       - 레이저는 stack의 top과 인덱스가 1차이가 남
       - 쇠막대기의 끝은 stack의 top과 항상 1보다 더 많은 차이가 남

<시간복잡도>
- O(n)
"""

a = input()
stack = []
ans = 0 # 잘려진 쇠막대기 조각의 총 개수
cnt = 0 # stack에 들어있는 막대기(열린괄호)의 개수

for i in range(len(a)):
    if a[i] == '(': # 열린 괄호는 스택에 추가
        stack.append(i+1)
        cnt += 1
    else: # 닫힌 괄호이면 레이저인지 쇠막대기의 끝인지 구분해야됨
        cnt -= 1
        if stack[-1] == i: # 레이저는 인덱스가 1차이 남
            # 레이저면 잘려진 막대기의 개수를 더해줌(잘려진 막대기의 개수 = 스택의 길이)
            stack.pop()
            ans += cnt
        else: # 쇠막대기의 끝이면 + 1
            stack.pop()
            ans += 1
print(ans)