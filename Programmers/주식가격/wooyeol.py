"""
    주식가격
    https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

    풀이시간 
    11:30 ~ 11:50 (20분)
    
    문제 조건
    1 <= prices의 각 가격 <= 10,000
    2 <= prices의 길이 <= 100,000

    시간 복잡도 : 
    O(N(N+1)/2)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 큐 와 스택

    문제를 잘못 읽어 10,000개의 데이터 인줄 알고 시간 복잡도를 생각하지않고 풀이했는데
    다시보니 100,000개인 것을 확인하였습니다. 
    
    그럼 이 풀이로는 풀이가 되지 않아야하는 의아함이 들어 다른 풀이를 참조하였습니다.

    풀이 참고 : https://velog.io/@soo5717/프로그래머스-주식가격-Python

    해당 풀이를 참고했을 때 2배 정도 빠른 효율성 테스트 결과를 확인 할 수 있었습니다.

"""
from collections import deque

# deque을 사용한 방법
def solution1(prices):
    # 전체 데이터 덱으로 변환
    dq = deque(prices)
    answer = []
    
    while dq:
        # 덱의 첫 요소 popleft
        target = dq.popleft()

        sec = 0
        # 현재 타겟보다 감소한 값이 존재한다면 break 후 시간 반환
        for price in dq:
            sec += 1
            if price < target:
                break
        answer.append(sec)
                
    return answer

# stack을 사용한 방법
def solution2(prices):
    # answer를 max 값으로 초기화
    # ex) [1,2,3,2,3] -> [4,3,2,1,0]
    answer = [v for v in range(len(prices)-1, -1, -1)]

    stack = [0]
    for idx in range(1, len(prices)):
        # prices의 값이 감소했다면
        while stack and prices[stack[-1]] > prices[idx]:
            # 가격이 떨어지지 않은 기간 업데이트
            p_idx = stack.pop()
            answer[p_idx] = idx - p_idx
        stack.append(idx)
    return answer

case1 = [1, 2, 3, 2, 3] 
print(solution1(case1)) # [4, 3, 1, 1, 0]
print(solution2(case1)) # [4, 3, 1, 1, 0]