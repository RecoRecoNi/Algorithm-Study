'''
풀이 시작 : 2023.08.11 23:31

- 인접한 괄호 쌍 '()' 을 제외하고 떨어져 있는 괄호 쌍은 모두 쇠 막대기를 나타낸다.
- 괄호 문자의 개수는 최대 100,000개이므로 O(nlogn)까지는 될 것 같다.
- 여는 괄호 '('가 연속으로 나오는 개수를 세고, 닫는 괄호 ')'가 나왔을 때 이전 괄호가 여는 괄호 '('이면(레이저), 직전까지 여는 괄호의 수 만큼 막대 조각을 얻는 데서 아이디어를 얻어 풀이 시작
- 단 한번의 순회로 답을 얻어낼 수 있으므로 O(N)의 풀이가 가능할 것이다.

풀이 완료 : 2023.08.12 00:23
'''

import sys

input = sys.stdin.readline

def solution() -> None:
    brakets: str = input().rstrip()             # 그냥 rstrip()을 생활화할께요 이거 때문에 시간을 ㅠㅠㅠ
    count: int = 0                              # 중첩 여는 괄호 수를 관리할 변수
    answer: int = 0                             # 잘린 막대 수를 관리할 변수

    for idx in range(len(brakets)):             # 모든 괄호를 순회
        if brakets[idx] == '(':                 # 여는 괄호가 나오면
            count += 1                              # 여는 괄호 중첩 개수 +1
        else:                                   # 닫는 괄호가 나오면
            if brakets[idx-1] == '(':               # 직전 괄호가 여는 괄호일 경우 (레이저)
                count -= 1                              # 직전 여는 괄호는 중첩 제외
                answer += count                         # 현재 열린 괄호 수 만큼의 막대 조각을 얻음
            else:                                   # 직전 괄호가 닫는 괄호일 경우 
                count -= 1                              # 열린 괄호 중 가장 짧은 괄호가 닫힘, 중첩 열린 괄호 수 -1
                answer += 1                             # 직전 레이저에 의해 남은 부분의 막대 조각을 고려해주어야 함

    print(answer)

solution()