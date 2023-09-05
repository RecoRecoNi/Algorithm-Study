"""
풀이 시작 : 2023-09-05 13:30

#### 문제 조건
- 단어의 길이 10 이하 -> 단어룰 순회하는 과정이 포함될 수 있음
- words의 단어는 50개 이하 -> 완전 탐색(50!)은 불가능 하다.

#### 풀이
- begin에서 알파벳을 하나만 바꿔서 변환할 수 있는 word로 변환 (재귀, 백트래킹 활용)
    - 두 문자열의 다른 문자의 개수를 카운트하는 로직 필요
    - 아직 변환되지 않았고, 다른 문자의 개수가 하나인 경우만 다음 word로 재귀 가능
- target으로 변환된 경우 카운트 반환(카운트는 매개변수로 관리)
    - 모든 경우를 리스트에 담아서 최종적으로 최소 카운트를 반환
    - 리스트에 담긴 카운트가 없을 경우, 변환될 수 없는 것이므로 0을 반환

풀이 완료 : 2023-09-05 13:55 (풀이 시간 : 25분)
"""

from typing import List


def can_transform(fr: str, to: str) -> bool:
    """
    두 문자열의 다른 문자가 하나인지의 여부를 반환한다.
    """
    return len([i for i in range(len(fr)) if fr[i] != to[i]]) == 1


def solution(begin: str, target: str, words: List[str]) -> int:
    visited = [False for _ in range(len(words))]
    answers = []

    def dfs(begin: str, target: str, cnt: int) -> int:
        if begin == target:
            answers.append(cnt)

        for i, word in enumerate(words):
            if can_transform(begin, word) and not visited[i]:
                visited[i] = True
                dfs(word, target, cnt + 1)
                visited[i] = False

    dfs(begin, target, 0)
    return min(answers) if answers else 0


def main() -> None:
    case1 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
    case2 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]

    print(solution(*case1))  # 4
    print(solution(*case2))  # 0


main()
