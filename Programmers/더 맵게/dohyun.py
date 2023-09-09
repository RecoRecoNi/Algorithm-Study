"""

풀이시간
- 약 30분

접근법
- 스코빌의 길이는 최대 백만 -> O(N) 에 가깝게 해결해야함
- 최대, 최소를 넣었다 뺐다 -> 힙을 이용하면 되겠다!

회고
- 수민님이 저번에 보여주신 힙이 기억에 나서 풀 수 있었습니다!!!

"""
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while True:
        not_spicy_one = heapq.heappop(scoville)
        
        if not_spicy_one >= K:
            return answer
        elif not scoville:
            return -1
        else:
            not_spicy_two = heapq.heappop(scoville)
            new_one = not_spicy_one + not_spicy_two * 2
            heapq.heappush(scoville, new_one)
            answer += 1