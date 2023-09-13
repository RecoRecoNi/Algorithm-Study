"""
    잃어버린 괄호
    https://www.acmicpc.net/problem/1541

    풀이시간
    11:28 ~ 12:00(32분)
    
    문제 조건
    식의 길이가 최대 50
    25개의 한 자리 숫자와 24개의 연산이 있을 때
    
    시간 복잡도 : O(25 * 2)가 최대 

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 문자열

    최솟값을 사용해야하기 때문에 음의 항을 최대화 하는 것이 중요하다.

    - 만약 이전 항이 음수항이었다면 다음 음수항이 나올때까지 모든 요소들을 괄호에 추가하기
"""
import sys

input = sys.stdin.readline

# 방정식 입력받기
equation = input()

# "-" 를 기준으로 음수항을 정의
terms = equation.split("-")

# 항들에는 앞자리에 0이 채워질 수 있기 때문에 각 항들은 int로 형 변환 후 덧셈 진행
for idx, term in enumerate(terms):
    t_term = list(map(int, term.split("+")))
    terms[idx] = sum(t_term)

# 첫 번째 항은 항상 양수
answer = terms[0]

# 두 번째 항부터는 음수
for term_idx in range(1, len(terms)):
    answer -= terms[term_idx]

print(answer)