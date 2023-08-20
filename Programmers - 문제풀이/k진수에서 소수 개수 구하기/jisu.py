'''
풀이 시작 : 2023-08-20 13:24

1 <= n <= 1,000,000 이므로, 1,000,000을 2진수로 바꿨을 때 길이가 M 이라면 
1 <= M <= 20 -> 그냥 일단 구현하면 되겠다.

n을 k진수로 바꾼 후 0을 기준으로 split

가장 왼쪽, 오른쪽 원소 -> P0, 0P 검사 : 그냥 가장 왼쪽, 오른속 원소가 소수인지
중간 원소 -> 0P0 검사 : 가운데 원소가 소수인지
원소가 하나일 경우 -> P 검사 -> 해당 원소가 소수인지

===> 결국 0을 split 한 리스트에서 소수 개수를 세면 된다.

풀이 완료 : 2023-08-20 13:48 (풀이 시간 : 24분)

'''
from typing import List

def de2k(n:int, k: int) -> str:                     # 10진수(decimal) -> k진수
    result = ''

    while n > 0:
        result += str(n%k)
        n //= k

    return str(result[::-1])

def isPrimeNumber(num: int) -> bool:                # 소수 판별
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):         # n의 n을 제외한 모든 약수는 [1, sqrt(n)] 내에 존재한다.
            if num%i == 0:
                return False
            
    return True

def solution(n: int, k: int) -> int:
    answer: int = 0
    kNum: str = de2k(n, k)                          # k진수로 바꾸기
    splitList: List[str] = kNum.split('0')          # 0을 기준으로 split

    for num in splitList:                           # 그 중 소수의 숫자 세기 
        if num and isPrimeNumber(int(num)):
            answer += 1

    return answer

def main() -> None:
    case1 = [437674, 3]
    case2 = [110011, 10]

    print(solution(*case1))     # 3
    print(solution(*case2))     # 2

main()