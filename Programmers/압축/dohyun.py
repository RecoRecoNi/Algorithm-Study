"""

풀이시간
- 46분

접근법
- n 이 1000 이하 -> O(N^2) 이상의 풀이도 가능
- 특정 알고리즘을 예시까지 친절히 주었고 시간복잡도 충분 -> 일단 구현해보자
- 초기 단어사전을 딕셔너리로 구현하려했지만 리스트로해도 문제없음 -> 리스트로 구현
- 업데이트되는 단어가 가변성을 띄는 것을 주의
    - 시간복잡도가 충분하기 때문에 반복문으로 구현

회고
- 예제를 친절하게 제공해줘서 풀이하기가 비교적 수월했음
- 이후에 궁금해서 검색해보니 해시 테이블로 구현되어있는 딕셔너리를 사용하는게 시간복잡도를 더 줄일 수 있는 방법이었던것 같음

"""

def solution(msg):
    answer = []
    words = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # 단어 사전 초기화 단계

    idx = -1
    while idx < len(msg) - 1: # 전체 단어들을 순회
        idx += 1
        temp_word = msg[idx] # 첫 글자 입력

        for len_word in range(2, len(words)): # 다음 글자들이 사전에 존재하는지 확인
            new_word = msg[idx:idx + len_word]
            
            if new_word in words: # 만약 단어사전에 존재하면 첫 글자가 아닌 해당 단어로 대체
                temp_word = new_word
            else:
                words.append(new_word) # 만약 단어사전에 존재하지 않으면 단어사전에 추가하고 반복문 종료
                break            
        
        answer.append(words.index(temp_word) + 1) # 최종적으로 결정된 단어 색인 번호 추가
        idx += len(temp_word) - 1 # 순회 시작 인덱스를 변경 (입력 단어가 첫 글자가 아닌 경우에만 업데이트됨)
            
    return answer


print(solution("KAKAO")) # [11, 1, 27, 15]
print('----------')
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print('----------')
print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]