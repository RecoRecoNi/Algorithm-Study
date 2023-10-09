"""
풀이시간: 20분

<input>
files: 파일명(100글자 이내, 영문 대소문자, 숫자, 공백, 마침표, 빼기 부호만으로 이루어져있음), 1000개 이하의 파일
- 영문자로 시작하며, 숫자를 하나 이상 포함
- HEAD: 최소 한 글자 이상의 문자
- NUMBER: 한 글자에서 최대 다섯글자 사이의 연속된 숫자(앞쪽에 0이 올 수 있음. 0~9999 사이의 숫자)
- TAIL: 숫자가 다시 나타날 수도, 아무 글자도 없을 수도 있다.

<solution>
head, number, tail을 나눠주고 정렬

<시간복잡도>
O(1000 * 100): files의 크기 * file의 최대 길이

<회고>
head, number, tail을 일일히 나눠서 구현했는데..
다른 사람들 풀이를 보니 정규표현식으로 아주 깔끔하게 구현한 걸 확인..

[정규표현식 풀이]
정규표현식으로 구현할 때, number를 먼저 정렬하고, head를 정렬한다. 순서가 바뀌는 점 주의!
또, 파이썬 정렬에서 ['123', '0123']의 각 원소를 int로 변환해 정렬한다 했을 때, 같은 값이라면 순서도 유지된다는 걸 처음 알았음..
"""
from typing import List


def solution(files: List[str]) -> List[str]:
    answer = [] # 정렬된 파일명

    for idx, file in enumerate(files):
        head, number, tail = '', '', ''
        # head, number, tail로 나누기
        for x in file:
            # 1) head는 숫자가 아닌 문자
            if not number and not x.isdigit():
                head += x
            # 2) number는 숫자
            elif not tail and x.isdigit():
                number += x
            # 3) tail은 그 외 나머지 부분(숫자가 다시 나타날 수도, 아무 글자도 없을 수도 있음)
            elif head and number:
                tail += x

        answer.append((head, number, tail, idx))
        # 1. head 사전 순 정렬 -> 2. number의 숫자순으로 정렬 -> 3. 원래 입력에 주어진 순서로 정렬
        answer.sort(key=lambda f: [f[0].lower(), int(f[1]), f[-1]])

    # map과 lambda 함수를 사용해 각 튜플을 연결된 문자열로 변환
    answer = list(map(lambda file: ''.join(map(str, file[:-1])), answer))
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.7MB)
테스트 2 〉	통과 (0.05ms, 10.7MB)
테스트 3 〉	통과 (199.79ms, 11.1MB)
테스트 4 〉	통과 (219.57ms, 11.4MB)
테스트 5 〉	통과 (222.30ms, 11.2MB)
테스트 6 〉	통과 (190.55ms, 11.2MB)
테스트 7 〉	통과 (241.18ms, 11.1MB)
테스트 8 〉	통과 (202.50ms, 11.2MB)
테스트 9 〉	통과 (162.69ms, 11.1MB)
테스트 10 〉	통과 (165.78ms, 11.1MB)
테스트 11 〉	통과 (189.86ms, 11.3MB)
테스트 12 〉	통과 (202.04ms, 11.2MB)
테스트 13 〉	통과 (193.55ms, 11.1MB)
테스트 14 〉	통과 (213.60ms, 11.3MB)
테스트 15 〉	통과 (268.70ms, 11.2MB)
테스트 16 〉	통과 (184.06ms, 11.2MB)
테스트 17 〉	통과 (191.54ms, 11MB)
테스트 18 〉	통과 (187.65ms, 11MB)
테스트 19 〉	통과 (186.75ms, 11MB)
테스트 20 〉	통과 (186.83ms, 11.3MB)
"""



# 정규표현식 풀이
import re


def solution(files):
    # number 정렬 후 head를 정렬해야 한다.
    files = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    files = sorted(files, key=lambda file: re.split('\d+', file.lower())[0])
    return files

"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.4MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (3.12ms, 10.5MB)
테스트 4 〉	통과 (5.10ms, 10.4MB)
테스트 5 〉	통과 (2.76ms, 10.5MB)
테스트 6 〉	통과 (2.58ms, 10.4MB)
테스트 7 〉	통과 (3.96ms, 10.5MB)
테스트 8 〉	통과 (2.36ms, 10.6MB)
테스트 9 〉	통과 (2.39ms, 10.4MB)
테스트 10 〉	통과 (3.13ms, 10.4MB)
테스트 11 〉	통과 (2.56ms, 10.4MB)
테스트 12 〉	통과 (2.75ms, 10.4MB)
테스트 13 〉	통과 (2.66ms, 10.5MB)
테스트 14 〉	통과 (3.72ms, 10.6MB)
테스트 15 〉	통과 (3.68ms, 10.4MB)
테스트 16 〉	통과 (2.44ms, 10.4MB)
테스트 17 〉	통과 (2.47ms, 10.5MB)
테스트 18 〉	통과 (2.57ms, 10.5MB)
테스트 19 〉	통과 (2.72ms, 10.5MB)
테스트 20 〉	통과 (2.92ms, 10.3MB)
"""