"""
    모음사전
    https://school.programmers.co.kr/learn/courses/30/lessons/84512

    풀이시간 
    20:50 ~ 20:30 (40분)
    
    문제 조건
    모음 5개를 5개 이하의 중복을 허용하여 단어 만들기 -> 3905개
    N = 3905

    시간 복잡도 : 
    O(N + NlogN + N) = O(모든 요소 생성 + 정렬 + 인덱스 탐색)
    O(NlogN)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 중복순열을 사용한 완전탐색

    - 중복순열로 가능한 모든 경우의 수를 생성
    - 생성된 사전 정렬
    - 인덱스 반환

    순열 : permutations
    중복순열 : product
    조합 : combinations
    중복조합 : combination_with_replacement

"""
from itertools import product

def solution(word):
    words = "AEIOU"
    bag = []
    
    # 중복 순열로 1,5개의 중복 순열 모두 구하기
    for r in range(1, 6):
        for item in product(words, repeat=r):
            bag.append("".join(item))
        
    # 데이터 사전 순 정렬
    bag_list = sorted(bag)

    # 인덱스 값 반환
    return bag_list.index(word) + 1