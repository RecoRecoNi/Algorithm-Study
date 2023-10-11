"""
풀이 시작 : 2023-10-06 13:43

#### 제한 사항
- topping의 길이가 1,000,000까지 이므로 O(N) ~ O(NlogN)의 알고리즘으로 해결해야 함

#### 풀이
- set으로 변환한 개수를 바탕으로 풀이하면 어떻게 해서든 시간초과
- 시간 복잡도를 해결하기 위해 Counter(dict)와 다른 defaultdict를 활용함
- 우선 Topping의 counter를 만들기 (O(N))
- Topping의 마지막 원소부터 하나씩 defaultdict에 넣기
    - Topping.pop()
    - pop했을 때 해당 토핑을 카운터에서 -1해주고, 0이 될 경우 del (O(1))
- 매 반복마다 counter의 길이와 defaultdict의 길이를 비교해서 같으면 토핑의 종류의 개수가 같은 것

풀이 완료 : 2023-10-06 13:57(풀이 시간 : 14분 소요)
"""
from typing import List
from collections import Counter, defaultdict


def solution(topping: List[int]) -> int:
    answer = 0

    counter = Counter(topping)  # 철수 토핑 (카운터(dict))
    other = defaultdict(int)  # 동생 토핑

    while len(topping) > 1:  # 모든 자르는 경우 고려
        counter[topping[-1]] -= 1  # 철수 토핑 마지막 부분을 동생한테 옮길 것임
        if counter[topping[-1]] == 0:  # 옮겼을 떄 해당 종류 토핑이 0개가 되면
            del counter[topping[-1]]  # 카운터에서 제거
        other[topping.pop()] += 1  # 동생한테 철수 마지막 부분 옮기기

        if len(counter) == len(other):  # 철수 토핑 종류와 동생 토핑 종류를 비교
            answer += 1

    return answer


def main() -> None:
    case1 = [1, 2, 1, 3, 1, 4, 1, 2]
    case2 = [1, 2, 3, 1, 4]

    print(solution(case1))  # 2
    print(solution(case2))  # 0


main()
