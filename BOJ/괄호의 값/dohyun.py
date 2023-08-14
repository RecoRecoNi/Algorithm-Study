"""

풀이시간
- 약 40분

접근법
- 문자열 길이 되게 짧음 -> 시간복잡도 신경쓰지말고 꼼꼼히 구현해보자
- 이전 풀이 문제(쇠 막대기)에서 스택 풀이를 제대로 이해못했지만, 비슷한 느낌인 것 같아 쇠 막대기 풀이 참고
- 올바르지 못한 괄호열은 어떻게 정의할까?
    - ( 다음 ] 가 오면 땡
    - [ 다음 ) 가 오면 땡
    - 소괄호와 대괄호의 개수가 다르면 땡

회고
- 스택 풀이 이해하기!

"""

import sys

text = sys.stdin.readline().strip()
answer = 0
stack = []
tmp_ans = 1 # 곱하기 연산을 해야하므로 1부터 시작

def filter_correct(text):
    cond1 = (text.count('(')==text.count(')')) & (text.count('[')==text.count(']'))
    cond2 = (text.count('[)') + text.count('(]') == 0)

    return cond1 & cond2

if filter_correct(text):
    for i in range(len(text)):
        if text[i]=="(":
            stack.append("(")
            tmp_ans *= 2
        
        elif text[i]=="[":
            stack.append("[")
            tmp_ans *= 3
        
        elif text[i]==")":
            if text[i-1]=="(":
                answer += tmp_ans # 괄호연산이 끝났으므로 정답 더해주기
            stack.pop()
            tmp_ans //= 2 # 소괄호가 닫혔으므로 곱했던 2를 다시 나눠줌
        
        elif text[i]=="]":
            if text[i-1]=="[":
                answer += tmp_ans # 괄호연산이 끝났으므로 정답 더해주기
            stack.pop()
            tmp_ans //= 3 # 대괄호가 닫혔으므로 곱했던 3을 다시 나눠줌
            
else:
    answer = 0

print(answer)