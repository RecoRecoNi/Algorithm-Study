"""
풀이시간: 20분

<제한사항>
- 2 <= 숫자 개수(n) <= 20
- n개의 음이 아닌 정수
- 숫자의 순서는 바꾸지 않고, +/- 둘 중에 하나를 사용

<시간복잡도>
O(2^n): 연산자(+/-)둘 중 하나를 n번 선택하는 경우
- n이 최대 20이기 때문에 2^20 = 1,048,576 연산횟수로 시간 내 통과 가능
"""

from typing import List
def solution(numbers, target):
    answer = go([], numbers, target)
    return answer

def go(oper: List, nums: List, goal: int) -> int:
    """
    oper: 연산자의 개수
    nums: 숫자의 개수
    goal: 타겟 넘버
    """
    if len(oper) == len(nums): # 연산자의 개수가 숫자의 개수와 같다면
        s = 0 # 합
        for i in range(len(nums)):
            s += oper[i] * nums[i] # - 또는 +가 붙은 수를 s에 더해줌
        if s == goal: # Base condition(타겟 넘버가 되면)
            return 1
        return 0 # 모든 경우의 수를 확인했지만 타겟 넘버가 될 수 없다면 0

    now = 0 # 타겟 넘버를 만드는 방법의 수
    now += go(oper+[-1], nums, goal) # -를 붙이는 경우
    now += go(oper+[1], nums, goal) # +를 붙이는 경우
    return now


"""
테스트 1 〉	통과 (3231.89ms, 10.6MB)
테스트 2 〉	통과 (3583.76ms, 10.6MB)
테스트 3 〉	통과 (2.76ms, 10.5MB)
테스트 4 〉	통과 (11.87ms, 10.5MB)
테스트 5 〉	통과 (128.74ms, 10.4MB)
테스트 6 〉	통과 (6.73ms, 10.6MB)
테스트 7 〉	통과 (3.28ms, 10.6MB)
테스트 8 〉	통과 (24.54ms, 10.4MB)
"""