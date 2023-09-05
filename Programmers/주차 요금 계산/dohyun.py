"""

풀이시간
- 약 37분

접근법
- records 의 길이가 1000 이하 -> 시간 복잡도 고려 X
- 시간:분 포맷을 분 단위로 변환해야 편할 듯함
- 출차 기록이 없는 친구들이 조금 까다로울 듯 한데, IN 개수와 OUT 개수가 안맞으면 23:59 출차를 추가하면 될듯
    - 이를 차량번호의 출차기록의 length 가 홀수인지 체크함으로서 구함
- 딕셔너리를 만들어 키값으로 차량번호를 넣으면 키값으로 정렬된 딕셔너리를 통해 반복문으로 풀 수 있을 듯함

회고
- 시각이 기본적으로 정렬되어 있어서 단순 append 나 출차 기록 예외처리 등이 수월했던 것 같음
- 중간중간 잔고장(?) 이 나서 시간이 조금 더 오래걸렸던 것 같은데 해볼만하다고 느낄수록 꼭 집중 놓지말기

"""

import math

def solution(fees, records):
    base_time, base_fee, per_time, per_fee = fees[0], fees[1], fees[2], fees[3]
    answer = []

    records_dict = {}
    
    for record in records: # 입력값 전처리
        time, car_num, inout = record.split()
        time = int(time[:2]) * 60 + int(time[3:]) # 시간을 분단위 포맷으로 변환
        
        if car_num in records_dict: # 레코드를 dictionary 형태로 바꾼 후 value 로는 time 을 입력
            records_dict[car_num].append(time)
        else:
            records_dict[car_num] = [time]
    
    for key, item in sorted(records_dict.items()): # 차량번호 순으로 정렬된 값을 뱉어야하므로 정렬
        if len(item)%2 == 1: # 출차기록이 없으면 (즉 길이가 홀수)
            item.append(23*60 + 59) # 23:59분 출차기록 추가

        cum_time = 0
        for idx in range(0, len(item), 2): # 이미 정렬되어 있으므로 입차, 출차를 해당 반복문으로 구함
            cum_time += (item[idx+1] - item[idx])
        
        if cum_time <= base_time: # 누적시간이 기본시간보다 작으면 기본요금 부과
            answer.append(base_fee)
        else: # 그렇지 않으면 원래 계산 공식대로 부과
            fee = base_fee + math.ceil((cum_time - base_time) / per_time) * per_fee
            answer.append(fee)

    return answer