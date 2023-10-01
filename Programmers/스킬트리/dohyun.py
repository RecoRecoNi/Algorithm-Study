"""

풀이시간
- 약 15분

접근법
- 시간복잡도 충분
- 선행 스킬이 필요함 -> 큐로 구현 가능!

회고
- 시간복잡도를 고려할 필요가 없었기 떄문에 비교적 수월하게 풀이
- 스택으로도 풀 수 있을것 같긴한데 큐가 선행스킬을 먼저 찍는다는 점에서 직관적으로 다가왔음
- 예외 케이스(25 라인)의 경우 조금 더 최적화 해낼 수 있을듯함
    - 여러분들의 코드를 열심히 공부하겠습니다!!!

"""

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        queue = deque(skill)
        uncommon_skills = set(skill) - set(skill_tree) # 선행 스킬루트에는 있지만 스킬트리에 해당 스킬을 사용하지 않는 경우
        
        for each_skill in skill_tree:
            if each_skill == queue[0]: # 큐의 첫번째 스킬(선행되어야 하는 스킬) 과 스킬트리의 순서가 일치하는 경우
                queue.popleft() # 선행스킬을 마스터한 것으로 판단
                if not queue: # 큐가 비었을 떄 중지
                    break

        if uncommon_skills == set(queue): # 선행스킬을 모두 제대로 사용했을 경우 or 큐에 남아있는 스킬이 사용하지 않는 스킬인 경우
            answer += 1

    return answer