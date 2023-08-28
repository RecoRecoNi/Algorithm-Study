'''
풀이 시작 : 2023.08.08 23:32 

- n층의 삼각형에서 숫자의 개수는 (2^n)-1 개이다. 
- 따라서 모든 경우의 수 중 최대값을 구하고자 하면 나올 수 있는 경우의 수는 ((2^n)-1)! -> 여기서 완전탐색으로 최대값을 찾기에는 너무 연산량이 많다.
- 가장자리에 있는 수들은 하나의 수가 더해지고, 안쪽의 수 들은 두 경우의 수 중 큰 경우의 수를 받을 것이다. 그러면 큰 경우만 받아서 저장하자(dp)
- 그러면 가장 마지막 층에서 가장 큰 원소만 구하면 거쳐간 숫자의 최대값을 구할 수 있다.
- 사실 dp 문제에서 많이 본 유형이었기 때문에 바로 떠올릴 수 있었다.

풀이 완료 : 2023.08.09 00:01
'''

from typing import List

def solution(triangle : List[List]) -> int:

    for row in range(1, len(triangle)):
        for col in range(row+1):                                                            # 한 row는 row개의 수를 가짐
            if col == 0:                                                                    # 좌측 가생이에 있는 수의 경우
                triangle[row][col] += triangle[row-1][col]                                      # 좌측 위 숫지(같은 col)
            elif col == row:                                                                # 우측 가생이에 있는 수의 경우
                triangle[row][col] += triangle[row-1][col-1]                                    # 우측 위 숫자(col-1)
            else:                                                                           # 그 외의 나머지 수의 경우
                triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])         # 좌측 위 숫자나 우측 위 숫자 중에 큰 거 더한 경우를 선택

    return max(triangle[-1])                                                                # 그러면 가장 마지막 층에서 가장 큰 원소가 거쳐간 숫자의 최대값이다.

def main():
    case1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
    case2 = [[7]] 
    case3 = [[7], [3, 8]]
    print(solution(case1)) # 30
    print(solution(case2)) # 7
    print(solution(case3)) # 15

main()