"""
    최고의 집합
    https://school.programmers.co.kr/learn/courses/30/lessons/12938

    풀이시간 
    21:46 ~ 22:28 (38분)
    
    문제 조건
    자연수의 개수 : 1 ~ 10,000 (n)
    모든 원소들의 합 : 1 ~ 100,000,000

    시간 복잡도 : O(n) 

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 단순 구현(수학)
    
    - 예외처리 구간(최고의 집합이 존재하지 않는 경우) : 모든 원소의 합이 원소의 개수보다 작을 경우에는 최고의 집합이 존재하지 않음
    
    - N개의 자연수의 중복을 허용하는 집합에서 S라는 모든 원소의 합을 값을 가지는 케이스 중에서 원소들의 곱이 최대가 되는 경우
        - 최대한 항들이 커야하기 때문에 모든 항들이 균일한 값을 가져야하며 모두 같은 값을 가질 수 없을 때는 (오름차순 정렬을 만들기 위해) 뒤의 원소부터 1씩 더 클 수 있게 분배합니다.
            - divmod를 사용해서 s//n과 s%n을 연산하고 몫은 해당 값의 개수만큼 answer 리스트를 만들고 나머지의 크기만큼 뒤에서 앞의 순서로 각 원소에 1을 더해준다.
"""
from typing import List


def solution(n: int, s: int) -> List[int]:
    # 최고의 집합이 존재하지 않는 경우
    # 모든 원소의 합이 원소의 개수보다 작을 경우에는 최고의 집합이 존재하지 않음
    if n > s:
        return [-1]

    # s를 n으로 나눴을 때 몫과 나머지 연산
    n_div_value, m = divmod(s, n)

    # n개만큼 몫을 answer에 저장하기
    answer = [n_div_value for _ in range(n)]

    # 뒤에서 부터 나머지 만큼 +1씩 원소에 더해주기
    for idx in range(-m, 0):
        answer[idx] += 1

    return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
