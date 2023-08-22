'''
풀이 시작 : 2023-08-18 11:03

N은 3^k 꼴로 주어짐

3^k * 3^k 를 순회하여 모두 같은 수인지 확인 -> 같다면 해당 수 종이 += 1
                                    -> 같지 않다면 9등분 -> 3^(k-1) * 3^(k-1) 를 순회하며 반복
                                        -> 이전 문제와 마찬가지로 각 영역에 해당하는 인덕스를 적절하게 조절하여 재귀해줘야 함
풀이 완료 : 2023-08-18 11:45 (풀이 소요 시간 : 42분)

'''
import sys
from typing import List, Dict

input = sys.stdin.readline

def solution() -> None:
    solutionDict:Dict[int, int]  = {-1:0, 0:0, 1:0} # 각 종이의 수를 담을 dict
    N: int = int(input())
    matrix: List[List[int]] = [list(map(int, input().rstrip().split())) for _ in range(N)]
    k: int = 0

    while N % 3 == 0:       # k 구하기
        k+=1
        N//=3
    
    def recur(k, rStart, rEnd, cStart, cEnd):       # 재귀함수, row의 시작과 끝, col의 시작과 끝을 인자로 받음
                                                    # 9등분 한 각각의 영역을 독립적으로 생각하기 위함
        initValue: int = matrix[rStart][cStart]              # 한 영역이 전부 같은 수임을 판별하기 위한 변수

        for r in range(rStart, rEnd):
            for c in range(cStart, cEnd):
                if matrix[r][c] != initValue:               # 해당 영역이 하나라도 같지 않으면 9등분
                    # k가 2(N=9)라고 생각해보면 r과 c가 각각 (0~2, 3~5, 6~8)인 9 영역으로 나뉘어야 함
                    for rDiv3 in range(rStart, rEnd, 3**(k-1)):  
                        for cDiv3 in range(cStart, cEnd, 3**(k-1)): 
                            recur(k-1, rDiv3, rDiv3+3**(k-1), cDiv3, cDiv3+3**(k-1))
                    return

        solutionDict[matrix[rStart][cStart]] += 1    # 전부 같은 수이면 초기값에 해당하는 종이가 한 장

    recur(k, 0, 3**k, 0, 3**k)
    
    for answer in solutionDict.values():
        print(answer)

solution()