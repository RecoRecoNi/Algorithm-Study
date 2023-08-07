"""
    이중우선순위큐
    https://school.programmers.co.kr/learn/courses/30/lessons/42628
    https://www.acmicpc.net/problem/7662
    
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

    # 파이썬은 최소합으로 heapq가 구현되어있기 때문에 우선순위큐를 사용해야할 때 
    # 최대 값을 기억하기 위해서는 최소 힙에 값을 대입 할 때 -1을 곱해준다.

    # 하지만 최소 힙은 최대 값을 구할 수 없고 최대 힙은 최소 값을 구할 수 없다.

    # 그렇기에 하나는 포기를 해야했고 그럴 경우 통과가 가능한지 생각해본다면 
    #     100만개의 연산중에 50만개는 값의 입력이었고 50만개는 heappop()를 사용할 수 없는 연산이다.
    #     이때에 시간 복잡도는 50만번 heappush :O(500,000log500,000)(3,765,423) + 50만번 최대 값 연산 max : O(500,000)
    #     3,765,423 + 500,000 = 4백2십만 번
    #     1초의 연산을 넘기지 않는다.

    # 최대 값을 구하는 방법은 Max() 와 heapq.nlargest(1,heap) 으로 구할 수 있는데 두 가지 경우의 O()를 계산하였을 때
    # nlargest(m) - O(n+logm) : max(list()) - O(n) 이므로 max의 효율이 간소하게 더 좋은 것을 알 수 있었다.

    # 하지만 코드 실행시에는 큰 차이가 없는 것을 확인 할 수 있었다.

    처음 풀이는 시간 복잡도를 잘못 계산한 결과로 다음의 풀이는 엣지 테스트 케이스에서는 틀렸다는 답을 낼 수 있었습니다.

    해당 문제에서는 최대 값과 최대 값을 모두 반환하기 위해 최대 힙과 최소 힙을 모두 구현해야하며 다음의 연산들은 heappush , heappop 으로 이루어져 있어
    O(nlogn)의 시간 복잡도를 가질 수 있게 됩니다.

    하지만 다음의 풀이의 중점은 어떻게 삭제된 요소들을 각각의 힙에 어떻게 반영할지 였습니다.

    그렇기에 삭제된 요소들을 가질 수 있는 리스트를 생성해주었으며 값이 중복될 수 있기에 operation에 idx를 부여하여 모니터링 할 수 있도록 하였습니다.

    분산으로 처리되는 경우 하나의 상태를 저장하는 아키텍쳐에서 아이디어를 얻을 수 있었으며 자세한 풀이는 아래의 블로그를 참고하였습니다.

    Ref : https://codio.tistory.com/entry/백준-7662번-이중-우선순위-큐-Python파이썬
"""
import sys
from typing import List
import heapq

# def solution(operations : List[str]):
#     # 정렬을 위한 Min / Max Heap(list) 생성
#     max_h:List[int] = []
#     min_h:List[int] = []
    
#     for operation in operations:    
#         # Operation Split 후 value integer로 변환
#         command, value = operation.split()
#         value = int(value)
        
#         # max 값은 max() 로 계산하고 min 값은 min_heap을 사용하여 계산
#         # max 값은 max_heap 으로 계산하고 min 값은 min_heap을 사용하여 계산
#         if command == "I":
#             # 기본적으로 min_heap을 제공하기 때문에 max_heap을 만들기 위해 -1을 곱해준다.
#             heapq.heappush(max_h, -value)
#             heapq.heappush(min_h, value)
#         elif command == "D" and max_h and min_h:
#             if value == 1:
#                 min_h.remove(-1 * heapq.heappop(max_h))
#                 # h.remove(*heapq.nlargest(1,h))
#             else:
#                 max_h.remove(-1 * heapq.heappop(min_h))
    

#     return [0,0] if not max_h else [-1 * heapq.heappop(max_h), heapq.heappop(min_h)]
#     # return [0,0] if not h else [*heapq.nlargest(1,h), h[0]]

# case1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]  # [0, 0]
# case2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] # [333, -45]
# print(solution(case1))
# print(solution(case2))


import sys
from typing import List
import heapq

input = sys.stdin.readline

def boj_solution():
    for  _ in range(int(input())):
        # 정렬을 위한 Min / Max Heap(list) 생성å
        max_h:List[int] = []
        min_h:List[int] = []

        N = int(input())

        removed_element:List[int] = [1] * N
        for idx in range(N):
            # Operation Split 후 value integer로 변환
            command, value = input().split()
            value = int(value)
            # max 값은 max() 로 계산하고 min 값은 min_heap을 사용하여 계산
            # max 값은 max_heap 으로 계산하고 min 값은 min_heap을 사용하여 계산
            if command == "I":
                # 기본적으로 min_heap을 제공하기 때문에 max_heap을 만들기 위해 -1을 곱해준다.
                heapq.heappush(max_h, (-value,idx))
                heapq.heappush(min_h, (value,idx))
            elif command == "D":
                if value == 1 and max_h:
                    removed_element[heapq.heappop(max_h)[1]] = 0
                    # min_h.remove(-1 * heapq.heappop(max_h))
                elif value == -1 and min_h:
                    removed_element[heapq.heappop(min_h)[1]] = 0
                    # max_h.remove(-1 * heapq.heappop(min_h))
            
            # 반환할 값이 삭제된 값인지 확인하고 삭제될 값이라면 삭제
            while max_h and removed_element[max_h[0][1]] == 0:
                heapq.heappop(max_h)
            while min_h and removed_element[min_h[0][1]] == 0:
                heapq.heappop(min_h)


        print("EMPTY" if not max_h else f"{-1 * max_h[0][0]} {min_h[0][0]}")
    
boj_solution()