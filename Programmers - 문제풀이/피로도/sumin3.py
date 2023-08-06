"""
# 백트래킹(재귀)을 이용한 풀이
- 풀이시간: 15분
- 시간복잡도: O(2 ** N) -> 최대 256번 연산으로 시간 내에 통과가능
    - 던전의 개수를 n이라고 하면, 각 던전에 대해서 선택/비선택의 2가지 경우가 있기 때문.
"""
from typing import List

answer = 0
n = 0
visited = []


def go(k:int, cnt:int, dungeons:List) -> None:
    global answer
    if cnt > answer: # 방문할 수 있는 던전의 개수가 이전까지보다 더 많다면 갱신
        answer = cnt

    for i in range(n):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True # 방문처리
            go(k - dungeons[i][1], cnt+1, dungeons) # 현재 피로도 - 소모 피로도
            visited[i] = False # 백트래킹

def solution(k:int, dungeons:List) -> int:
    global n, visited
    n = len(dungeons) # 던전의 개수
    visited = [False] * n # 던전 방문처리 배열
    go(k, 0, dungeons)
    return answer


"""
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.28ms, 10.3MB)
테스트 5 〉	통과 (1.08ms, 10.2MB)
테스트 6 〉	통과 (2.82ms, 10.2MB)
테스트 7 〉	통과 (17.61ms, 10.1MB)
테스트 8 〉	통과 (47.09ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉통과 (0.99ms, 10.3MB)
테스트 11 〉통과 (0.01ms, 10.2MB)
테스트 12 〉통과 (2.13ms, 10.3MB)
테스트 13 〉통과 (0.26ms, 10.2MB)
테스트 14 〉통과 (0.09ms, 10.2MB)
테스트 15 〉통과 (0.04ms, 10.2MB)
테스트 16 〉통과 (0.04ms, 10.2MB)
테스트 17 〉통과 (0.10ms, 10.2MB)
테스트 18 〉통과 (0.02ms, 10.2MB)
테스트 19 〉통과 (0.08ms, 10.3MB)
"""


