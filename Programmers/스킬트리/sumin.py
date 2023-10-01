"""
풀이시간: 30분

<input>
skill: 선행 스킬 순서(알파벳 대문자)
- 1이상 26이하로 중복해서 주어지지 않음

스킬트리: 유저들이 만든 스킬트리
- 1 이상 20이하인 배열
- 각 원소는 길이가 2 이상 26인 문자열로, 스킬은 중복해서 주어지지 않음

<solution>
skill_tree를 하나씩 순회하며 해당 스킬트리가 가능한지 확인한다.
1) skill_tree의 스킬을 하나씩 확인하면서 선행스킬에 포함되는 스킬만 뽑아 문자열로 만든다.
2) 위에서 만든 스킬 문자열이 선행 스킬의 순서에 해당되는지 확인한다.
- 여기서 선행스킬에 해당되는게 하나도 없을 때도 카운트 돼야한다. (이 부분을 놓쳐서 오래걸림..)
- ex) skill = "CBD", skill_trees = ["AF"] -> 1

<시간복잡도>
O(len(skill_trees) * len(skill_tree))
최대 연산횟수는 20 * 26 = 520
"""
from typing import List


def solution(skill: str, skill_trees: List[str]) -> int:
    answer = 0 # 가능한 스킬트리 개수

    for skill_tree in skill_trees: # 최대 20개
        skill_name = ''.join(map(str, [s for s in skill_tree if s in skill]))

        if not skill_name or (skill_name[0] == skill[0] and skill_name in skill):
            answer += 1

    return answer


"""
테스트 1 〉	통과 (0.01ms, 10.5MB)
테스트 2 〉	통과 (0.01ms, 10.5MB)
테스트 3 〉	통과 (0.01ms, 10.7MB)
테스트 4 〉	통과 (0.01ms, 10.5MB)
테스트 5 〉	통과 (0.02ms, 10.6MB)
테스트 6 〉	통과 (0.01ms, 10.7MB)
테스트 7 〉	통과 (0.02ms, 10.5MB)
테스트 8 〉	통과 (0.01ms, 10.6MB)
테스트 9 〉	통과 (0.03ms, 10.5MB)
테스트 10 〉	통과 (0.03ms, 10.5MB)
테스트 11 〉	통과 (0.02ms, 10.5MB)
테스트 12 〉	통과 (0.02ms, 10.6MB)
테스트 13 〉	통과 (0.02ms, 10.5MB)
테스트 14 〉	통과 (0.01ms, 10.7MB)
"""