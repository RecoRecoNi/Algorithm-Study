"""
풀이시간: 10분

<input>
- phone_book의 길이: 1 이상 1,000,000 이하
- 각 전화번호의 길이: 1 이상 20 이하
- 같은 전화번호가 중복해서 들어있지 않다.

<solution>
1) 정렬 후 현재 확인하고 있는 번호가 다음 번호의 접두어인지 확인하는 방법
2) 해시를 이용해 특정 전화번호의 접두어가 다른 번호인지 확인하는 방법

<시간 복잡도>
1) O(nlogn)
2) O(nm): n은 전화번호의 총 개수, m은 전화번호의 길이로 최대 20

<기타>
이 외에 트라이로도 풀이 가능
"""

from typing import List

# 정렬로 풀기
def solution(phone_book: List) -> bool:
    # 전화번호를 사전순으로 정렬
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # 다음 번호 비교 -> 접두어인지 확인
        if phone_book[i+1].startswith(phone_book[i]): # 접두어인 경우
            return False
    return True


# 해시로 풀기
def solution(phone_book: List) -> bool:
    phone_hash = {} # 전화번호 접두사를 저장할 해시

    # 각 전화번호의 접두사를 해시에 저장
    for number in phone_book:
        phone_hash[number] = True

    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_hash: # 접두어인 경우
                return False
    return True


# 테스트 케이스
test_case1 = ["119", "97674223", "1195524421"]     # 출력: False
test_case2 = ["123","456","789"]                   # 출력: True
test_case3 = ["12","123","1235","567","88"]        # 출력: False
test_case4 = ["456", "467"]                        # 출력: True
test_case5 = ["1195524421", "97674223", "119"]     # 출력: False

print(solution(phone_book=test_case5))