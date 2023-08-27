"""
    압축
    https://school.programmers.co.kr/learn/courses/30/lessons/17684

    풀이시간 22:30 ~ 23:00 | 23:53 ~ 00:27 (1시간 4분)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 구현

    1. W(현재 입력) 값을 찾기
        - 가장 긴 사전에 있는 문자열 w를 찾기
    2. 가장 긴 W의 사전 인덱스 값을 answer에 삽입
    3. W+C를 사전에 등록하기
    
"""
from typing import List


def solution(msg: str):
    answer: List = []

    msg_len: int = len(msg)
    cur: int = 0
    last_index: int = 26

    # 사전 구현
    bag = {chr(65 + code): code + 1 for code in range(26)}

    while cur < msg_len:
        # 1. w(현재 입력)가정 값을 지정
        w = msg[cur]

        # 1. 가장 긴 문자열 w를 찾기
        while cur + 1 < msg_len and w + msg[cur + 1] in bag:
            w += msg[cur + 1]
            cur += 1
            # print("2 : ", w)

        # 2. 가장 긴 W의 사전 인덱스 값을 answer에 삽입
        answer.append(bag[w])

        # 3. 사전에 w+c를 등록
        if cur + 1 < msg_len and w + msg[cur + 1] not in bag:
            last_index += 1
            bag[w + msg[cur + 1]] = last_index

        cur += 1

    return answer


case1 = "KAKAO"
case2 = "TOBEORNOTTOBEORTOBEORNOT"
case3 = "ABABABABABABABAB"

print(solution(case1))
print(solution(case2))
print(solution(case3))
