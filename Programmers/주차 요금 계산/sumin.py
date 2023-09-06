"""
풀이시간: 20분

<input>
- fees: 주차 요금 (fees의 길이 = 4)
    - fees[0]: 기본 시간(분)
    - fees[1]: 기본 요금(원)
    - fees[2]: 단위 시간(분)
    - fees[3]: 단위 요금(원)

- records: 자동차의 입/출차 내역 (1 ≤ records의 길이 ≤ 1,000)
    - 시각, 차량번호, 내역

<solution>
- 단순 구현!!

<시간 복잡도>
O(NlogN): 전체 코드 중 정렬이 가장 많은 시간 소요됨
"""

import math


def solution(fees, records):
    """
    fees: 주차요금
    records: 자동차 입/출차내역
    """
    answer = [] # 차량번호가 작은 자동차부터 청구할 주차 요금
    basic_time, basic_fee, unit_time, unit_fee = fees
    # 전체 차량
    cars = {}

    for record in records:
        time, num, status = record.split()
        time = int(time[:2]) * 60 + int(time[3:]) # 시간을 분 단위로 변환
        if num not in cars:
            cars[num] = []
        cars[num].append(time)

    # 출차 기록이 없으면 23:59에 출차된 것으로 간주
    for car, times in sorted(cars.items()):
        if len(times) % 2 != 0: # 입/출차 내역이 홀수이면 출차를 하지 않은 것
            cars[car].append(24*60-1)

        minutes = 0 # 누적 주차 시간(분)
        while times:
            out_time = times.pop() # 출차 시간
            in_time = times.pop() # 입차 시간
            minutes += out_time - in_time

        # 누적 주차 요금
        if minutes <= basic_time: # 기본시간 이하 -> 기본 요금
            total_fee = basic_fee
        else: # 기본 요금 + 단위 요금
            total_fee = basic_fee + math.ceil((minutes - basic_time) / unit_time) * unit_fee

        answer.append(total_fee)

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.08ms, 10.4MB)
테스트 5 〉	통과 (0.27ms, 10.3MB)
테스트 6 〉	통과 (0.31ms, 10.3MB)
테스트 7 〉	통과 (1.53ms, 10.5MB)
테스트 8 〉	통과 (0.85ms, 10.5MB)
테스트 9 〉	통과 (0.18ms, 10.5MB)
테스트 10 〉	통과 (1.27ms, 10.6MB)
테스트 11 〉	통과 (1.96ms, 10.8MB)
테스트 12 〉	통과 (2.07ms, 10.7MB)
테스트 13 〉	통과 (0.04ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
"""