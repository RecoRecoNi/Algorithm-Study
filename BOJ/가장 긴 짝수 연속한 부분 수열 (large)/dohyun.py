"""

풀이시간
- 약 40분 풀이 -> 도저히 시작이 안되서 풀이 참고

접근법
- N 백만 -> O(NlogN) ~ O(N) 복잡도로 해결
- 짝수로 이루어져있는 연속한 부분 수열의 가장 긴길이를 만들려면?
    - 짝수들이 밀집되어 있는 수열의 중간에 낀 홀수들을 삭제해야함
- 인덱스별 짝수 여부를 저장해놓으면 유용할 것
    - 삭제를 진행해주어야 하기 때문에 시간복잡도 측면에서 리스트 대신 딕셔너리 사용
    - 이 때 해당 인덱스 까지의 짝수 개수를 저장해놓으면 어떨까?

- 풀이 실패로 답지 참조
    - 투 포인터를 활용 -> 특정 조건을 만족하는 부분 수열의 탐색을 낮은 시간복잡도로 풀이 가능
    - 핵심은 홀수의 개수가 K개(최대 제거가능한 횟수)가 될때까지 탐색하는 것
    
회고
- 떠올리기 어려운 문제가 아니었음에도 불구하고 투포인터 자체를 생각도 못했다 ㅠㅠ
    - 특정 조건을 만족하는 부분 수열을 찾는 문제는 투포인터를 생각해보는게 좋을 듯
- 가장 낯선 유형 중 하나인데 문제 많이 풀어보기

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))

cnt = 0 # 홀수의 개수
start, end = 0, 0
size, size_max = 0, 0 # 현재 수열의 길이, 최대 수열의 길이
flag = True

for start in range(n): # 투포인터 탐색 시작
    while cnt <= k and flag:
        if S[end] % 2:
            if cnt == k: # 만약 홀수가 K 개라면 탐색 멈춤 -> K 개의 홀수 제거
                break
            cnt += 1
        size += 1 # 늘어난 현재 수열의 길이
        
        if end == n - 1: # 최대 탐색이 끝났다면 탐색 멈춤
            flag = False
            break
        
        end += 1 # end 인덱스 증가

    size_max = max(size-cnt, size_max) # 홀수개를 제거했을 때의 임시 수열의 길이의 최대값

    # start 를 한 칸 뒤로 이동시키는 작업    
    if S[start] % 2: # start가 홀수가 아니라면 홀수의 개수 감소
        cnt -= 1
        
    size -= 1 # start 를 수열에서 제거 (뒤로 이동)

print(size_max)
