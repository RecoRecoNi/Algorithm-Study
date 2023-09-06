"""
    주차 요금 계산
    https://school.programmers.co.kr/learn/courses/30/lessons/92341

    풀이시간 
    10:31 ~ 11:05 (34분)

    문제 조건
    1 <= R(records) <= 1000

    시간 복잡도 : 
    O(R(레코드 검사) + R(출차 시간이 안 적혀진 차량) + R(정렬) + R(차량별 주차 요금 계산))
    
    O(4R) : 최대 O(4000)


    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 구현
    1. 방문한 시간을 체크하고 출차한 시간을 체크하여 테이블에 등록 후 출차 시 주차 시간 업데이트
        - 출차 기록이 없는 차량은 23:59분 기준으로 출차 처리
    
    2. 차량별 주차 시간을 계산하여 주차 요금 계산
"""
import math
from typing import List
from datetime import datetime
from collections import defaultdict


def solution(fees: List, records: List):
    # 주차 시간 반환을 위한 answer
    answer = []

    # 자동차의 총 주차 시간을 저장하는 테이블
    time_table = defaultdict(int)

    # 자동차의 입차와 출차를 기록하기 위한 dictionary
    ## set을 고려하였지만 차 번호와 입차 시간 두 가지를 기억해야했기에 불가피하게 dictionary를 사용했습니다.
    cars = defaultdict()

    # 1. 최대 1000개의 records를 통해 방문한 시간을 체크하고 출차한 시간을 체크하여 테이블에 등록 후 출차 시 주차 시간 업데이트
    for record in records:
        time, car_number, action = record.split()
        time = datetime.strptime(time, "%H:%M")
        # 입차 일 경우 입출차 관리 딕셔너리에 등록
        if action == "IN":
            cars[car_number] = time
        # 출차일 경우 주차 시간 관리 테이블에 주차 시간 저장 후 출차 처리
        else:
            diff = int((time - cars[car_number]).seconds / 60)
            time_table[car_number] += diff
            del cars[car_number]  # 출차 처리

    # records의 모든 처리가 끝난 후에도 남아있는 차량들은 23:59분 기준으로 출차 처리
    if cars:
        for key, value in cars.items():
            time = datetime.strptime("23:59", "%H:%M")
            diff = int((time - value).seconds / 60)
            time_table[key] += diff

    # 자동차 번호 순으로 정렬
    sorted_time_tabel = sorted(time_table.items())

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    base_time, base_fees, unit_time, unit_fees = fees

    # 주차 요금 계산
    for _, time in sorted_time_tabel:
        if time <= base_time:
            answer.append(base_fees)
        else:
            answer.append(
                base_fees + math.ceil((time - base_time) / unit_time) * unit_fees
            )

    return answer


case1 = (
    [180, 5000, 10, 600],
    [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT",
    ],
)
case2 = (
    [120, 0, 60, 591],
    [
        "16:00 3961 IN",
        "16:00 0202 IN",
        "18:00 3961 OUT",
        "18:00 0202 OUT",
        "23:58 3961 IN",
    ],
)
case3 = (
    [1, 461, 1, 10],
    ["00:00 1234 IN"],
)
print(solution(*case1))
print(solution(*case2))
print(solution(*case3))
