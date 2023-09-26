"""
    가장 긴 짝수 연속한 부분 수열 (large)
    https://www.acmicpc.net/problem/22862
    
    풀이시간
    21:53 ~ 22 : 50 (57분)

    문제조건
    1 <= N <= 1,000,000
    1 <= K <= 100,000
    1 <= x <= 10^6

    시간 복잡도
    O(N + K + N) : O(N)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? 시뮬레이션 + 최적화

    예외처리 : 만약 K가 N-1보다 크다면 모든 짝수를 가지는 부분 수열의 합과 같다.

    1. 연속된 짝수를 가지는 부분 수열의 원소 개수 구하기 O(N)
        1 2 3 4 5 6 7 8
        [0, 1, 1, 1, 1]

        1 2 3 4 5 5 6 8
        [0, 1, 1, 0, 2]

        2 4 6 8 8 6
        [6]

        2 1 3 2 4 8
        [1, 0, 3]

    2. K만큼 슬라이딩하며 데이터를 더해서 Max 값을 갱신 (리스트의 원소를 슬라이딩하는 과정을 최적화)

"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))


# 1. 연속된 짝수를 가지는 부분 수열의 원소 개수 구하기
even_number = [0]
for num in array:
    # 짝수라면 even_number 증가
    if num % 2 == 0:
        even_number[-1] += 1
    # 홀수라면 다음 even_number 부분 수열로 넘기기
    else:
        even_number.append(0)
# print(even_number)

# 예외처리 : 만약 K가 N-1보다 크다면 모든 짝수 갯수를 더한 갯수와 같다.
if N - 1 <= K:
    print(sum(even_number))

else:
    # 2. K만틈 슬라이딩하며 데이터 더해서 max값 갱신
    answer = value = sum(even_number[0:K+1])

    # 최적화 하기 전 (시간 초과)
    # for idx in range(len(even_number) - K):
    #     value = sum(even_number[idx: idx+(K+1)])
    #     if value > answer:
    #         answer = value

    # 슬라이딩 코드 최적화 후 (통과)
    for idx in range(len(even_number) - (K + 1)):
        value -= even_number[idx]
        value += even_number[idx+K+1]
        if value > answer:
            answer = value
    
    print(answer)


