"""
풀이 시작 : 2023-09-03 23:00

- 10진수를 n진수로 변환하는 함수 정의
    - 최대 16진수까지 변환할 수 있으므로 알파벳 F까지 추가하는 로직 구현해야 함
- 문자열의 길이가 (m*t)이 될 때까지 n진수 이어 붙이기
    - 튜브 순서가 t번 돌 수 있을 때까지
- 튜브의 순서대로 문자 출력 [::p], 개수 오버하는 경우 t개까지만 출력

풀이 완료 : 2023-09-03 23:20 (20분 소요)

"""


def de2n(num: int, base: int) -> str:
    """
    n을 base진수로 변환하는 메서드
    이 떄 base는 최대 16이다.
    """
    if num == 0:
        return "0"

    result = ""

    while num > 0:
        rem = num % base
        num //= base

        if rem == 15:  # 최대 16진수 알파벳 처리 로직
            result += "F"
        elif rem == 14:
            result += "E"
        elif rem == 13:
            result += "D"
        elif rem == 12:
            result += "C"
        elif rem == 11:
            result += "B"
        elif rem == 10:
            result += "A"
        else:
            result += str(rem)

    return result[::-1]


def solution(n: int, t: int, m: int, p: int) -> str:
    """
    n : 변환할 진수
    t : 미리 구할 숫자의 갯수
    m : 게임에 참가하는 인원
    p : 튜브의 순서
    """
    tmp = ""
    num = 0
    while len(tmp) < (m * t):  # 튜브 순서가 t번 돌 수 있을 때까지
        tmp += de2n(num, n)  # n진수로 변환하여 이어붙임
        num += 1
    return tmp[p - 1 :: m][:t]  # 오버하는 경우 t개까지만 출력


def main() -> None:
    case1 = [2, 4, 2, 1]
    case2 = [16, 16, 2, 1]
    case3 = [16, 16, 2, 2]

    print(solution(*case1))  # "0111"
    print(solution(*case2))  # "02468ACE11111111"
    print(solution(*case3))  # "13579BDF01234567"


main()
