"""
[프로그래머스 - 표현 가능한 이진트리](https://school.programmers.co.kr/learn/courses/30/lessons/150367)
- 15분 정도 문제 이해에만 힘을 쏟았는데 이해가 안돼서 [정답](https://ddingmin00.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2023-KAKAO-BLIND-RECRUITMENT-%ED%91%9C%ED%98%84-%EA%B0%80%EB%8A%A5%ED%95%9C-%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC) 참고
- 문제 이해부터 풀이까지 다 너무 어려웠음..
"""

import math


def check(num_bin, prev_parent):
    """
    이진 트리를 만족하기 위해서는,
    자식 노드 위에 항상 부모 노드가 존재해야 함 => 이를 체크하는 함수
    """
    mid = len(num_bin) // 2  # 중앙값 기준으로 재귀적으로 확인

    if num_bin:
        son = num_bin[mid] == "1"
    else:  # 더 이상 확인할 노드가 없으면 True 반환
        return True

    if son and not prev_parent:  # 부모 노드가 없으면 False 반환
        return False
    else:  # mid 앞, 뒤에 대해 재귀적으로 check
        return check(num_bin[mid + 1 :], son) and check(num_bin[:mid], son)


def sol(num):
    if num == 1:  # 1은 항상 참
        return 1

    # 2진수 변환
    num_bin = bin(num)[2:]

    # 이진 포화트리에 맞게 자릿수를 맞춰줘야 함 => 2^n - 1 꼴의 자릿수를 가져야 함
    digit = 2 ** (int(math.log(len(num_bin), 2)) + 1) - 1
    num_bin = "0" * (digit - len(num_bin)) + num_bin  # 자릿수에 맞게 앞에 0을 채워줌

    # 누군가의 부모 노드는 항상 존재해야 함
    if num_bin[len(num_bin) // 2] == "1" and check(num_bin, True):
        return 1  # 존재하면 1
    else:
        return 0  # 존재하지 않으면 0


def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(sol(num))

    return answer
