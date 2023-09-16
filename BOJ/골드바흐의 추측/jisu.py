"""
풀이 시작 : 2023-09-14 16:32

#### 풀이 방법
- 에라토스테네스의 체를 활용해 10000 이하의 소수를 모두 구해 놓기
- 두 소수의 차이가 가장 작은 골드바흐 파티션 찾기

풀이 완료 : 2023-09-14 16:58 (풀이 시간 : 26분)
"""

import sys
from typing import Set

input = sys.stdin.readline


def get_prime_numbers() -> Set[int]:
    """
    에라토스테네스의 체 알고리즘을 활용해 10000이하의 모든 소수를 반환한다.
    """

    is_primes = [False, False] + [True for _ in range(9999)]
    for i in range(2, 101):
        j = 2
        while i * j <= 10000:
            is_primes[i * j] = False  # 여기서 나오는 배수는 소수가 아님
            j += 1

    # 소수인 인덱스만 반환
    return {i for i, is_prime in enumerate(is_primes) if is_prime}


prime_numbers = get_prime_numbers()


T = int(input())
for _ in range(T):
    n = int(input().rstrip())

    i = 2
    # 골드바흐 파티션 구하기
    while n - i >= i:
        # 차이가 가장 작은 골드바흐 파티션을 구하기 위함
        if (i in prime_numbers) and (n - i in prime_numbers):
            last = i
        i += 1

    print(last, n - last)
