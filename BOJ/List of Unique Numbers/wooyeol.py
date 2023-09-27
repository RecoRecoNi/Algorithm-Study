"""
    List of Unique Numbers
    https://www.acmicpc.net/problem/13144
    
    풀이시간
    23 : 02 ~ 23:24 / 23: 50 ~ 31 (풀이 실패)

    풀이 참고
    https://eunbin00.tistory.com/163

    문제조건
    1 <= N <= 100,000
    1 <= x <= 100,000

    시간 복잡도

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? 투 포인터

    각 요소를 하나씩 검사하며 중복이 발생하면 start 조정, 중복이 발생하지 않으면 start 조정

    1. End 위치의 값이 중복이 아닐 경우
        - End 위치의 값이 사용됨을 알리고
        - End를 증가시켜 다음 숫자 확인
        - 증가된 수열을 기준으로 가능한 부분 수열 갯수 추가하기 -> 어떻게 사람의 머리에서 이런게 나올 수 있죠...?
            ex) 5   
                1 2 3 1 2

                [1]
                1 - [1]

                [1, 2]
                2 - [2],[1,2]

                [1, 2, 3]
                3 - [3],[2,3][1,2,3]

                [2, 3, 1]
                3 - [1],[3,1],[2,3,1]

                [3, 1, 2]
                3 - [2],[1,2],[3,1,2]

                [1],[2],[3],[1],[2]
                [1,2][2,3],[3,1][1,2]
                [1,2,3],[2,3,1][3,1,2]


    2. End 위치의 값이 중복일 경우
        - Start 위치의 값을 사용되지 않음으로 알리고
        - Start를 증가시켜 범위 조정
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

answer = 0
num_dict = defaultdict(bool)

start, end = 0, 0

while start < N and end < N:
    # 1. End 위치의 값이 중복이 아닐 경우
    if not num_dict[array[end]]:
        # End 위치의 값이 사용됨을 알리고
        num_dict[array[end]] = True
        
        # 다음 숫자 확인
        end += 1

        # 증가된 수열을 기준으로 가능한 부분 수열 갯수 추가하기
        answer += (end - start)

    # 2. End 위치의 값이 중복일 경우
    else:
        # Start 위치의 값을 사용하지 않음을 알리고
        num_dict[array[start]] = False
        
        # start 기준 다음 값 확인
        start += 1

print(answer)