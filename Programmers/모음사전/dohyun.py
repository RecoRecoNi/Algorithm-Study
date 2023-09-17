"""

풀이시간
- 약 30분 소요

접근법
- word 의 길이가 5 이하이고 모음으로만 이루어져있기 때문에 경우의 수가 많이 안나올것같음
    - 우선 모든 조합을 구한다음 전체 경우의수를 구해보자
    - 중복을 허용하고 순서가 존재하는 경우의수 -> 중복순열
- 전체 경우의 수는 3905 -> 그냥 다 구하고 index 로 접근해도 문제 없음
- 모음 사전의 구성 원리를 잘 이해 못하겠음 -> 그냥 정렬해봤는데 이런 느낌이 맞는듯?!

회고
- 규칙을 찾아서 풀어내는 문제 같은데 모음 사전 구성 원리 자체를 이해 못해서 경우의 수를 직접 따져볼 수 없었음

"""

from itertools import product

def solution(word):
    vowel_dict = []
    for i in range(1, 6): # 단어 길이별 중복순열 계산
        for w in product("AEIOU", repeat=i):
            vowel_dict.append("".join(w)) # 튜플형태로 저장하면 길이가 너무 길기 때문에 문자열로 변환하여 저장

    vowel_dict.sort() # 모음사전 순서대로 정렬
    return vowel_dict.index(word) + 1 # 인덱스가 아닌 "번째" 이므로 1 더해줌