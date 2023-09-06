"""
풀이시간: 10분

<input>
진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
- n: 진법 (2 ≦ n ≦ 16)
- t: 미리 구할 숫자의 갯수 (0 ＜ t ≦ 1000)
- m: 게임에 참가하는 인원 (2 ≦ m ≦ 100)
- p: 튜브의 순서 (1 ≦ p ≦ m)

<solution>
1. 변환한 숫자를 모두 합친 문자열의 길이가 t * m가 될 때까지 순서대로 숫자를 n진수로 변환해 추가해준다.
2. 문자열을 순회하며 튜브의 순서가 되는 문자열을 ans에 추가한다.

<시간복잡도>
O(t*m)
"""

# number(10진수)를 base진수로 변환하는 함수
def convert(number: int, base: int) -> str:
    """
    number: 변환할 숫자(10진수)
    base: 변환할 진수
    """
    nums = '0123456789ABCDEF'
    q, r = divmod(number, base) # 몫, 나머지
    if q == 0:
        return nums[r]
    else:
        return convert(q, base) + nums[r]

def solution(n: int, t: int, m: int, p: int) -> str:
    """
    n: 변환할 진법
    t: 미리 구할 숫자의 개수
    m: 게임에 참가하는 인원
    p: 튜브의 순서
    """
    converted_nums = ''
    i = 0 # 숫자는 0부터 시작

    # 필요한 숫자를 미리 변환하여 converted_nums에 저장
    while len(converted_nums) < t * m:
        converted_nums += convert(i, n) # i를 n진수로 변환
        i += 1
    return converted_nums[p-1:t*m:m] # 튜브의 순서가 돌아올 때마다 출력

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.11ms, 10.1MB)
테스트 6 〉	통과 (0.12ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.2MB)
테스트 8 〉	통과 (0.12ms, 10MB)
테스트 9 〉	통과 (0.12ms, 10.1MB)
테스트 10 〉	통과 (0.12ms, 10.3MB)
테스트 11 〉	통과 (0.13ms, 10.1MB)
테스트 12 〉	통과 (0.13ms, 10.2MB)
테스트 13 〉	통과 (0.23ms, 10.2MB)
테스트 14 〉	통과 (25.40ms, 10.4MB)
테스트 15 〉	통과 (25.76ms, 10.4MB)
테스트 16 〉	통과 (24.76ms, 10.1MB)
테스트 17 〉	통과 (2.01ms, 10.1MB)
테스트 18 〉	통과 (1.22ms, 10.3MB)
테스트 19 〉	통과 (0.34ms, 10.2MB)
테스트 20 〉	통과 (1.03ms, 10MB)
테스트 21 〉	통과 (6.36ms, 10.1MB)
테스트 22 〉	통과 (2.70ms, 10.2MB)
테스트 23 〉	통과 (8.83ms, 10.2MB)
테스트 24 〉	통과 (13.03ms, 10.2MB)
테스트 25 〉	통과 (10.28ms, 10.3MB)
테스트 26 〉	통과 (4.47ms, 10.2MB)
"""