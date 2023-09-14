"""
    수 이어 쓰기 2
    https://www.acmicpc.net/problem/1790

    풀이시간
    21:59 ~ 22:49 22:55 ~ 24:16 (2시간 11분)
    
    문제 조건
    1 <= N <= 100,000,000
    1 <= K <= 100,000,000

    시간 복잡도 :
    O(9 * 9 + 9)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 수학

    1. 전체 N이 가질 수 있는 자리 수 확인
     - 주어진 N에 자리 수(min_square == 자리 수를 10의 승수로 표현) 확인 및 10**x을 뺀 남은 정수의 값(extra) 확인
     - 현재 N까지 숫자를 이어 붙였을 때 생기는 자리 수 확인
        - 실제 자리수 * (10**실제 자리수 - 10**(실제 자리수 - 1))의 누적합

    2. 만약 N의 최대 자리수 보다 k가 크다면 -1

    3. 아니라면 K를 real number로 변경해주고 해당 값의 몇 번째 자리의 숫자를 반환 하는지 확인

    ex) 
    5 5
    min_square : 0 , extra : 5
    k_to_number : 5
    5

    20 23
    min_square : 1 , extra : 11
    k_to_number : 16
    6

"""
import sys

input = sys.stdin.readline

N, k = map(int, input().split())

# 1. 전체 N이 가질 수 있는 자리 수 확인
## 주어진 N에 자릿수 확인 및 10**square를 제외하고 남은 정수의 갯수 반환
min_square, extra = -1, 0
for square in range(1, 10):
    if (10 ** square) > N:
        min_square = square - 1  # square 업데이트
        extra = N - (10 ** (min_square)) + 1  # 제외하고 남은 정수
        break

# print(f"min_square : {min_square} , extra : {extra}")

## 현재 N 숫자까지 이어붙였을 경우 생기는 자리 수
counts = 0
for m in range(min_square):
    counts += (m+1) * (10 ** (m+1) - 10 ** (m))
counts += (min_square+1) * extra

# 2. 만약 N의 최대 자리수 보다 k가 크다면 -1
if k > counts:
    print(-1)
    exit()

# 3. 아니라면 K를 real number로 변경해주고 해당 값의 몇 번째 자리의 숫자를 반환 하는지 확인
else:
    # 현재 누적합 자리와 이전까지의 누적합 자리
    counts_k, prev_counts_k = 0, 0
    for square in range(1, 10):
        # 누적합을 통한 10**x의 자리 수를 통해 나타낸 이어붙인 자리 수
        counts_k += square * (10 ** square - 10 ** (square-1))
        
        # k를 넘어서면
        if counts_k >= k:
            k -= prev_counts_k

            # k-1까지의 숫자와 x승수 divmod 진행 후 
            m, n = divmod(k-1, square)

            # 결과 값 생성
            k_to_number = 10**(square-1) + m # 이전 10 ** 승수에 몫만큼 더해주기

            # print("k_to_number :",k_to_number)

            # 나머지 인덱스에 있는 숫자 반환
            print(str(k_to_number)[n])
            break
        prev_counts_k = counts_k
