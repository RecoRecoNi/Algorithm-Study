"""
    스킬트리
    https://school.programmers.co.kr/learn/courses/30/lessons/49993

    풀이시간 
    10:23 ~ 10:39 (16분)
    
    문제 조건
    1 <= len(skill) <= 26
    1 <= len(skill_trees) <= 20
    2 <= 각 skill_trees의 길이 <= 26

    시간 복잡도 : 
    O(20 * 26)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 완전 탐색

    데이터의 중복과 갯수가 크게 문제 되지 않기 때문에 완전 탐색으로 단순 구현을 진행하였습니다.

    완전 탐색 과정
    각각의 스킬트리 과정을 확인합니다.
    - 선행 스킬의 인덱스를 증가시키며 선행 스킬이 순서대로 주어지는지 확인하기
        - 스킬트리의 스킬을 하나씩 확인하고 선행 스킬에 포함된다면 등장해야하는 선행 스킬과 비교
            - 정상일 경우 다음 선행 스킬의 인덱스로 증가
            - 아니라면 인터럽트
        - 인터럽트가 일어나지 않은 스킬트리는 정답으로 인정
"""

def solution(skill, skill_trees):
    answer = 0

    # 선행 스킬의 Set화
    set_skill = set(skill)

    # 선행 스킬의 List화
    skill = list(skill)
    
    # 주어진 모든 스킬트리 검사
    for skill_tree in skill_trees:
        # 현재 검사해야하는 선행 스킬의 인덱스
        skill_idx = 0

        # 정상적으로 검사가 종료되었는지 Interrupt 여부 확인
        interrupt = False

        # 현재 스킬트리의 스킬을 하나씩 검사
        for alpha in skill_tree:
            # 현재 스킬트리의 스킬이 선행 스킬 내부에 존재하고
            if alpha in set_skill:
                # 현재 검사해야하는 선행 스킬의 인덱스를 가지는 스킬과 같다면 정상
                if alpha == skill[skill_idx]:
                    # 다음 선행 스킬을 검사합니다.
                    skill_idx += 1

                # 만약 다르다면 비정상 인터럽트
                else:
                    interrupt = True
                    break
        
        # 인터럽트가 진행되지 않았다면 정상적으로 검사 완료
        if not interrupt:
            answer += 1
    
    return answer