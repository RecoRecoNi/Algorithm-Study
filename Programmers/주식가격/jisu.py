"""
풀이 시작 : 2023-10-01 13:54

#### 제한 사항
- prices의 길이는 100,000 이하이므로 O(NlogN) 이하의 알고리즘을 설계해야 한다.

#### 풀이
- i번째 요소부터 모든 원소를 비교하는 방법으로 하면 시간 초과가 날 것

풀이 중단 : 2023-10-01 14:54 (1시간 경과)

#### 풀이 참고
- 스택을 활용, 스택에 떨어지지 않는 부분까지의 인댁스를 담고, 증가하지 않는 부분의 인덱스의 차를 활용한다.
    - [1, 2, 3, 2, 3]의 경우 0번째부터 떨어지지 않는 부분까지 스택에 push -> stack : [0, 1, 2]
    - idx(3)번째의 2는 stack[-1](2)번째 원소보다 작으므로, idx-stack[-1] = 3 - 2 = 1초 동안 떨어지지 않음
    - 다음 떨어지지 않는 부분까지인 3번째 4번째 인덱스까지 스택에 담으면 최종적으로 [0, 1, 3, 4]
    - 스택에 남아있는 값들은 끝날 때까지 가격이 떨어지지 않은 것이다.
        - 따라서 해당 idx의 떨어지지 않는 기간은 len(prices)-1 초에서 해당 idx를 뺀 기간이다.

풀이 완료 : 2023-10-01 15:25 (1시간 31분 소요)

"""
from typing import List


def solution(prices: List[int]) -> List[int]:
    answer = [0 for _ in range(len(prices))]
    stack = []

    for idx, price in enumerate(prices):  # 가격이 떨어지지 않는 부분까지 stack에 인덱스 담기
        while stack and price < prices[stack[-1]]:  # 값이 떨어지는 경우
            j = stack.pop()  # stack에 담긴 인덱스를 순서대로 pop해
            answer[j] = idx - j  # 어디서부터 떨어졌는지를 인덱스의 차를 통해 파악

        stack.append(idx)  # 떨어지는 부분 계산 끝났으면 다시 떨어지지 않는 부분 담기

    while stack:  # 끝날 때까지 값이 떨어지지 않은 애들
        j = stack.pop()  # stack의 값들은 해당 애들의 인덱스 값이므로
        answer[j] = len(prices) - 1 - j  # 끝날 때와 인덱스의 차가 떨어지지 않은 기간

    return answer


def main() -> None:
    case1 = [1, 2, 3, 2, 3]

    print(solution(case1))  # [4, 3, 1, 1, 0]


main()
