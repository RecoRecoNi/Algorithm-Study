"""
풀이시간: 30분

<input>
- 영문 대문자로만 이뤄진 문자열 msg
- msg의 길이는 1이상 1000 이하

<solution>
- 시작지점과 끝지점 인덱스를 통해 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
- 현재 입력이 사전에 존재하지 않는 단어라면 그 끝지점의 인덱스를 하나 줄인 것이 가장 긴 문자열 w에 해당함
- w의 색인번호를 answer에 추가(출력)하고, 사전에 존재하지 않는 단어(w+c)를 사전에 등록하면 된다.
- 딕셔너리 자료형을 사용하면 O(1)로 모두 탐색 가능

<시간복잡도>
O(n): msg의 길이
"""
from string import ascii_uppercase


def solution(msg):
    answer = []
    # 1. 길이가 1인 모든 단어를 포함하도록 사전 초기화
    dic = {alpha : i+1 for i, alpha in enumerate(ascii_uppercase)}

    # i: 시작 지점, j: 끝지점
    i, j = 0, 0
    while j < len(msg): # j가 msg의 길이를 넘지 않는 동안 반복
        j += 1
        # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        if j == len(msg) or msg[i:j+1] not in dic: # 현재 단어가 사전에 없다면 그 단어의 직전까지가 사전에 존재하는 가장 긴 문자열 w
            answer.append(dic[msg[i:j]]) # 3. w에 해당하는 사전의 색인 번호를 answer에 추가
            dic[msg[i:j+1]] = len(dic) + 1 # w+c에 해당하는 단어를 사전에 등록
            i = j # 다음 글자로 넘어간다.

    return answer


# 테스트 케이스
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))


"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.38ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.52ms, 10.3MB)
테스트 7 〉	통과 (0.35ms, 10.3MB)
테스트 8 〉	통과 (0.37ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.41ms, 10.2MB)
테스트 11 〉	통과 (0.23ms, 10.2MB)
테스트 12 〉	통과 (0.40ms, 10.4MB)
테스트 13 〉	통과 (1.04ms, 10.4MB)
테스트 14 〉	통과 (0.98ms, 10.2MB)
테스트 15 〉	통과 (0.52ms, 10.2MB)
테스트 16 〉	통과 (0.44ms, 10.2MB)
테스트 17 〉	통과 (0.61ms, 10.1MB)
테스트 18 〉	통과 (0.26ms, 10.3MB)
테스트 19 〉	통과 (0.15ms, 10.4MB)
테스트 20 〉	통과 (0.54ms, 10.3MB)
"""