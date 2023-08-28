"""

풀이시간
- 약 1시간 30분

접근법
- 비내림차순이므로 시작 인덱스가 고정되어 있으면 종료 인덱스는 특정 값까지의 합이 k 를 넘는이상 종료됨
    - 따라서 시작 인덱스를 반복문으로 시작하기로 함
- 배열에 저장하지 않고 갱신 방식으로 답 저장 방식 채택
    - 연산 속도 줄일 수 있음
- 처음에는 슬라이싱 연산을 매번해서 sum 을 했는데, 부분 수열의 합이고 업데이트 되는것은 인덱스들이기 때문에 매번 합을 할 필요가 없었음
    - 슬라이싱 연산 시간복잡도 O(end-start) -> 합을 변수에 저장해서 갱신하자!

회고
- 생각보다 쉬운것 같다하고 풀었는데 테케에서 절반 정도 시간초과 나서 당황
    - 그림을 다시 짜느라 고생했음 ... 처음부터 시간복잡도 고려를 꼼꼼히 해야하는데 아직 습관이 안된 것 같다 ㅠㅠ

"""

def solution(sequence, k):
    answer = []
    end_idx = 0
    seq_len = len(sequence)
    
    for start_idx in range(len(sequence)):
        if start_idx == 0:  # 맨 처음 시작할때의 임시 합 정의
            tmp_sum = sequence[start_idx]
        else:
            tmp_sum -= sequence[start_idx -1]   # 부분수열이 업데이트 되었으므로 이전 값 제거

        while end_idx <= len(sequence): # 마지막 시퀀스까지 루프 돌기
            if tmp_sum < k: # 시작 인덱스가 고정일 때 합이 k 보다 작으면 종료 인덱스 늘려야 함
                end_idx += 1
                if end_idx < len(sequence): # 오류 픽스 코드
                    tmp_sum += sequence[end_idx]
            
            elif tmp_sum > k:   # 합이 k 를 넘으면 종료 인덱스를 늘릴 필요가 없고 시작 인덱스를 늘려야 함
                break
            
            elif tmp_sum == k:  # 합이 k 인 경우, 즉 정답
                if (end_idx - start_idx) < seq_len: # 부분 수열의 길이를 미리 저장해놓고 이것보다 짧을 때만 정답 갱신
                    answer = [start_idx, end_idx]
                    seq_len = end_idx - start_idx
                break
    
    return answer

print(solution([1,2,3,4,5], 7)) # [2,3]
print(solution([1,1,1,2,3,4,5], 5)) # [6,6]
print(solution([2,2,2,2,2], 6)) # [0,2]