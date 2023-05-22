"""
    이모티콘 할인행사
    https://school.programmers.co.kr/learn/courses/30/lessons/150368
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 단순 구현
    
    1. 할인율이 10단위로 4개만 주어졌고 이모티콘의 갯수도 7개로 주어졌다는 것은 
    7개의 이모티콘에 각 할인율을 모두 적용한 결과를 구해도 4^7(16,384)번의 연산이 진행된다는 의미이다.

    이때에 중복순열을 사용하여 모든 케이스를 구하고 해당 할인율일 때의 사람들의 이모니콘 플러스 가입 숫자와
    결재 금액을 계산하여 최대의 이윤을 구하는 해를 찾는다.

"""
import sys
from itertools import product

def compare(t1,t2):
    """
    두 개의 원소 중 이모티콘 플러스 가입자 수가 많은 원소 반환
    만약 가입자 수가 같다면 결제금액이 더 큰 원소를 반환
    """    
    if t1[0] > t2[0]:
        return t1
    elif t1[0] < t2[0]:
        return t2
    else:
        if t1[1] > t2[1]:
            return t1
        else:
            return t2

def solution(users, emoticons):
    discount_rate = [10,20,30,40]
    answer = [-1,-1]
    # 1. 이모티콘 할인율은 4개로 정해져 있으므로 중복 순열을 사용하여 각 이모티콘의 할인율 계산
    for case in product(discount_rate,repeat=(len(emoticons))): 
        plus, money = 0,0
        # 2. 이모티콘 할인율이 적용되었을 때 유저들의 구매 상황을 확인
        for rate, cost in users:
            r_cost = 0 # 이모티콘 플러스를 사용하지 않았을 때 구매하게 되는 비용
            
            # 할인된 금액으로 구매 했을 때 총 소비 비용
            for idx,discount in enumerate(case):
                # 유저의 기준보다 할인율이 높다면 구매
                if rate <= discount:
                    r_cost += emoticons[idx] * ((100 - discount) / 100)
            
            # 구매했을 때 기준 cost 이상의 금액이 나왔다면 이모티콘 플러스 결제
            if r_cost >= cost:
                plus += 1
            # 아니라면 해당 이모티콘만 사용
            else:
                money += int(r_cost)

            # 우선순위기준으로 가장 최적의 해 저장
            answer = compare(answer,[plus,money])
    return answer

# [1,5400]
users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users,emoticons))