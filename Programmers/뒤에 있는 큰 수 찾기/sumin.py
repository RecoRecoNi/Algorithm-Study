"""
풀이시간 : 25분

<input>
numbers: 정수로 이루어진 배열
- 4 ≤ numbers의 길이 ≤ 1,000,000
- 1 ≤ numbers[i] ≤ 1,000,000

<solution>
현재까지 나온 수들을 최소힙으로 저장하고, 이후 더 큰 수가 나오면 더 작은 수의 해당 위치를 업데이트 해주기

<시간복잡도>
O(nlogn)

다 풀고 다른 사람 풀이를 보니까 굳이 heap을 써줄 필요가 없었음..
stack으로 이전 숫자의 인덱스만 저장해두고, 현재 수가 더 클때 pop해서 해당 인덱스의 위치를 업데이트 해주면 되는데...😂
"""
from typing import List
import heapq

def solution(numbers: List) -> List:
    n = len(numbers)
    answer = [-1] * n
    heap = [] # 최소힙

    for i in range(n):
        cur_number = numbers[i]
        while heap and heap[0][0] < cur_number: # 현재 확인하고 있는 수 이전에 나온 수 중에 현재 수보다 작은 수를 모두 갱신
            num, idx = heapq.heappop(heap)
            answer[idx] = cur_number

        heapq.heappush(heap, (cur_number, i)) # [현재 확인하고 있는 수, 인덱스]를 최소힙에 추가

    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))

"""
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.59ms, 10.3MB)
테스트 6 〉	통과 (6.51ms, 11.3MB)
테스트 7 〉	통과 (6.21ms, 11.4MB)
테스트 8 〉	통과 (32.56ms, 17.1MB)
테스트 9 〉	통과 (30.88ms, 16.9MB)
테스트 10 〉	통과 (65.20ms, 19.6MB)
테스트 11 〉	통과 (65.26ms, 19.5MB)
테스트 12 〉	통과 (135.81ms, 25.4MB)
테스트 13 〉	통과 (135.28ms, 25.4MB)
테스트 14 〉	통과 (369.68ms, 43.3MB)
테스트 15 〉	통과 (880.09ms, 75.4MB)
테스트 16 〉	통과 (887.28ms, 75.5MB)
테스트 17 〉	통과 (904.36ms, 75.5MB)
테스트 18 〉	통과 (794.01ms, 75.5MB)
테스트 19 〉	통과 (751.38ms, 75.5MB)
테스트 20 〉	통과 (1627.31ms, 136MB)
테스트 21 〉	통과 (1341.66ms, 173MB)
테스트 22 〉	통과 (1307.02ms, 70.9MB)
테스트 23 〉	통과 (503.30ms, 173MB)
"""