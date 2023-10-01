"""
풀이시간: 35분

<input>
prices: 초 단위로 기록된 주식가격이 담긴 배열
- prices의 각 가격: 1 이상 10,000 이하인 자연수
- prices의 길이: 2 이상 100,000이하

<solution>
prices의 길이가 최대 100,000이기 때문에 최대 O(nlogn)으로 설계해야 한다.
- price를 하나씩 확인하면서 stack에 있는 (이전의) 주식 가격이 현재 price보다 크다면 주식 가격이 떨어진 것이기 때문에 stack에서 현재 price보다 큰 값들은 모두 제거한다.
- stack에 현재 price의 인덱스를 추가한다.
- 마지막 price는 처리가 안됐기 때문에 마지막 인덱스와 아직까지 스택에 남아있는 스택에 대한 처리를 해준다.
    - 이 때까지 스택에 남아있는 인덱스들은 끝까지 가격이 떨어지지 않은 거기 때문에 len(prices) - 인덱스 - 1로 값을 구해준다.


<시간복잡도>
O(N) = O(N) + O(N)
- 각 인덱스에 대한 처리는 한번씩만 발생함
- for문으로 prices의 리스트를 순회하면서 각 주식가격을 한번씩 처리
- while문이 있더라도 주식 가격의 인덱스는 스택에 한 번만 들어가고 한 번만 나오기 때문이다.
- 두 번째 for문을 통해 stack에 저장된 인덱스에 대한 처리를 하더라도 결국 O(N)이기 때문에 O(N) + O(N) = O(N)으로 볼 수 있다.
"""
from typing import List


def solution(prices: List[int]) -> List[int]:
    """
    prices: 초 단위로 기록된 주식가격이 담긴 배열
    """
    answer = [0] * len(prices)
    stack = [] # 주식가격의 시점(=인덱스)

    for idx, price in enumerate(prices):
        # 현재 주식가격이 이전의 주식 가격보다 떨어졌다면
        while stack and price < prices[stack[-1]]:
            top_idx = stack.pop()
            answer[top_idx] = idx - top_idx
        stack.append(idx)

    # 스택에 남아있는 인덱스들에 대한 처리
    for remaining_idx in stack:
        answer[remaining_idx] = len(prices) - remaining_idx - 1

    return answer


"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.7MB)
테스트 2 〉	통과 (0.03ms, 10.5MB)
테스트 3 〉	통과 (0.44ms, 10.7MB)
테스트 4 〉	통과 (0.50ms, 10.6MB)
테스트 5 〉	통과 (0.29ms, 10.6MB)
테스트 6 〉	통과 (0.02ms, 10.7MB)
테스트 7 〉	통과 (0.31ms, 10.7MB)
테스트 8 〉	통과 (0.20ms, 10.6MB)
테스트 9 〉	통과 (0.02ms, 10.6MB)
테스트 10 〉	통과 (0.34ms, 10.7MB)

효율성  테스트
테스트 1 〉	통과 (23.53ms, 19.2MB)
테스트 2 〉	통과 (16.81ms, 17.7MB)
테스트 3 〉	통과 (25.24ms, 19.8MB)
테스트 4 〉	통과 (21.36ms, 18.7MB)
테스트 5 〉	통과 (13.57ms, 17.3MB)
"""