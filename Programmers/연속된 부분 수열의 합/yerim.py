"""
- 소요 시간: 50분 + 30분(풀이 참고)

- 초기 접근 방법 => 시간 초과
    - 시작 인덱스를 고정하고, 부분 수열의 길이가 1~n일 때 각 경우의 합을 모두 구함
        - 시작 인덱스가 증가하는 만큼, 만들 수 있는 부분 수열의 개수는 짧아짐
    - 부분 수열의 합이 k인 경우 해당 부분 수열 저장
        - 부분 수열을 키로, 시작 인덱스와 마지막 인덱스를 값으로 하는 딕셔너리로 저장
    - 여러 부분 수열을 길이, 인덱스 순으로 정렬해 첫 번째 원소를 답으로 리턴

- [참고](https://safetymo.tistory.com/14)
    - 투 포인터를 사용
    - 합이 작으면 오른쪽 포인터를 이동하고, 합이 크거나 같으면 왼쪽 포인터를 이동
    
"""

# # 초기 접근 방법 => 시간 초과
# def solution(sequence, k):
#     subseq = []
#     len_seq = len(sequence)
    
#     for i in range(len_seq): # 시작 인덱스
#         for j in range(len_seq-i): # 마지막 인덱스 + 1
#             if sum(sequence[i:i+j+1]) == k:
#                 subseq.append([i, i+j])
    
#     subseq = sorted(subseq, key=lambda x: x[1]-x[0])
#     return subseq[0]

def solution(sequence, k):
    answer = []
    right = 0
    sum_subseq = 0
    
    for left in range(len(sequence)):
        while right < len(sequence) and sum_subseq < k: # 합이 k보다 작으면
            sum_subseq += sequence[right] # 오른쪽 원소를 계속 더함 (오른쪽 포인터를 오른쪽으로 이동)
            right += 1
        
        if sum_subseq == k:
            if not answer:
                answer = [left, right-1]
            else:
                # 기존 부분 수열의 길이가, 현재 구한 부분 수열의 길이보다 크면 현재 구한 부분 수열을 answer로 저장. 아니면 기존 부분 수열을 answer로 유지
                answer = [left, right-1] if answer[1] - answer[0] > right - 1 - left else answer 
        
        sum_subseq -= sequence[left] # 왼쪽에 있는 원소를 제외 (왼쪽 포인터를 오른쪽으로 이동)
        
    return answer