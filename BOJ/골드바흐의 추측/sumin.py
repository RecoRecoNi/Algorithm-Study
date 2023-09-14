"""
풀이 시간: 22분

<input>
t: 테스트케이스
n: 찾아야 하는 골드바흐 파티션의 합이 되는 짝수(4 ≤ n ≤ 10,000)

<solution>
합이 n이 되는 짝수를 어떻게 찾을 수 있을까?
- 2 ~ 최대 10,000개까지의 소수 중 합이 n이 되게 하는 두 소수를 찾기 위해서 투포인터를 사용할 수 있다.
- 소수가 정렬돼있는 상태이기 때문에 left는 시작 인덱스, right은 끝 인덱스로 초기화 후, 두 소수의 합을 계속해서 target과 비교하며 포인터를 이동시킨다.

<시간복잡도>
O(nlog(logn)): 에라토스테네스의체
find_parition 함수는 최대 O(n)


뭔가 더 최적화할 수 있는 방법이 있을 것 같은데 생각이 안남.... 여러분의 신박한 풀이 기다립니다..
"""

import sys
input = sys.stdin.readline
from typing import List

def find_prime_numbers(mx: int) -> List:
    """
    mx: 2 ~ mx까지 중 소수인 수
    """
    arr = [True] * (mx+1)
    arr[0] = arr[1] = False # 0과 1은 소수가 아님

    # 에라토스테네스의 체
    for i in range(2, int(mx**(1/2))+1):
        if arr[i]: # i가 소수인 경우
            j = 2
            while i * j <= mx:
                arr[i*j] = False
                j += 1

    return [i for i in range(len(arr)) if arr[i]]


def find_partition(target: int, prime_number: List) -> List:
    """
    target: 찾아야 하는 골드바흐 파티션의 합이 되는 짝수
    prime_number: n까지의 소수 배열
    """
    left, right = 0, len(prime_number)-1
    diff = target # 현재까지 찾은 최소 차이
    result = [0, 0] # 최소 차이를 가지는 골드바흐 파티션

    # 투포인터
    while left <= right:
        cur_sum = prime_number[left] + prime_number[right]
        if cur_sum == target: # 두 소수의 합이 target이 될 때
            if diff > prime_number[right] - prime_number[left]: # 최소 차이 업데이트
                diff = prime_number[right] - prime_number[left]
                result[0], result[1] = prime_number[left], prime_number[right]
            left += 1
        elif cur_sum < target: # 두 소수의 합이 target보다 작다면 left를 증가
            left += 1
        else: # 두 소수의 합이 target보다 크다면 right를 감소
            right -= 1
    return result

# 테스트 케이스의 수
t = int(input())
primes = find_prime_numbers(10000) # 입력으로 들어올 수 있는 가장 큰 n은 10,000이기 때문에 미리 10,000까지 모든 소수를 구해둠
for _ in range(t):
    n = int(input())
    print(*find_partition(n, primes))