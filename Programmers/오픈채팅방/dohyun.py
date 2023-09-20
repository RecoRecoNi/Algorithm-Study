"""

풀이시간
- 약 15분

접근법
- N이 1만 -> O(N^2) ~ O(NlogN)
- 유저가 나중에 닉변하는 경우를 생각해서 결과를 순회할 때 배열에 저장하는 행위를 한번 해야함
- 고유 아이디는 그대로 -> 이거를 딕셔너리로 활용하자

회고
- 시간복잡도나 코드를 조금 더 간결하게 할 수 있을 것 같다는 생각
    - 여러분들의 코드를 잘 공부해보겠습니다!!

"""

from collections import defaultdict

def solution(records):
    users = defaultdict()
    answer = []

    for record in records:
        behavior, code, *user = record.split()
        
        if user: # 닉네임이 비어있지 않은 경우 닉네임 갱신(Leave 가 아닌 경우)
            users[code] = user # {유저의 고유 아이디 : 닉네임}
        
        if behavior == "Enter":
            answer.append([code, "님이 들어왔습니다."])
        elif behavior == "Leave":
            answer.append([code, "님이 나갔습니다."])

    for i in range(len(answer)):
        code, printer = answer[i]
        answer[i] = users[code][0] + printer # 유저의 고유 아이디를 닉네임으로 변경하며 완전한 문장형태로 변환
    
    return answer