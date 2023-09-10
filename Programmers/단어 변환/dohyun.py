"""

풀이시간
- 약 1시간 30분

접근법
- 하나의 단어는 접근하면 다시 사용하지 않음 (왜? 다시 접근할거면 변환을 할 필요가 없으니까, 무한 루프도는거)
- 한번 방문한 곳은 다시 안감 + 완전탐색 + 최소 count -> BFS
- "한 번에 한 개의 알파벳만 바꿀 수 있다" 조건만 잘 처리하자!
    - 단어의 길이가 최대 10이므로 그냥 단순 순회하며 확인해보면 될 듯함

회고
- 한 개의 알파벳만 바꿀 수 있다 -> "BCB" 와 같은 단어가 오면 "ACA" 로도 바꿀 수 있다
    - 이렇게 해석을 잘 못해서 시간이 좀 오래 걸렸음 ㅠ ㅠ

"""

from collections import deque

def solution(begin, target, words):
    if target not in words: # 정답이 없으면 0 반환
        return 0
    
    def check_word(word1, word2): # 한 개의 알파벳만 바꿔도 되는지 여부를 반환
        cnt = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                cnt += 1
            if cnt > 1:
                return False
        return True

    words.append(begin)
    visit = [-1] * (len(words))
    queue = deque([len(words)-1])
    visit[len(words)-1] = 0

    target_idx = words.index(target)
    
    while queue: # BFS
        node = queue.popleft()
    
        for i in range(len(words)):
            if visit[i] == -1: # 방문하지 않은 단어에만 접근
                if check_word(words[node], words[i]): # 한개의 알파벳 조건 만족하면
                    queue.append(i) # 해당 단어도 큐에 추가
                    visit[i] = visit[node] + 1
            elif i==target_idx: # 이미 방문한적이 있으며 target 에 도달했다면 정답 반환
                return visit[target_idx]