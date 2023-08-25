'''
풀이 시작 : 2023-08-03 16:50

- 던전 개수가 최대 8개이므로 뭔 짓을 해도 될듯
- 완전 탐색으로 접근해보자
- permutation으로 모든 순서를 정해서 탐험 가능한 던전 수를 모두 구하는 방식

풀이 완료 : 2023-08-03 17:12

##### 완전탐색 말고 그리디하게 풀 수는 없을까?
- 최소 피로도와 소모 피로도의 상관 관계를 생각해봤을 떄 그리디한 접근은 어려울 것 같음
- 여러 풀이들을 확인해봤지만 모든 케이스에서 성공한 그리디 풀이는 없었음
'''

from typing import List
from itertools import permutations

def solution(k:int, dungeons:List):
    max_result = 0

    all_cases = permutations(dungeons)              # 던전 탐험 순서의 모든 경우의 수
    for case in all_cases:                          # 하나씩 드가 봅시다
        cur_k = k
        num_of_clear = 0
        breakFlag = False

        for at_list, consumption in case:           # 하나의 케이스에서 각 던전 탐색
            if cur_k >= at_list:                        # 다음 던전 탐험이 가능한 경우 (현재 피로도가 던전 최소 피로도 이상인 경우)
                cur_k -= consumption                        # 피로도 차감해주고
                num_of_clear += 1                           # 클리어
            else:                                       # 다음 던전 탐험이 가능하지 않은 경우
                continue                                    # 다음 던전은 패스
        
            if max_result < num_of_clear:               # 탐험 가능 최대 던전 수 업데이트
                max_result = num_of_clear

    return max_result                               # 모든 경우에서 최대 던전 수 반환

def main():
    case1 = [80, [[80,20],[50,40],[30,10]]]	# 3
    print(solution(*case1))

main()