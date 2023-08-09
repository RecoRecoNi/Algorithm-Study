'''
풀이 시작 : 2023.08.09 13:03

- 순서를 바꾸지 않아도 된다 -> 덧셈 뺄셈 연산자만 바꿔가며 경우의 수를 판단
- 그리디한 접근은 어려울 것 같고(어차피 다 탐색해야함), 주어지는 수의 개수가 많지 않아서(20개) 완전탐색(dfs)으로 구현할 수 있을듯 함
- 모든 수를 순서대로 탐색해야하므로 가지 치기는 없고, 그냥 부호만 바꿔가며 가지를 뻗어나가기만 하면 될 것 같다.

풀이 완료 : 2023.08.09 13:22
'''

from typing import List


result = 0

def dfs(idx: int, numbers: List[int], target: int, total: int):
    global result

    if idx == len(numbers):                             # 모든 수의 탐색이 끝난 경우
        result += 1 if total == target else 0           # 해당 경우의 수의 결과가 target number이면 최종 결과에 +1
        return                                          # 이는 재귀의 종료 조건임
    
    dfs(idx+1, numbers, target, total+numbers[idx])     # idx번째를 더하고 idx+1번째 탐색 시작
    dfs(idx+1, numbers, target, total-numbers[idx])     # idx번째를 빼고 idx+1번째 탐색 시작


def solution(numbers: List[int], target: int) -> int:
    global result

    dfs(0, numbers, target, 0)      # 0번 인덱스부터 탐색 시작

    return result

def main() -> None:
    global result
    case1 = [[1, 1, 1, 1, 1], 3]    # 5
    case2 = [[4, 1, 2, 1], 2]       # 2

    print(solution(*case1))         # 5
    result = 0                      # 전역변수 초기화
    print(solution(*case2))         # 2

main()