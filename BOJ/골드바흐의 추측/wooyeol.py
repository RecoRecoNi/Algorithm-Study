"""
    골드바흐의 추측

    풀이시간
    20:44 ~ 21:28 (44분)
    
    문제 조건
    4 <= N <= 10,000
    2 <= target <= 10,000인 짝수

    시간 복잡도 :
    O(값 입력 + 에라토스테네스의 체 만들기 + 골드바흐의 파티션 찾기)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 구현

    1. 입력 받은 케이스 중 최대 값까지의 소수를 구하기 - 에라토스테네스의 체
    2. 골드바흐 파티션 찾기 -> 두 소수의 차이가 가장 작은 것을 출력
        - 가장 작은 소수 값부터 확인하며 
        - 작은 소수 값이 먼저 나오며 target 값에서 작은 소수 값을 제외한 값이 소수일 경우 중
        - 두 소수의 차이가 최소일 경우 정답에 두 소수의 값 업데이트

"""
import sys
from collections import defaultdict

input = sys.stdin.readline

# Inputs
N = int(input())

## 정답
answer = [0] * N

## 입력받은 최대 정수
max_value = 0

## 입력받는 테스트 케이스 값
targets = [] 

# 테스트 케이스 입력 받기
for _ in range(N):
    target = int(input())
    targets.append(target)

    # 최대 값 확인 및 업데이트
    if target > max_value:
        max_value = target
    
# 1. 최대 값까지 에라토스테네스의 체 만들기
table = [False, False] + [True] * (max_value-1)

## defaultdict를 사용한 이유 입력한 순서를 기억하고 in 연산의 시간 복잡도를 O(1)로 만들기 위해서 
prime_numbers = defaultdict(bool)

## 2 이상 max_value 이하의 값까지 소수 확인 -> 10,000개까지 총 1229개의 소수
for num in range(2, max_value+1):
    if table[num]:
        prime_numbers[num] = True
        for n in range(num, max_value+1, num):
            table[n] = False
# print(prime_numbers.keys(), len(prime_numbers), max(prime_numbers))

# 2. 골드바흐의 파티션 찾기 -> 답이 무조건 있음 예외처리 필요 없음
for idx, target in enumerate(targets):
    min_gap = 100001
    # 소수 중에서
    for p_num in prime_numbers.keys():
        # 작은 소수 값이 먼저 나오며 target 값에서 작은 소수 값을 제외한 값이 소수일 경우 -> 골드바흐의 파티션
        if (p_num <= target - p_num) and (target - p_num) in prime_numbers:
            # 만약 두 소수의 차이가 최소일 경우 정답 업데이트
            if target - (2 * p_num) < min_gap:
                min_gap = target - (2 * p_num)
                answer[idx] = (p_num, target - p_num)

for row in answer:
    print(*row)