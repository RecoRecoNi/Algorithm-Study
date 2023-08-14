"""
풀이시간: 30분

<input>
- 1 <= 문자열의 길이 <= 30

<solution>
- 단순 구현 문제, 다만 예외처리를 잘해줘야 됨!!
- 괄호값을 모두 더해줘야 하기 때문에 올바른 괄호 쌍이 닫힐 때마다 더해준다.
- 여는 괄호의 경우 항상 stack에 추가해주고, 곱해질 값을 저장해 둘 num 변수를 둔다.
    - (의 경우 괄호 안의 값은 모두 *2가 되기 때문에 num *= 2를
    - [의 경우 괄호 안의 값은 모두 *3이 되기 때문에 num *= 3를 해준다.
- 닫는 괄호의 경우 올바르지 못한 괄호쌍이 되거나, 올바른 괄호쌍이 되거나 두 가지 경우가 있다.
    1) 올바르지 못한 괄호쌍
    - stack이 비어있거나 stack의 top이 자신의 짝 괄호가 아닌 경우
    2) 올바른 괄호쌍
    - 직전 괄호가 자신의 짝 괄호인 경우 -> ans 값 갱신
- 모든 괄호값을 순회한 후 stack이 비어있으면 ans값 출력, stack이 비어있지 않다면 0 출력
    - ex) [[]

<시간 복잡도>
O(N)
"""
a = input()

stack = []
ans = 0 # 누적해서 더해질 값
num = 1 # 곱해질 값

for i in range(len(a)):
    if a[i] == '(': # 소괄호
        num *= 2
        stack.append(a[i])
    elif a[i] == '[':
        num *= 3 # 대괄호
        stack.append(a[i])
    elif a[i] == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        if a[i-1] == '(':
            ans += num # 직전 괄호가 여는 괄호였다면 값 추가
        num //= 2
        stack.pop()
    elif a[i] == ']':
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        if a[i-1] == '[':
            ans += num
        num //= 3
        stack.pop()

print(ans if not stack else 0)