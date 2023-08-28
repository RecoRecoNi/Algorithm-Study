"""
다음 순열(next_permutation)을 이용한 풀이
- 풀이시간: 20분
- 시간복잡도: O(N! * N * N) -> 최대 2,580,480번 연산으로 시간 내에 통과가능
    1. 전체 순열을 구하는 부분: O(N! * N)
    2. 각 순열에 대해 던전을 탐험하는 부분: O(N)
"""
from typing import List

# 다음 순열로 풀기
def next_permutation(a): # 순열 a를 계속 변경
    i = len(a) - 1 # 뒤에서부터
    # 1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다 -> 가장 긴 감소수열
    while i > 0 and a[i-1] >= a[i]: # 마지막 수열
        i -= 1
    if i <= 0: # 0번째 index까지 확인한 경우(내림차순)
        return False # 다음 순열이 없음(마지막 순열)
    j = len(a)-1
    # 2. j >= i 이면서 a[j] > [i-1]를 만족하는 가장 큰 j를 찾는다
    while a[j] <= a[i-1]:
        j -= 1
    # 3. a[i-1]과 a[j]를 swap
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    # 4. A[i]부터 순열을 뒤집는다.
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True # 다음 순열이 있음


def solution(k:int, dungeons:List) -> int:
    answer: int = -1  # 유저가 탐험할 수 있는 최대 던전 수
    n = len(dungeons)
    a = list(range(n))
    while True: # 모든 순열 구하기
        cnt = 0
        now = k
        for i in a:
            need, use = dungeons[i]
            if now >= need:
                cnt += 1
                now -= use
        if cnt > answer:
            answer = cnt
        if not next_permutation(a): # 다음 순열이 없다면 종료
            break
    return answer

"""
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.14ms, 10.2MB)
테스트 4 〉	통과 (0.16ms, 10.2MB)
테스트 5 〉	통과 (0.91ms, 10.4MB)
테스트 6 〉	통과 (6.38ms, 10.3MB)
테스트 7 〉	통과 (58.50ms, 10.2MB)
테스트 8 〉	통과 (57.08ms, 10.2MB)
테스트 9 〉	통과 (0.14ms, 10.3MB)
테스트 10 〉통과 (6.22ms, 10.4MB)
테스트 11 〉통과 (0.03ms, 10.3MB)
테스트 12 〉통과 (51.09ms, 10.3MB)
테스트 13 〉통과 (63.14ms, 10.3MB)
테스트 14 〉통과 (47.68ms, 10.3MB)
테스트 15 〉통과 (60.85ms, 10.4MB)
테스트 16 〉통과 (5.84ms, 10.4MB)
테스트 17 〉통과 (50.85ms, 10.2MB)
테스트 18 〉통과 (0.03ms, 10.4MB)
테스트 19 〉통과 (0.26ms, 10.3MB)
"""