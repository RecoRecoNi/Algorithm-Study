"""
1시간 정도 소요
[제한조건]
5 <= len(sequence) <= 1,000,000
1 <= sequence <= 1,000
5 <= k <= 1,000,000,000

[idea]
0, 1, 2, ... i 번째 원소부터 누적합을 구한 후, 누적합이 k인 경우 찾기
이 때 기본 오름차순으로 정렬되어 있으므로 누적합은 항상 증가하는 방향이다.
또한 오름차순인 것에 힌트, 누적합이 k인 경우를 찾을 때 이진 탐색을 활용할 수 있다.

[누적합 활용]
sequence의 각 원소를 해당 원소까지의 누적 합으로 업데이트 한 후, i번째 원소 전까지의 누적합을 빼어
i번째부터의 누적합을 활용할 수 있다.

[이진 탐색]
i번째 인덱스 부터의 인덱스를 활용할 수 있다면, 오름차순으로 정렬되어있음을 활용해 이진 탐색을 적용할 수 있다.
"""

def solution1(sequence : list, k : int) -> list:            # 시간 초과 케이스 O(N * N/2)
    nums : list = [0 for _ in range(len(sequence))]
    interval = 999999
    answer = None

    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            nums[i] += sequence[j]
            if nums[i] == k:
                if j-i < interval:
                    answer = [i, j]
                    interval = j-i
            if nums[i] > k:
                break

    return answer


def solution(sequence : list, k : int) -> list:     # 이진 탐색을 적용, O(NlogN)
    
    interval = 1000000                              # 최대 interval은 1000000
    answer = None

    for i in range(1, len(sequence)):       
        sequence[i] += sequence[i-1]

    for i in range(-1, len(sequence)):              # i번쨰 부터의 누적합 활용
        
        sub = 0 if i == -1 else sequence[i]         # sub : i번째 이전까지의 누적합
        start, end = 0, len(sequence)-1             # -1 : 0번째 이전에는 누적합이 없는 것에 대한 예외

        while start < end:                          # 이진탐색으로 k 값을 가지는 인덱스 찾기
            mid = (start + end) // 2                # 정확히는 처음으로 k 이상인 값을 가진 인덱스 찾기 (keyword : 파라메트릭 서치)
            if sequence[mid] - sub >= k:            
                end = mid
            else:
                start = mid + 1

        if sequence[start] - sub == k and (start - (i+1)) < interval:           # 정답은 수열이 가장 짧아야하고, 짧은 것 중에는 먼저 나온 것임
            answer = [i+1, start]
            interval = start - (i+1)

    return answer
        


case1 = [[1, 2, 3, 4, 5], 7]
case2 = [[1,1,1,2,3,4,5], 5]
case3 = [[2,2,2,2,2], 6]

print(solution(*case1))
print(solution(*case2))
print(solution(*case3))