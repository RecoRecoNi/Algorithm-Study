'''
풀이 시작 : 2023-08-20 12:49

N은 1,000,000 이하이므로 O(NlogN)안에 해결해야한다.

phone_book에 대해 정렬을 수행하면 아스키 코드 순 -> 짧은 순으로 정렬이 되므로,
만약 한 번호가 다른 번호의 접두어라면, i-1번째 인덱스의 번호가 i번째 번호의 접두어일 것이다.

풀이 완료 : 2023-08-20 13:00 (풀이 시간 : 11분)
'''
from typing import List

def solution(phone_book: List[str]) -> bool:
    phone_book.sort()                                   # 맨 앞 글자의 아스키 코드 오름차순 -> 짧은 순으로 정렬
    for i in range(1, len(phone_book)):                 # 만약 한 번호가 다른 번호의 접두어라면,
        if phone_book[i].startswith(phone_book[i-1]):   # i-1번째 인덱스의 번호가 i번째 번호의 접두어일 것이다.
            return False
        
    return True

def main() -> None:
    case1 = ["119", "97674223", "1195524421"]       
    case2 = ["123","456","789"]
    case3 = ["12","123","1235","567","88"]

    print(solution(case1))  # false
    print(solution(case2))  # true
    print(solution(case3))  # false

main()