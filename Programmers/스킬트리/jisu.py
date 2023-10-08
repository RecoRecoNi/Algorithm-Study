"""
풀이 시작 : 2023-10-01 16:07

#### 제한 조건
- 문자열의 길이 <= 26
- 리스트의 길이 <= 20
- 26 * 20 = 5200, 한 번의 순회에서 모든 문자열의 문자를 순회하는 것은 괜찮음

#### 풀이
- 스킬트리에서 가능한 개수를 세면 됨
- 선행 스킬이 있는 스킬의 경우, 선행 스킬을 배웠는지의 여부를 판단하면 됨
    - A -> B -> C 일 때 C에 대해서 B여부만 판단하면 됨 (어차피 A를 안배우면 B를 못배우기 때문)

풀이 완료 : 2023-10-01 16:22 (풀이 시간 : 15분 소요)
"""
from typing import List


def solution(skill: str, skill_trees: List[str]) -> int:
    before = {}  # 어떤 스킬의 직전 선행 스킬을 담을 dict
    answer = 0

    for idx in range(len(skill) - 1):
        before[skill[idx + 1]] = skill[idx]  # 선행 스킬이 필요한 경우 직전 선행 스킬 담기

    for skill_tree in skill_trees:
        learned = {s: False for s in skill}  # 선행 스킬을 배웠는지의 여부
        is_failed = False  # 정답 여부를 판단하기 위한 flag
        for sk in skill_tree:
            if sk in before and not learned[before[sk]]:  # 선행 스킬이 필요한데 안 배운 경우
                is_failed = True  # Fail
                break
            learned[sk] = True

        if not is_failed:  # 모두 제대로 배웠으면
            answer += 1  # 정답

    return answer


def main() -> None:
    case1 = ["CBD", ["BACDE", "CBADF", "AECB", "BDA"]]

    print(solution(*case1))  # 2


main()
