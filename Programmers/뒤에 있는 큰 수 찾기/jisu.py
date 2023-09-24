"""
풀이 시작 : 2023-09-20 11:05

#### 제한 사항
- numbers의 길이는 1,000,000이므로 O(NlogN) 이하의 알고리즘을 설계해야 한다.

#### 풀이
- 뒤에서부터 접근
- i와 i+1을 비교해서 i+1이 더 큰 경우는 값을 dp에 저장하고, 더 작은 경우는 dp[i+1]과 비교해서 dp[i+1]이 더 큰 경우 dp[i] = dp[i+1]
    - case7 = [9, 1, 5, 3, 6, 10]  # [-1 5 -1 6 10 -1] <- 이 경우가 반례, 첫 번째 원소가 10의 정보를 알아야 한다.

풀이 중단 : 2023-09-20 11:55 (50분 경과)
풀이 재개 : 2023-09-22 00:00

#### 풀이
- dp 테이블을 만들어도 dp[i]와 dp[i+1] 비교만을 수행해야지 거슬러 탐색을 수행하면 시간초과 발생 (O(N^2)과 같은 효과임)
    - 근데 그러면 답을 도출해낼 수 없다....
- 큐를 활용? 어차피 가장 가까이 있는 큰 수는 dp가 채워지는 순간 업데이트 되는 것, 
    - 거슬러 찾아 올라가지 않고 찾아 올라가는 과정에서의 수는 버려도 된다. (다음 원소 입장에서도 필요 없음)
    - 이를 위해서 appendleft와 appendpop을 이용했음 -> ?? -> stack으로 변경
- 만약 numbers[i]가 numbers[i+1]보다 작다면, stack에 들어온 순서대로 비교해서 numbers[i]보다 작은 원소는 전부 pop, 
    - numbers[i]보다 큰 첫 번째 큰 원소가 뒤에서 가장 가까이 있는 큰 수임
    - 만약 안나오면 뒤에 큰 수가 없는 것이므로 -1
- 18~20번 라인의 아이디어를 떠올리기까지 너무 많은 시간이 걸렸다...
풀이 완료 : 2023-09-22 00:27 (풀이 시간 : 1시간 17분 소요)


"""
from typing import List


def solution(numbers: List[int]) -> List[int]:
    dp = [-1 for _ in range(len(numbers))]
    stack = [numbers[-1]]

    for i in range(
        len(numbers) - 2, -1, -1
    ):  # 맨 뒤의 수는 차피 -1 고정, 맨 뒤에서 두 번째 원소부터 거꾸로 탐색
        while (
            stack and stack[-1] <= numbers[i]
        ):  # 스택에 들어온 순서대로 탐색, numbers[i]보다 큰 원소 발견할 때까지
            stack.pop()  # 원소 제거, 어차피 다음 순회할 원소 입장에서도 필요 없는 수들임
        dp[i] = stack[-1] if stack else -1  # numbers[i]보다 큰 원소가 발견되면 그 수를 가져가고 없으면 -1

        stack.append(numbers[i])  # 뒤에서부터 탐색 순서대로 stack에 넣기

    return dp


def main() -> None:
    case1 = [2, 3, 3, 5]
    case2 = [9, 1, 5, 3, 6, 2]
    case3 = [1, 1, 1]
    case4 = [1, 2, 3]
    case5 = [3, 2, 1]
    case6 = [1, 3, 2]
    case7 = [9, 1, 5, 3, 6, 10]  # [-1 5 -1 6 10 -1]

    print(solution(case1))  # [3, 5, 5, -1]
    print(solution(case2))  # [-1, 5, 6, 6, -1, -1]
    print(solution(case3))  # [-1, -1, -1]
    print(solution(case4))  # [2, 3, -1]
    print(solution(case5))  # [-1, -1, -1]
    print(solution(case6))  # [3, -1, -1]
    print(solution(case7))  # [10, 5, 6, 6, 10, -1]


main()
