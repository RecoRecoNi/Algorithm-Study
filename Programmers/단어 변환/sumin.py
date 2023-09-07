"""
풀이 시간: 20분

<입력, 제한사항>
- 각 단어는 알파벳 소문자로만 이루어져 있음
- 각 단어의 길이는 3 이상 10이하, 모든 단어의 길이가 같음
- words에는 3개 이상 50개 이하의 단어가 있고, 중복되는 단어는 없음
- begin과 target은 서로 다름
- 변환할 수 없는 경우 0 return


<풀이>
begin 단어에서 target 단어까지 가는 최단경로를 찾기 위해서 BFS를 사용함(각각의 단어를 노드로 생각)
1. 시작 단어를 큐에 넣는다.
2. dist 배열에 {key: value}를 {각 단어: begin에서 해당 단어까지 걸리는 최단거리} 형태로 초기화한다.
3. 큐에서 하나의 단어씩 꺼내 다음 단어로 올 수 있는 단어만 깊이를 갱신한다. (이 때, dist 배열을 사용해 아직 방문하지 않은 단어에 대해서만 처리한다.)
    - can_transform 함수를 통해 '한 번에 한 개의 알파벳만 바꿀 수 있습니다.' 조건을 만족하는지 확인
4. 만약 현재 단어가 target 단어라면 해당 단어까지의 깊이를 return 해준다.
5. 큐가 빌 때까지 다 돌아도 target 단어까지의 깊이를 return 하지 못한다면 해당 단어로 만들 수 없는 경우이기 때문에 0을 return 한다.

<시간 복잡도>
O(N * K)
- N: words 리스트의 길이(최대 50)
    - BFS를 통해 words 리스트의 모든 단어를 한 번씩만 확인하므로 O(N)
- K: 단어의 길이(최대 10)
    - can_transform 함수는 두 단어의 길이만큼만 비교하기 때문에 최대 O(K)
-> 큐와 딕셔너리를 통해 각 단어를 한 번씩만 처리하기 때문에, 전체 시간복잡도는 O(N*K)
"""

from typing import List
from collections import deque

# word1을 word2로 변환할 수 있는지 확인하는 함수
def can_transform(word1: str, word2: str) -> bool:
    diff_cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_cnt += 1
        if diff_cnt > 1: # 한 번에 한 단어만 바꿀 수 있음
            return False
    return diff_cnt == 1 # 한 단어만 바뀐 경우 True값 반환


def solution(begin: str, target: str, words: List) -> int:
    q = deque([begin])
    dist = {begin: 0} # 해당 단어까지의 깊이

    while q:
        cur_word = q.popleft()
        if cur_word == target: # 현재 단어가 target 단어라면
            return dist[cur_word] # begin -> target까지 필요한 최소 횟수
        for word in words: # 아직 확인하지 않은 단어에 대해서만 다음 단어로 선택할 수 있는지 확인
            if word not in dist and can_transform(cur_word, word):
                q.append(word)
                dist[word] = dist[cur_word] + 1 # 거리 갱신

    return 0 # 큐가 빌 때까지 while 문에서 최소 횟수가 return 되지 않았다면 target 단어를 만들 수 없는 것임


"""
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.06ms, 10.7MB)
테스트 3 〉	통과 (0.23ms, 10.5MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.5MB)
"""