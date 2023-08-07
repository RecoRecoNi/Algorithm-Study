"""
    이중우선순위큐
    https://school.programmers.co.kr/learn/courses/30/lessons/42628
    
    100만번의 연산이 주어지고 이를 해결하기 위해서는 초당 2000만번을 계산하는 파이썬은 최대 O(nlogn)에 계산되어야한다.

    풀이시간
    22:35 ~ 23:35(1시간)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> Heap

    heapify - O(n)
    heappush - O(logn)
    heappop - O(logn)
    nlargest(m) - O(n+logm)
    
    max(list()) - O(n)

    파이썬은 최소합으로 heapq가 구현되어있기 때문에 우선순위큐를 사용해야할 때 
    최대 값을 기억하기 위해서는 최소 힙에 값을 대입 할 때 -1을 곱해준다.

    하지만 최소 힙은 최대 값을 구할 수 없고 최대 힙은 최소 값을 구할 수 없다.

    그렇기에 하나는 포기를 해야했고 그럴 경우 통과가 가능한지 생각해본다면 
        100만개의 연산중에 50만개는 값의 입력이었고 50만개는 heappop()를 사용할 수 없는 연산이다.
        이때에 시간 복잡도는 50만번 heappush :O(500,000log500,000)(3,765,423) + 50만번 최대 값 연산 max : O(500,000)
        3,765,423 + 500,000 = 4백2십만 번
        1초의 연산을 넘기지 않는다.

    최대 값을 구하는 방법은 Max() 와 heapq.nlargest(1,heap) 으로 구할 수 있는데 두 가지 경우의 O()를 계산하였을 때
    nlargest(m) - O(n+logm) : max(list()) - O(n) 이므로 max의 효율이 간소하게 더 좋은 것을 알 수 있었다.

    하지만 코드 실행시에는 큰 차이가 없는 것을 확인 할 수 있었다.
"""

from typing import List
import heapq

def solution(operations : List[str]):
    # 정렬을 위한 Heap(list) 생성
    h:List[int] = []
    
    for operation in operations:    
        # Operation Split 후 value integer로 변환
        command, value = operation.split()
        value = int(value)
        
        # max 값은 max() 로 계산하고 min 값은 min_heap을 사용하여 계산
        if command == "I":
            heapq.heappush(h, value)
        elif command == "D" and h:
            if value == 1:
                h.remove(max(h))
                # h.remove(*heapq.nlargest(1,h))
            else:
                heapq.heappop(h)

    return [0,0] if not h else [max(h), h[0]]
    # return [0,0] if not h else [*heapq.nlargest(1,h), h[0]]

case1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]  # [0, 0]
case2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] # [333, -45]
print(solution(case1))
print(solution(case2))


#1 max(h)
# 테스트 1 〉	통과 (0.06ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.03ms, 10.6MB)
# 테스트 4 〉	통과 (0.03ms, 10.5MB)
# 테스트 5 〉	통과 (0.03ms, 10.8MB)
# 테스트 6 〉	통과 (0.03ms, 10.8MB)

#2 nlargest(1,h)
# 테스트 1 〉	통과 (0.03ms, 10.7MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.03ms, 10.7MB)
# 테스트 4 〉	통과 (0.03ms, 10.5MB)
# 테스트 5 〉	통과 (0.03ms, 10.6MB)
# 테스트 6 〉	통과 (0.05ms, 10.5MB)