"""
풀이시간: 30분

<제한사항>
- operations는 최대 1,000,000이하인 문자열 배열로 주어진다.
    -> 최대 O(nlogn)으로 해결해야 한다.
- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제한다.
- 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시한다.

<solution>
- 파이썬의 heapq 라이브러리를 사용해 우선순위큐를 만든다.
- 이 때, 파이썬의 heapq는 기본적으로 최소힙이기 때문에, 최소힙과 최대힙을 각각 만들어 주어진 연산을 수행한다.
    1) I 숫자: 최소힙과 최대힙 둘 다에 주어진 숫자를 삽입한다.
    2) D 1: 최대힙에서 최댓값을 삭제한다.
    3) D -1: 최소힙에서 최솟값을 삭제한다.
-> 가장 중요한 포인트는 visited라는 방문배열을 만들어 해당 노드가 처리됐는지 확인할 수 있도록 한다.
최대힙에서 삭제된 숫자가 최소힙에도 반영되게, 최소힙에서 삭제된 숫자가 최대힙에도 반영되게 하기 위함.

<시간복잡도>
n은 연산의 수, k는 힙에 저장된 원소의 개수라고 할 때, 
삽입/삭제의 경우 모두 O(log(k))가 걸리기 때문에 전체 시간복잡도는 O(n * log k)가 된다.


<번외>
이 문제의 경우, 백준에도 똑같은 이름의 거의 동일한 문제가 있지만 테스트 케이스가 더 많고 정확하다.
실제로 프로그래머스에서는 단순 구현이나 nsmallest를 사용해 TLE가 나거나 반례가 있는 코드들도 정답처리 돼있다;
이 문제를 여러 번 풀어보고 또 다시 정리하며, 이 풀이가 정해에 가장 가까운 풀이일 거라고 생각한다.
"""
import heapq


def solution(operations):
    answer = [0, 0] # 큐가 비어있으면 [0,0]
    n = len(operations) # 연산의 수
    
    visited = [False] * n # 값의 삭제 여부를 기록하기 위한 배열
    min_h, max_h = [], [] # 최소힙, 최대힙
    for i in range(n):
        oper, num = operations[i].split() # 공백을 기준으로 연산과 숫자로 나눔

        # 1) I 숫자 -> 최소힙/최대힙 둘 다에 주어진 숫자를 삽입한다.
        if oper == 'I': 
            heapq.heappush(min_h, (int(num), i)) # 몇 번째 노드를 처리했는지 표시하기 위해 i를 함께 넣어준다
            heapq.heappush(max_h, (-int(num), i)) # 기본적으로 heapq는 최소힙이기 때문에 최대힙으로 사용하려면 -를 붙여서 넣어줘야 한다.
            visited[i] = True # 해당 노드를 방문처리한다.
        
        # 2) D 1 -> 최대힙에서 최대값을 삭제한다.
        elif num == '1':
            while max_h and not visited[max_h[0][1]]: # 삭제되지 않은 노드가 나올 때까지
                heapq.heappop(max_h)
            if max_h: # 큐(최대힙)가 비어있지 않다면
                visited[max_h[0][1]] = False # 최대힙의 루트가 항상 가장 큰 값을 가지고 있기 때문에 해당 값을 삭제처리해준다.
                heapq.heappop(max_h)
        
        # 3) D -1 -> 최소힙에서 최솟값을 삭제한다.
        elif num == '-1':
            while min_h and not visited[min_h[0][1]]: # 삭제되지 않은 노드가 나올 때까지
                heapq.heappop(min_h)
            if min_h: # 큐(최소힙)가 비어있지 않다면
                visited[min_h[0][1]] = False # 최소힙의 루트가 항상 가장 작은 값을 가지고 있기 때문에 해당 값을 삭제처리해준다.
                heapq.heappop(min_h)
        
    # 최소힙/최대힙에서 각각 삭제처리되지 않은 값을 처리한다.
    while max_h and not visited[max_h[0][1]]: heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]: heapq.heappop(min_h)

    # 최소힙과 최대힙의 첫 번째 원소(루트 노드)는 항상 각각 가장 작은 값과 가장 큰 값을 가지고 있다.
    if max_h:
        answer[0] = -max_h[0][0]
    if min_h:
        answer[1] = min_h[0][0]

    return answer


"""
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
"""