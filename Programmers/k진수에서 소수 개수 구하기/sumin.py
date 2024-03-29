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

# 소수 판별
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
    # 변환된 수에 대한 조건으로 0이 양쪽 or 오른쪽 or 왼쪽 or 아예 안 붙는 경우에 해당하는 지 확인해야 하기 때문에 0을 기준으로 나눠줌 
    # -> 0을 기준으로 나눠지는 수는 해당 조건들 중 어느 하나라도 만족함
    for segment in converted_num.split('0'):
        if not segment: # 빈 문자열
            continue
        if is_prime(int(segment)): # 소수
            cnt += 1
    return cnt

# 테스트 케이스
n1, k1 = 437674, 3
print(solution(n1, k1))