'''
풀이 시작 : 2023.08.03 15:45

우선순위 큐에서 빈 큐가 아니라면 최대값, 최소값만 구할 수 있으면 된다.
이를 위해 큐를 최소힙으로 구현한다면 최소 값은 0번쨰 인덱스, 최대 값은 nlargest(1)로 구해낼 수 있다.
그렇다면 최소값을 삭제하는 연산은 O(1)에 가능할 것 같은데, 최대 값을 삭제하는 것은 O(n) 이상이 걸릴 것
될까..? 복잡도가 감이 안잡힘 일단 해보자 -> 옹 된당

풀이 완료 : 2023.08.03 16:06

### 이번 풀이에 사용했던 [heapq 라이브러리의 시간 복잡도](https://medium.com/plain-simple-software/python-heapq-use-cases-and-time-complexity-ee7cbb60420f)가 헷갈려서 다시 찾아봤다.
- heappush(heap, value) : 삽입 시에 제자리 찾아가는 과정을 거침, 이진 트리 기반이므로 O(logn)
- heappop(heap) : 최소값 하나를 삭제 후 힙 구조에 맞춰서 인덱싱을 거침 O(logN)
- nlargest(m, heap) : heap에서 큰 순서대로 m개 찾아서 반환해줌, 복잡도는 힙의 요소가 n개라고 할 때 O(n+log(m))
'''

from typing import List
from heapq import heappush, heappop, nlargest


def solution(operations : List):
    heap:List[str] = list()  # 리스트를 힙으로 활용할 것, 디폴트는 min heap

    for operation in operations:
        op, value = operation.split()
        if op == 'I':                       # 삽입 연산
            heappush(heap, int(value))
        elif heap:                                  # 최대값 / 최소값 삭제 연산, heap에 원소가 있을 때만 실행
            if value=='1':                          # 최대값 삭제 연산
                heap.remove(*nlargest(1, heap))     # 1번째로 큰 값 찾아서 삭제(nlargest의 반환 타입은 list임)
            else:                                   # 최소값 삭제 연산
                heappop(heap)                       # min heap이 default이므로 heappop시 최소값 삭제

    return [*nlargest(1, heap), heappop(heap)] if heap else [0, 0]      # heap에 원소가 있으면 [최대값, 최소값] 반환, 비었으면 [0, 0] 반환


def main():
    case1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]  # [0, 0]
    case2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] # [333, -45]
    print(solution(case1))
    print(solution(case2))


main()