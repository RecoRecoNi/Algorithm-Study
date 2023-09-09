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
    """
    begin의 문자를 words 내의 단어들로 변환을 거듭하여 target으로 만들 수 있는 최소 카운트를 반환한다.
    """
    visited = [False for _ in range(len(words))]  # 방문 여부를 관리하는 visited 배열
    answers = []  # 정답을 담을 answers 배열

    def dfs(begin: str, target: str, cnt: int) -> int:  # 변환을 거듭하는 재귀 함수
        if begin == target:  # target으로 변환을 성공한 경우
            answers.append(cnt)  # 정답 배열의 경우의 수 추가

        for i, word in enumerate(words):  # 현재 begin 문자열에서 words에 있는 문자 중
            if (
                can_transform(begin, word) and not visited[i]
            ):  # 다른 문자가 하나이고, 아직 변환되지 않은 경우에만
                visited[i] = True  # 방문 처리 후
                dfs(word, target, cnt + 1)  # 해당 단어로 변환
                visited[i] = False  # 백트래킹, 다른 경우로 가지 뻗기

    dfs(begin, target, 0)
    return min(answers) if answers else 0  # 최소 경우의 수 반환


def main() -> None:
    case1 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
    case2 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]

    print(solution(*case1))  # 4
    print(solution(*case2))  # 0


main()
