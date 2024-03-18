"""
풀이시간: 20분

<input>
topping: 롤케이크에 올려진 토핑들의 번호를 저장한 정수배열(1 ≤ topping의 길이 ≤ 1,000,000)
- 1 ≤ topping의 원소 ≤ 10,000

<solution>
전체 토핑의 개수와 토핑의 가짓수에서 철수가 먹게되는 토핑의 개수와 가짓수를 계속해서 갱신하며 답을 찾아나간다.
이 때, set 자료형을 써서 철수가 먹게되는 토핑의 가짓수를 O(1)에 탐색한다.

<시간복잡도>
O(N)
"""
from typing import List
from collections import Counter


def solution(topping: List) -> int:
    """
    topping: 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열
    """
    answer = 0 # 롤케이크를 공평하게 자르는 방법의 수
    tot = Counter(topping) # 각 토핑의 개수
    tot_cnt = len(tot) # 전체 토핑의 가짓수

    # 철수가 먹게되는 토핑의 종류
    eat = set()
    eat_cnt = 0
    for x in topping:
        # 기존에 없는 토핑인 경우 -> 토핑을 set에 추가하고, 먹게되는 토핑의 가짓수도 증가
        if x not in eat:
            eat.add(x)
            eat_cnt += 1
        # 전체 토핑에서 철수가 먹게되는 토핑의 개수 1 감소
        tot[x] -= 1
        if tot[x] == 0: # 만약 해당 토핑을 모두 철수가 먹게된다면 동생이 먹는 토핑의 가짓수 1 감소
            tot_cnt -= 1
        if eat_cnt == tot_cnt: # 철수가 먹는 토핑의 가짓수와 동생이 먹는 토핑의 가짓수가 같아지면 경우의 수 1 증가
            answer += 1
        elif eat_cnt > tot_cnt: # 철수가 먹는 가짓수가 더 커진다면 더 이상 확인할 필요 없으니 반복문 종료
            break

    return answer


def main() -> None:
    case1 = [1, 2, 1, 3, 1, 4, 1, 2]
    case2 = [1, 2, 3, 1, 4]
    print(solution(case1)) # 2
    print(solution(case2)) # 0

main()