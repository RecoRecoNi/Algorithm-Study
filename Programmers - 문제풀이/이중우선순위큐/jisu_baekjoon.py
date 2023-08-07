'''
이중 우선순위 큐 백준 버전 : 프로그래머스 문제와 동일하지만, 테스트 케이스에 대해 좀 더 엄격한 문제
풀이 시작 : 2023.08.06 21:25

- 동일하게 min heap으로 구현하되, 보다 효율적으로 최댓값을 삭제해야 함
- 접근 1 : minheap, maxheap을 관리하는 MinMaxHeap 클래스를 구현해서 해결해보기
  - 문제는 한 쪽에서 pop 했을 때 다른 한 쪽은 어떻게 없앨꺼냐...
    - 반대편 heap 맨 뒤에서 부터 탐색해서 없애보기? 맨 뒤에서 부터 있을 확률이 높으니까 조금 더 연산이 줄지 않을까? 안정적이지는 못 한 방법.
      - 없앤다음에 heapify 해야함
      - 시간초과...
'''

import sys
from typing import List
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

class MinMaxHeap:
    def __init__(self):
        self.minHeap: List = list()
        self.maxHeap: List = list()

    def empty(self) -> bool:
        return len(self.minHeap) == len(self.maxHeap) == 0

    def push(self, value: int) -> None:
        heappush(self.minHeap, value)
        heappush(self.maxHeap, -value)

    def popMin(self) -> int:
        result = heappop(self.minHeap)
        
        for idx in range(len(self.maxHeap)-1, -1, -1):
            if self.maxHeap[idx] == -result:
                self.maxHeap.pop(idx)
                heapify(self.maxHeap)

        return result
    
    def popMax(self) -> int:
        result = heappop(self.maxHeap)

        for idx in range(len(self.minHeap)-1, -1, -1):
            if self.minHeap[idx] == -result:
                self.minHeap.pop(idx)
                heapify(self.minHeap)

        return -result
    
def solution():
    num_of_testcases = int(input())
    for _ in range(num_of_testcases):

        heap = MinMaxHeap()

        num_of_operations = int(input())
        for _ in range(num_of_operations):
            op, value = input().rstrip().split()
            value = int(value)

            if op == 'I':
                heap.push(value)

            elif op == 'D' and not heap.empty():
                if value == 1:
                    heap.popMax()
                else:
                    heap.popMin()

        print('EMPTY') if heap.empty() else print(*[heap.popMax(), heap.popMin()])

solution()

