'''
이중 우선순위 큐 백준 버전 : 프로그래머스 문제와 동일하지만, 테스트 케이스에 대해 좀 더 엄격한 문제
풀이 시작 : 2023.08.06 21:25

- 동일하게 min heap으로 구현하되, 보다 효율적으로 최댓값을 삭제해야 함
- 접근 1 : minheap, maxheap을 관리하는 MinMaxHeap 클래스를 구현해서 해결해보기
  - 문제는 한 쪽에서 pop 했을 때 다른 한 쪽은 어떻게 없앨꺼냐...
    - 반대편 heap 맨 뒤에서 부터 탐색해서 없애보기? 맨 뒤에서 부터 있을 확률이 높으니까 조금 더 연산이 줄지 않을까? 안정적이지는 못 한 방법.
      - 없앤다음에 heapify 해야함
      - 시간초과...
- 접근 2 : 삽입된 수의 유효성 검증 로직 추가
  - 지금 최대힙, 최소힙을 동시에 활용했을 때 문제가 pop을 했을 때 반대쪽 힙에 이를 반영해주는 데에서 문제임
  - 그럼 반대쪽에서 pop할 때 이미 삭제된 원소가 나온다면 이를 무효처리해주면 됨
  - 이를 위해서는 삽입된 원소라는 걸 알리기 위한 별도의 자료구조가 필요함 -> 2^31개의 수를 모두 체크하지 말고 최대 1000000개의 수가 주어지니까 이 순서대로 수가 삽입되어있는 지를 관리하자
  - 그러기 위해서 삽입할 때 이 자료구조의 인덱스 정보를 같이 넘겨줘야함.
  - 큐가 비었는지 확인해야하는 경우가 있으니까 원소 고유 개수를 세는 변수를 하나 관리하자.
  - 막판에 출력 시 pop을 사용해서 출력하면 max, min값을 둘 다 출력하지 못하므로 peek도 구현해야 함, 동일하게 pop으로 이미 삭제한 원소이면 무효처리 해주면 된다.

풀이 완료 : 2023.08.07 12:58
'''

import sys
from typing import List
from heapq import heappush, heappop

input = sys.stdin.readline

class MinMaxHeap:
    def __init__(self, num_of_operations):
        '''
        생성자

        - self.inserted : 현재 이중우선순위큐에 삽입된 수들의 유효성을 관리하는 변수
        - self.minHeap, self.maxHeap : 이중 우선순위큐를 구현하기 위한 min Heap, max Heap
        - self.count : 유효한 수들의 개수를 관리하는 변수
        '''
        self.inserted: List[bool] = [False for _ in range(num_of_operations)]
        self.minHeap: List[int] = list()
        self.maxHeap: List[int] = list()
        self.count: int = 0

    def empty(self) -> bool:
        '''
        현재 이중우선순위큐가 비었는지 확인하는 연산
        '''
        return self.count == 0

    def push(self, value: int, idx: int) -> None:
        '''
        이중우선순위큐 삽입 연산

        - 각 힙에 value 값과 함께 현재 입력 순서 인덱스를 삽입한다.
        - idx번째 순서로 삽입된 수는 유효한 수임을 체크
        - 최대힙을 구현하기 위해 value에 -기호를 붙혀 삽입해야 한다.
        '''
        self.inserted[idx] = True
        self.count += 1
        heappush(self.minHeap, (value, idx))
        heappush(self.maxHeap, (-value, idx))

    def popMin(self) -> int:
        '''
        이중우선순위큐 최소값 pop 연산

        - validation : 검증을 위한 boolean 변수
        - inserted[idx]가 True인 유효한 수가 반환될 때까지 최소 힙에서 반복해서 heappop연산을 수행한다.
        - 유효하지 않은 수(False)가 반환되었다는 것은 이미 max heap에서 삭제된 수라는 뜻
        '''
        validation = False

        while not validation:
            result, idx = heappop(self.minHeap)
            validation = self.inserted[idx]
        
        self.inserted[idx] = False
        self.count -= 1

        return result
    
    
    def popMax(self) -> int:
        '''
        이중우선순위큐 최소값 pop 연산

        - validation : 검증을 위한 boolean 변수
        - inserted[idx]가 True인 유효한 수가 반환될 때까지 최대 힙에서 반복해서 heappop연산을 수행한다.
        - 유효하지 않은 수(False)가 반환되었다는 것은 이미 min heap에서 삭제된 수라는 뜻
        - max heap을 구현하기 위해 value가 음수로 저장되어 있으므로 부호를 반전하여 값을 반환해주어야 함
        '''
        validation = False

        while not validation:
            result, idx = heappop(self.maxHeap)
            validation = self.inserted[idx]
    
        self.inserted[idx] = False
        self.count -= 1

        return -result
    
    def peekMin(self) -> int:
        '''
        이중우선순위큐 최소값 peek 연산

        - 마지막 반환 시에 pop으로 반환하게 되면 최대, 최소 값을 온전하게 반환하지 못함(큐에 원소가 하나 있는 경우)
        - 마찬가지로 유효하지 않은 값은 모두 pop해버리고, 유효한 값이 큐의 최 상단에 있으면 이를 반환
        '''
        while not self.inserted[self.minHeap[0][1]]:
            heappop(self.minHeap)

        return self.minHeap[0][0]

    def peekMax(self) -> int:
        '''
        이중우선순위큐 최대값 peek 연산

        - 마지막 반환 시에 pop으로 반환하게 되면 최대, 최소 값을 온전하게 반환하지 못함(큐에 원소가 하나 있는 경우)
        - 마찬가지로 유효하지 않은 값은 모두 pop해버리고, 유효한 값이 큐의 최 상단에 있으면 이를 반환
        '''
        while not self.inserted[self.maxHeap[0][1]]:
            heappop(self.maxHeap)

        return -self.maxHeap[0][0]
      
    
def solution():
    num_of_testcases = int(input())
    for _ in range(num_of_testcases):
        num_of_operations = int(input())
        heap = MinMaxHeap(num_of_operations)
        for idx in range(num_of_operations):
            op, value = input().rstrip().split()
            value = int(value)

            if op == 'I':
                heap.push(value, idx)

            elif op == 'D' and not heap.empty():
                if value == 1:
                    heap.popMax()
                else:
                    heap.popMin()

        print('EMPTY') if heap.empty() else print(*[heap.peekMax(), heap.peekMin()])

solution()

