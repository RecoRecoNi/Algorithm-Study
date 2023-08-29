'''
풀이 시작 : 2023-08-29 10:50

3 <= L <= C <= 15 이므로 N! 이전 알고리즘까지는 가능할 것 같다.

- 암호가 알파벳의 오름차순으로 배열되어있을 것 -> 갖고 있는 알파벳 리스트 정렬
- 이후 순서대로 인덱스 C까지 순회하며, 알파벳을 가져가는 경우, 안가져가는 경우로 분기(재귀)
- 이때 자음 모음 개수를 관리해야 하는데, 매번 길이가 L이 될 때마다 문자을열 탐색하는 것은 비효율 적이라고 판단 -> 매개변수로 관리
    - 자음(모음)이 추가될 경우 자음(모음)) 매개변수 +1,
    - 최종적으로 C까지 순회를 마치고 길이가 L인 password에 대해서 자음&모음 개수를 만족하는 패스워드를 출력

풀이 완료 : 2023-08-29 11:15 (풀이 시간 : 25분)
'''


import sys
from typing import List

input = sys.stdin.readline

def recur(idx:int, password: str, n_consonant: int, n_vowel: int) -> None:
    '''
    idx를 0 to C 까지 순회하여 alpha_list[idx]를 password에 포함하는 경우, 포함하지 않는 경우로 분기(재귀)한다.
    C까지 순회를 마쳤을 때 길이가 L인 패스워드에 대해서 자음&모음 조건을 만족하면 출력한다. 
    '''
    if idx == C:
        if len(password)==L and n_consonant >= 2 and n_vowel >= 1:          # 순회를 마쳤을 때 조건을 만족하면
            print(password)                                                 # 출력한다.
        return
                                                                            # idx번째 알파벳을 포함하는 경우
    if alpha_list[idx] in {'a', 'e', 'i', 'o', 'u'}:                            # 모음이면
        recur(idx+1, password+alpha_list[idx], n_consonant, n_vowel+1)              # 모음 카운트 증가시켜 재귀
    else:                                                                       # 자음이면
        recur(idx+1, password+alpha_list[idx], n_consonant+1, n_vowel)              # 자음 카운트 증가시켜 재귀
        
    recur(idx+1, password, n_consonant, n_vowel)                            # idx번째 알파벳을 포함하지 않는 경우

L, C = map(int, input().rstrip().split())
alpha_list: List[str] = sorted(input().rstrip().split())                    # 암호는 오름차순이므로 정렬 후 탐색
recur(0, '', 0, 0)

