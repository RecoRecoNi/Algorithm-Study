"""
    전화번호 목록
    https://school.programmers.co.kr/learn/courses/30/lessons/42577

    풀이시간 
    23:35 ~ 24:01

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 문자열 내장 함수

    1~100만개의 번호중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인
    
    1. 컨텐츠를 길이 순으로 정렬 + 이중 For문을 사용하여 확인
    2. 숫자순으로 정렬 + startwith로 접두어를 검사
"""
from typing import List

# 1번
# def solution(phone_book: List[str]):
#     # phone book 길이 순으로 정렬
#     phone_book.sort(key=lambda x: len(x))

#     # 번호의 순서대로 확인하며 다음 번호부터 끝번까지 확인
#     for idx, num in enumerate(phone_book):
#         num_length = len(num)

#         for target in phone_book[idx + 1 :]:
#             if num == target[:num_length]:
#                 return False

#     return True


# 2번
def solution(phone_book: List[str]):
    # 숫자 순서로 정렬
    phone_book.sort()

    # 현재 인덱스와 다음 인덱스의 처음을 startswith를 통해 확인
    for idx in range(len(phone_book) - 1):
        if phone_book[idx + 1].startswith(phone_book[idx]):
            return False

    return True


# case1 = ["119", "97674223", "1195524421"]  # false
case1 = ["97674223", "1195524421", "119"]  # false
case2 = ["123", "456", "789"]  # true
case3 = ["12", "123", "1235", "567", "88"]  # false

print(solution(case1))
print(solution(case2))
print(solution(case3))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.00ms, 10.5MB)
# 테스트 3 〉	통과 (0.00ms, 10.4MB)
# 테스트 4 〉	통과 (0.00ms, 10.6MB)
# 테스트 5 〉	통과 (0.00ms, 10.5MB)
# 테스트 6 〉	통과 (0.00ms, 10.5MB)
# 테스트 7 〉	통과 (0.00ms, 10.5MB)
# 테스트 8 〉	통과 (0.00ms, 10.5MB)
# 테스트 9 〉	통과 (0.00ms, 10.4MB)
# 테스트 10 〉	통과 (0.00ms, 10.6MB)
# 테스트 11 〉	통과 (0.00ms, 10.6MB)
# 테스트 12 〉	통과 (0.00ms, 10.6MB)
# 테스트 13 〉	통과 (0.00ms, 10.6MB)
# 테스트 14 〉	통과 (0.37ms, 10.5MB)
# 테스트 15 〉	통과 (0.45ms, 10.6MB)
# 테스트 16 〉	통과 (0.51ms, 10.6MB)
# 테스트 17 〉	통과 (1.09ms, 10.6MB)
# 테스트 18 〉	통과 (0.92ms, 10.8MB)
# 테스트 19 〉	통과 (0.62ms, 10.7MB)
# 테스트 20 〉	통과 (1.12ms, 10.8MB)

# 효율성  테스트
# 테스트 1 〉	통과 (2.91ms, 11MB)
# 테스트 2 〉	통과 (2.61ms, 11.1MB)
# 테스트 3 〉	통과 (92.17ms, 31.1MB)
# 테스트 4 〉	통과 (89.16ms, 28.4MB)
