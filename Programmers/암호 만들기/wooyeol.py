"""
    암호 만들기
    https://www.acmicpc.net/problem/1759

    풀이시간 
    10:52 ~ 11:43 (49분)
    
    문제 조건
    3 <= L <= C <= 15
    L개의 알파벳 소문자 (최소 한 개의 모음과 두 개의 자음)

    시간 복잡도 : O(L x C)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 백 트래킹

    - 주어진 알파벳을 정렬하고 방문한 알파벳은 표시를 해둔다.
    1. 백트래킹을 구현하며 Base Condition(길이가 L과 같고 모음의 갯수가 0보다 크고 자음의 갯수가 1보다 클 경우)일 경우만 값을 출력

    2. 백 트래킹을 위한 검사문들을 작성한다.
        1. 중복을 허용하지 않고 알파벳 사전순일 경우만 확인하기 때문에 현재 담겨있는 알파벳보다 더 큰 인덱스 값만 검사한다.
    
        2. 방문하지 않은 알파벳일 경우
            2-1. 현재 위치를 방문 처리하고 해당 값을 Password에 넣은 뒤 자음과 모음 갯수를 업데이트한다.
            2-2. 다음 자리 알파벳을 백 트래킹으로 찾는다.
            2-3. 탐색된 알파벳을 방문처리를 해제하고 자,모음 갯수를 다시 업데이트 한다.
"""

import sys
from typing import List, Set

global isused_vowel, isused_consonants

input = sys.stdin.readline

# Input
L, C = map(int, input().split())
characters: List[str] = input().split()

# 모음의 갯수
vowels: Set[str] = set(["a", "e", "i", "o", "u"])

# 방문한 알파벳 표시
isused: List[bool] = [False] * C

# 암호에 추가한 모음 과 자음의 갯수 확인
isused_vowel: int = 0  # 모음
isused_consonants: int = 0  # 자음

# 암호를 저장할 리스트
password: List[str] = []


# 알파벳 순으로 정렬
characters.sort()


def backtracking(length: int, max_idx: int):
    global isused_vowel, isused_consonants

    # Base Condition
    ## 길이가 L과 같고 모음의 갯수가 0보다 크고 자음의 갯수가 1보다 크다면 출력 후 리턴
    if length == L and isused_vowel > 0 and isused_consonants > 1:
        print("".join(password))
        return

    # max_idx의 값보다 큰 인덱스만 검사한다.
    for idx in range(max_idx, C):
        # 이미 방문한 알파벳이면 패스
        if isused[idx]:
            continue

        # 현재 위치를 방문 처리 후 암호에 해당 알파벳 추가하고 해당 알파벳이 모음인지 자음인지 카운트
        isused[idx] = True
        password.append(characters[idx])
        if characters[idx] in vowels:
            isused_vowel += 1
        else:
            isused_consonants += 1

        # 백 트래킹
        backtracking(length + 1, idx)

        # 현재 위치를 방문 처리에서 제외 후 암호에서 제거하고 해당 알파벳이 모음인지 자음인지 확인 후 갯수 감소
        isused[idx] = False
        if password.pop() in vowels:
            isused_vowel -= 1
        else:
            isused_consonants -= 1

    return


backtracking(0, 0)

# print(C)
