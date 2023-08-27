"""
    야근 지수
    https://school.programmers.co.kr/learn/courses/30/lessons/12927

    풀이시간 
    00:33 ~ 01:16 (43분)
    
    문제 조건
    n : 1 ~ 1,000,000 이하 O(nlogn)가능 
    works의 길이 : 1 ~ 20,000
    works의 각 값 : 1 ~ 50,000

    시간 복잡도 : O(n+k) 
        n : works의 길이 20,000
        k : works의 최대 값 50,000

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 계수 정렬

    예외처리 : 남은 작업량이 퇴근까지 남은 시간보다 같거나 적으면 야근 피로도는 0
    - 최선의 값은 남은 작업량의 모든 값을 전체적으로 줄여주는 것이다.
        - 계수정렬을 사용해야한다. (Counter를 사용)
    - Counter 내에 있는 가장 큰 값을 기준으로 작업량을 분산시켜(1씩 뺄셈을 해주어) 전체적인 피로도를 낮춰야한다.

        1. 가장 크기가 큰 작업의 개수가 퇴근까지 남은 시간보다 작을 경우
            - 작업량을 분산시키고 남은 시간을 갱신
                - ex)
                    4시간짜리 작업이 2개에 3시간짜리 작업이 3개일 경우 (n = 3)
                    3시간짜리 작업을 4시간짜리 작업의 개수만큼 늘리고
                    퇴근까지 남은 시간을 1시간 빼주고 4시간짜리 작업은 0으로 변경

        2. 가장 크기가 큰 작업의 개수가 퇴근까지 남은 시간보다 크거나 같을 경우
            - 작업량을 분산시키고 남은 시간을 갱신
                - ex)
                    4시간짜리 작업이 2개에 3시간짜리 작업이 3개일 경우 (n = 1)
                    4시간짜리 작업의 개수에서 n 만큼 제외하고
                    3시간짜리 작업을 4시간짜리 작업의 개수만큼 늘려준다.
                    퇴근까지 남은 시간은 무조건 0으로 변경

        3. 분산된 작업량에 따른 피로도 계산
"""
from typing import List


def solution(n: int, works: List[int]):
    answer = 0

    # 계수 정렬을 위한 Counter 생성
    works_counter = [0] * (max(works) + 1)
    for value in works:
        works_counter[value] += 1

    # 예외처리 : 남은 작업량이 퇴근까지 남은 시간보다 적으면 야근 피로도는 0
    if sum(works) <= n:
        return 0

    # 작업량을 분산시키는 과정
    for idx in range(len(works_counter) - 1, 0, -1):
        # 1. 가장 크기가 큰 작업의 개수가 퇴근까지 남은 시간보다 작을 경우
        if works_counter[idx] < n:
            # 작업량을 분산시키고 남은 시간을 갱신
            works_counter[idx - 1] += works_counter[idx]
            n -= works_counter[idx]
            works_counter[idx] = 0

        # 2. 가장 크기가 큰 작업의 개수가 퇴근까지 남은 시간보다 크거나 같을 경우
        else:
            # 작업량을 분산시키고 남은 시간을 갱신
            works_counter[idx] -= n
            works_counter[idx - 1] += n
            n = 0

    # 분산된 작업량에 따른 피로도 계산
    for idx, value in enumerate(works_counter):
        answer += idx**2 * value

    return answer


case1 = [4, [4, 3, 3]]  # 12
case2 = [1, [2, 1, 2]]  # 6
case3 = [3, [1, 1]]  # 0

print(solution(*case1))
print(solution(*case2))
print(solution(*case3))
