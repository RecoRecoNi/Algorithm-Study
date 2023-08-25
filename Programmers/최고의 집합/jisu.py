'''
풀이 시작 : 2023-08-21 11:11

1 <= n <= 10,000 이므로 O(NlogN)으로 구현해야 한다.

중복집합임에 주의, 각 집합의 원소는 중복될 수 있음
최고 집합이 존재하지 않는 경우는 S가 합으로 만들어지지 않는 집합 => n보다 s가 더 작은 경우

최대한 S를 큰 수로 토막 내는 것이 각 원소의 곱이 최대가 되는 집합이다.
1. S를 N으로 나눈 몫을 m이라고 할때 집합에 m을 추가
2. S-=m, N-=1
3. N개의 수가 모일 때까지 반복
4. 정렬 후 반환

풀이 완료 : 2023-08-21 11:28 (풀이 시간 : 17분)
'''
from typing import List

def solution(n: int, s: int) -> List:

    answer:List = list()

    if n > s:               # 예외 : 최고의 집합이 만들어지지 않는 경우
        return [-1]
    
    while n > 0:            # 아래 과정을 통해 집합의 원소가 N개가 될 때까지 반복
        m = s//n                # S를 최대한 큰 수로 토막내야 한다.
        answer.append(m)        
        n -= 1
        s -= m

    return sorted(answer)   # 오름차순으로 정렬된 리스트를 반환

    
def main() -> None:
    case1 = [2, 9]
    case2 = [2, 1]
    case3 = [2, 8]

    print(solution(*case1))
    print(solution(*case2))
    print(solution(*case3))

main()