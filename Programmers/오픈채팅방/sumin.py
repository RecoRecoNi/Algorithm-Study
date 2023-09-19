"""
풀이시간: 13분

<input>
record: 채팅기록
- 길이는 1 이상 100,000이하
- [유저아이디]로 구분한다.

<solution>
로그와 유저 아이디를 별도로 저장해서 관리하면 된다.

<시간복잡도>
O(N): 최악의 경우 record의 길이
"""
from typing import List


def solution(record: List[str]):
    answer = [] # 최종적으로 방을 개설한 사람이 보게 되는 메시지 문자열 배열
    # [uid, 상태]
    log = []
    # 유저: uid
    user = {}
    for i in record:
        status, uid = i.split()[0], i.split()[1]
        log.append([uid, status])
        if len(i.split()) > 2: # Enter 또는 Change
            user[uid] = i.split()[2]

    for uid, status in log:
        if status == 'Enter':
            answer.append(f"{user[uid]}님이 들어왔습니다.")
        elif status == "Leave":
            answer.append(f"{user[uid]}님이 나갔습니다.")

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.6MB)
테스트 4 〉	통과 (0.06ms, 10.5MB)
테스트 5 〉	통과 (1.89ms, 10.8MB)
테스트 6 〉	통과 (1.23ms, 10.8MB)
테스트 7 〉	통과 (1.05ms, 10.7MB)
테스트 8 〉	통과 (2.12ms, 10.7MB)
테스트 9 〉	통과 (1.34ms, 10.9MB)
테스트 10 〉	통과 (2.16ms, 10.7MB)
테스트 11 〉	통과 (0.94ms, 10.4MB)
테스트 12 〉	통과 (0.97ms, 10.4MB)
테스트 13 〉	통과 (2.22ms, 10.7MB)
테스트 14 〉	통과 (1.34ms, 11.1MB)
테스트 15 〉	통과 (0.02ms, 10.5MB)
테스트 16 〉	통과 (0.02ms, 10.5MB)
테스트 17 〉	통과 (0.12ms, 10.7MB)
테스트 18 〉	통과 (0.12ms, 10.4MB)
테스트 19 〉	통과 (1.20ms, 10.8MB)
테스트 20 〉	통과 (1.26ms, 10.7MB)
테스트 21 〉	통과 (1.19ms, 10.8MB)
테스트 22 〉	통과 (1.19ms, 10.8MB)
테스트 23 〉	통과 (1.21ms, 11MB)
테스트 24 〉	통과 (1.21ms, 10.9MB)
테스트 25 〉	통과 (187.29ms, 49.2MB)
테스트 26 〉	통과 (179.17ms, 52.4MB)
테스트 27 〉	통과 (180.27ms, 55.8MB)
테스트 28 〉	통과 (183.44ms, 56.8MB)
테스트 29 〉	통과 (205.04ms, 56.8MB)
테스트 30 〉	통과 (150.41ms, 51.5MB)
테스트 31 〉	통과 (134.87ms, 52.7MB)
테스트 32 〉	통과 (156.41ms, 47.9MB)
"""