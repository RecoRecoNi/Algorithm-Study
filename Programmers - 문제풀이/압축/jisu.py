'''
풀이 시작 : 2023-08-22 14:43

- 주어지는 문자열의 길이는 1000글자 이하이므로 문자열을 활용하는 로직은 O(N^2)까지 적용 가능
- 색인 번호를 담을 해시 테이블을 만들어서 관리
- 투 포인터(i, j)를 활용해서 색인을 참조할 문자열을 결정
    - 기준 문자(i) 부터 (사전에 있는 단어 + 다음 단어)가 없을 때까지 j를 증가시켜 사전에 있는 단어는 출력, 없는 단어는 등록을 반복하면 된다.

풀이 완료 : 2023-08-22 15:19
모레
'''

from typing import List, Dict

def solution(msg: str) -> List[int]:

    hash_table: Dict[str:int] = {ch:idx+1 for idx, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}   # 길이가 1인 모든 사전 단어 초기화
    answer: List[int] = []
    i: int = 0
    count: int = 26     # 현재 사전에 26개 초기화 되어 있음

    while i < len(msg):                                     # 기준 문자(i)가 문자열 순회를 마칠 때까지
        j=i+1                                                   # j는 i+1로 초기화 / 'apple'을 예시 'apple'[0:1] -> 'a'

        while j < len(msg) and msg[i:j+1] in hash_table:    # (사전에 있는 단어 + 다음 단어)가 사전에 없을 때까지
            j+=1                                                # 'apple'의 경우 'a'는 사전에 있고, 'ap' 는 사전에 없으므로 j는 2까지 증가

        answer.append(hash_table[msg[i:j]])                 # 사전에 있는 단어는 출력 / 'a'는 출력
        count += 1
        hash_table[msg[i:j+1]] = count                      # 사전에 없는 단어는 count 증가 시켜서 사전에 넣기  / 'ap'는 사전에 다음 색인 번호로 인덱싱해서 추가
        i=j                                                 # 출력 다음 부분부터 다시 탐색 시작

    return answer

def main() -> None:
    case1 = 'KAKAO'
    case2 = 'TOBEORNOTTOBEORTOBEORNOT'
    case3 = 'ABABABABABABABAB'

    print(solution(case1))      # [11, 1, 27, 15]
    print(solution(case2))      # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    print(solution(case3))      # [1, 2, 27, 29, 28, 31, 30]

main()