"""

풀이시간
- 약 30분

접근법
- n <= 10000 -> O(NlogN)
- 에라토스테네스의 체? 아직 암기 못함 -> 업그레이드 버전 소수 판별로 가자..!
- 작은 수의 소수를 left 라고했을 떄 number - left 가 소수이면 OK
    - 여러가지 경우가 나올걸 대비해 차이를 갱신
- n 이 1만까지이므로 미리 소수를 구해놓고, set 자료형을 활용하여 시간복잡도 개선
    
회고
- n 이 매우 컸다면 메모리초과 문제가 발생했을 것 같은 생각
    - 근데 에라토스테네스의 체도 마찬가지일 것 같음 (그냥 n이 매우 크게 주어지지가 않을듯!)

"""

import sys

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

inputs = sys.stdin.readline

all_prime_numbers = []
set_all_prime_numbers = set()

for i in range(2, 10000): # 주어진 범위내의 소수들을 다 저장
    if is_prime_number(i):
        all_prime_numbers.append(i)
        set_all_prime_numbers.add(i)

n = int(inputs().rstrip())

for _ in range(n):
    num = int(inputs().rstrip())
    min_diff = float('inf')

    i = 0
    while all_prime_numbers[i] <= (num - all_prime_numbers[i]): # 왼쪽 값이 오른쪽 값보다 무조건 작도록 설정
        prime_n = all_prime_numbers[i]
        left, right = prime_n, num - prime_n # 좌항, 우항 정의
        
        if right in set_all_prime_numbers: # 우항도 소수를 만족한다면,
            diff = right - left
            if diff <= min_diff: # 가장 거리가 작은 답을 출력
                min_diff = diff
                answer = (left, right)

        i += 1
    
    print(answer[0], answer[1])