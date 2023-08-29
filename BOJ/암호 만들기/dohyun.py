"""

풀이시간
- 약 1시간 20분

접근법
- 알고리즘에 따라 사전 시간복잡도가 많이 달라질듯 함
- 최소 한 개의 모음 / 최소 두 개의 자음
    - 해당 조건을 잘 처리하는 것이 관건
    - 암호가 이미 존재하므로 최소 한 개의 모음과 두 개의 자음이 입력으로 주어지긴 할 것 -> 예외처리 할 필요 X
- 문자열의 조합 -> itertools 모듈을 잘 활용해보자
    - 걱정되는 것은 시간복잡도에 걸리지 않을까?
    - 최악의 경우인 15 에도 15C10(조합) = 3003 이므로 문제없을 듯 함
    - 정렬하는 과정이 많지만 최대 L (15이하) 길이의 정렬이므로 문제될 것 없음

회고
- 풀고나서 답을 보니 뭔가 운이 좋아서(?) 풀이가 가능했던 것 같은 기분 ...
- 물론 시간복잡도에 걸릴 것 같다는 생각이 들었다면 가능한 조합을 다 구하지는 않았겠지만, 그래도 정석적인 풀이(정형화 되어있는?)를 지향하기

"""

import sys
from itertools import combinations

inputs = sys.stdin.readline
L, C = map(int, inputs().split())
texts = inputs().split()

gathers = [] # 모음
consonants = [] # 자음

# 모음과 자음을 각각 분리하는 과정
for text in texts:
    if text in ["a", "e", "i", "o", "u"]:
        gathers.append(text)
    else:
        consonants.append(text)

answer = []

gathers_comb = []
consonants_comb = []
for i in range(1, len(gathers) + 1): # 모음은 무조건 1개부터 시작하도록 고정 -> 점차 늘려나감
    if L-i < 2: # 만약 자음이 2개 이상이 채워지지 못하면 경우의수 구하는 과정 종료
        break
    else:
        gathers_comb.append(list(combinations(gathers, i))) # 모음의 개수만큼 알파벳 배열 생성
        consonants_comb.append(list(combinations(consonants, L-i))) # 자음의 개수만큼 알파벳 배열 생성

answer = []
for gather_comb, consonant_comb in zip(gathers_comb, consonants_comb): # 모음 배열과 자음 배열 불러옴
    for gather in gather_comb:
        for consonant in consonant_comb:
            password = sorted(list(gather) + list(consonant)) # 모음과 자음을 조합하여 암호 생성 (리스트 형태)
            password = "".join(password) # 리스트 형태의 암호를 문자열로 변경
            answer.append(password)

answer.sort() # 배열 정렬
for ans in answer:
    print(ans)