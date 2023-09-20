"""
풀이 시작 : 2020-09-20 11:05

#### 제한 사항
- numbers의 길이는 1,000,000이므로 O(NlogN) 이하의 알고리즘을 설계해야 한다.

[9,  1,  8, 3,  6, 10, 11]
[10, 5, 10, 6, 10, 11, -1]

"""
from typing import List


def solution(numbers: List[int]) -> List[int]:
    idx = len(numbers) - 1
    result = [0 for _ in range(len(numbers))]

    while idx >= 0:
        for i in range(idx, -1, -1):
            if numbers[idx] > numbers[i]:
                result[i] = numbers[idx]

        if result[idx] == 0:
            result[idx] = -1

        idx -= 1

    return result


def main() -> None:
    case1 = [2, 3, 3, 5]
    case2 = [9, 1, 5, 3, 6, 2]
    case3 = [1, 1, 1]
    case4 = [1, 2, 3]
    case5 = [3, 2, 1]
    case6 = [1, 3, 2]
    case7 = [9, 1, 5, 3, 6, 10]

    print(solution(case1))  # [3, 5, 5, -1]
    print(solution(case2))  # [-1, 5, 6, 6, -1, -1]
    print(solution(case3))  # [-1, -1, -1]
    print(solution(case4))  # [2, 3, -1]
    print(solution(case5))  # [-1, -1, -1]
    print(solution(case6))  # [3, -1, -1]
    print(solution(case7))  # [10, 5, 6, 6, 10, -1]


main()
