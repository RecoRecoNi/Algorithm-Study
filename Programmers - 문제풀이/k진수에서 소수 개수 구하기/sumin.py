"""
풀이시간: 20분

<input>
- 1 ≤ n ≤ 1,000,000
- 3 ≤ k ≤ 10

<solution>
1) n을 k진수로 변환
2) 소수 판별

<시간복잡도>
O(log_k*n * √n)
"""
# n을 k진수로 변환하는 함수
def convert_to_base(n: int, base: int) -> str:
    result = '' # k진수로 변환 후 값
    while n:
        n, remainder = divmod(n, base)
        result += str(remainder)
    return result[::-1]

# 소수 판별(에라토스테네스의 체)
def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def solution(n: int, k: int) -> int:
    converted_num = convert_to_base(n, k) # n을 k진수로 변환
    cnt = 0 # 조건에 맞는 소수의 개수
    for segment in converted_num.split('0'):
        if not segment: # 빈 문자열
            continue
        if is_prime(int(segment)): # 소수
            cnt += 1
    return cnt

# 테스트 케이스
n1, k1 = 437674, 3
print(solution(n1, k1))