"""
풀이 시작 : 2023-09-04 23:40

- 문제 조건
    - records의 길이는 1,000 이하이므로, n^2까지 고려해봐도 될 것 같다.

- 문제 풀이
    - 입차 시 dict에 입차 내역을 기록, 출차 시 dict의 내역을 바탕으로 시간 계산
    - 시간은 차번 별 시간을 기록할 별도의 dict 활용
    - 하루 동안의 모든 주차 내역을 합산 후 요금을 계산하여야 함.
    - 최종적으로 합산 된 주차 시간으로 요금 계산 후, 차번 오름차순으로 요금 반환

풀이 완료 : 2023-09-05 00:40(1시간 소요)

"""
from typing import List
from collections import defaultdict


def get_fee(during_time: int, fees: List[int]) -> int:
    """
    최종 주차 시간을 바탕으로 fees 조건에 맞게 주차 요금을 계산한다.
    """
    if during_time <= fees[0]:  # 기본 주차 시간보다 적은 경우
        return fees[1]  # 기본 주차 요금 반환
    else:  # 기본 주차 시간보다 많은 경우
        tmp = fees[1]  # 기본 주차 시간, 요금 합산
        during_time -= fees[0]
        tmp += fees[3] * (during_time // fees[2])  # 추가 주차시간, 요금 합산
        tmp += fees[3] if during_time % fees[2] != 0 else 0  # 나누어 떨어지지 않으면 추가 요금 1회분 추가
        return tmp


def get_during_time(in_time: str, out_time: str) -> int:
    """
    입차 시간, 출차 시간을 바탕으로 주차 되어있던 시간을 min 단위로 변환한다.
    """
    in_hour, in_min = map(int, in_time.split(":"))
    out_hour, out_min = map(int, out_time.split(":"))

    return (out_hour - in_hour) * 60 + (out_min - in_min)  # 분 단위로 변환하여 반환


def solution(fees: List[int], records: List[str]) -> List[int]:
    """
    하루 동안의 최종 주차 시간을 바탕으로 주차 요금을 계산하여 차량 번호의 오름차순으로 반환한다.
    최종 주차 시간을 계산해야 하므로, 특정 차량의 모든 주차 내역(시간)을 합산한 후 요금을 계산해야 한다.

    record_dict : 특정 차량이 현재 입차된 시간을 담을 dictionary
    time_dict : 특정 차량의 하루 간 전체 입차 시간을 담을 dictionary(defalut dict)
    result_dict : 특정 차량의 합산 주차 요금을 담을 dictionary(default dict)
    """
    record_dict = {}
    time_dict = defaultdict(int)
    result_dict = defaultdict(int)

    for record in records:
        time, car_num, _ = record.split()
        if car_num in record_dict:  # 기존 입차된 내역이 있으면(출차)
            time_dict[car_num] += get_during_time(
                record_dict[car_num], time
            )  # 해당 시각까지 주차된 시간을 계산하여 저장
            del record_dict[car_num]  # 입차 내역 삭제
        else:  # 기존 입차된 내역이 없으면(입차)
            record_dict[car_num] = time  # 입차 내역 기록

    for key, value in record_dict.items():  # 하루가 끝났을 떄 입차 내역은 있는데, 출차 내역은 없는 경우
        time_dict[key] += get_during_time(value, "23:59")  # 23시 59분 출차로 계산

    for key, value in time_dict.items():  # 모든 차량의 주차 시간 기록을 바탕으로 주차요금 계산
        result_dict[key] += get_fee(value, fees)

    return [fee for _, fee in sorted(result_dict.items())]  # 차량 번호의 오름차순으로 정렬하여 반환


def main() -> None:
    case1 = [
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
    ]
    case2 = [
        [120, 0, 60, 591],
        [
            "16:00 3961 IN",
            "16:00 0202 IN",
            "18:00 3961 OUT",
            "18:00 0202 OUT",
            "23:58 3961 IN",
        ],
    ]
    case3 = [[1, 461, 1, 10], ["00:00 1234 IN"]]

    print(solution(*case1))  # [14600, 34400, 5000]
    print(solution(*case2))  # [0, 591]
    print(solution(*case3))  # 	[14841]


main()
