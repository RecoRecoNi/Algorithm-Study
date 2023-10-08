"""
    자동차 테스트
    https://softeer.ai/practice/info.do?idx=1&eid=1717

    풀이시간 
    14:41 ~ 15:02
    21:36 ~ 21:46 (31분)
    
    문제 조건
    * 1 ≤ n ≤ 50,000
    * 1 ≤ q ≤ 200,000
    * 1 ≤ 자동차의 연비 ≤ 1,000,000,000
    * 1 ≤ mi ≤ 1,000,000,000 (i는 1 이상 q 이하입니다. 즉, mi 는 각 질의에 대응하는 중앙값을 의미합니다.)
    
    시간 복잡도 :
    O(nlogn + q * logn)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 이진탐색

    1. 이진 탐색을 진행하기 위해서 정렬을 진행
    2. 정렬된 리스트에서 입력받은 값이 몇번째 인덱스에 존재하는지 bisect_left를 통해 확인
    3. 인덱스 값이 처음 혹은 마지막이라면 해당 값은 불가능
    4. 아니라면 왼쪽의 개수와 오른쪽의 개수를 곱해서 경우의 수를 반환합니다.
    5. 또한 입력받은 연비가 존재하지 않아도 0을 반환합니다.
"""
import sys
from bisect import bisect_left

input = sys.stdin.readline

# 데이터 입력
n,q = map(int, input().split())
cars = sorted(map(int, input().split()))

# 연비 탐색을 위한 집합
cars_set = set(cars)

# Q번 입력받으며
for _ in range(q):
    value = int(input())
    
    # 해당 연비가 존재한다면
    if value in cars_set:
        # 해당 인덱스 탐색 - 이진탐색(O(logN))
        value_idx = bisect_left(cars, value)

        # 처음과 마지막 인덱스가 아니라면 예외가 아님
        if not (value_idx == 0 or value_idx == n-1):
                left = value_idx
                right = n - 1 - value_idx
                # 경우의 수를 구하기 위해 왼쪽 개수와 오른쪽 개수를 곱한 값을 반환
                print(left * right)
        # 예외처리 : 처음과 마지막 인덱스일 경우 중앙값이 될 수 없음
        else:
            print(0)
    # 예외처리 : 주어진 연비가 존재하지 않음
    else:
        print(0)
    