"""
    오픈채팅방
    https://school.programmers.co.kr/learn/courses/30/lessons/42888

    풀이시간 
    20 : 48 ~ 21 : 03 (15분)

    문제 조건
    1 <= record(R) <= 100,000

    시간 복잡도 : 
    O(R + R) = O(R)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 시뮬레이션

    - 문제 내용에 따라 uid 저장 테이블과 들어오고 나올 때를 records에 기록하여 최종적 변경된 닉네임으로 채팅 서비스 기록 남기기

"""
def solution(record):
    answer = []

    # uid와 닉네임 테이블 정의
    table = dict()

    # 입장/퇴장 기록 추가
    records = []
    
    for data in record:
        # 기록 분리
        oper, *args = data.split()

        # uid 와 name 파싱
        uid = args[0]
        if len(args) > 1:
            name = args[1] 

        # 명령에 따라 처리
        if oper == "Enter":
            # 입장시 테이블에 이름 추가 및 입장 기록 남기기
            table[uid] = name
            records.append((True, uid))
        
        elif oper == "Leave":
            # 퇴장시 기록에 퇴장 기록 남기기
            records.append((False, uid))

        elif oper == "Change":
            # 닉네임 변경하기
            table[uid] = name

    # 기록에 따라 변경된 닉네임으로 채팅기록 남기기
    for sign, uid in records:
        if sign:
            sentence = f"{table[uid]}님이 들어왔습니다."
        else:
            sentence = f"{table[uid]}님이 나갔습니다."
        answer.append(sentence)

    return answer

case1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(case1))