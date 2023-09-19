"""
풀이 시작 : 2023-09-19 10:40

#### 제한 사항
- record의 길이는 100,000 이하이므로 O(NlogN) 이하의 알고리즘을 설계해야 한다.

#### 풀이
- 채팅방 입/퇴장 시 이름 메시지 출력
- 이름바꿔 들어오면 기존 메시지 이름도 바뀜 : 메시지와 사용자 정보를 끝까지 가지고 있어야 함
- 닉넴 중복 허용

- record를 총 두 번 탐색해, 첫 탐색에서 user id 별 최종 닉네임을 탐색하고, 두 번째 탐색에서 메시지를 출력한다.
- O(2N)으로 해결 가능하다. (startswith(str)는 앞에서부터 str 만큼만 비교하므로 상수 시간으로 계산)

풀이 완료 : 2023-09-19 10:55 (풀이 시간 : 15분 소요)
"""
from typing import List


def solution(record: List[str]) -> List[str]:
    """
    채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
    모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 한다.
    """
    id2name = {}  # user_id 별 닉네임을 담을 dict
    result = []  # 최종 메시지를 담을 list

    for info in record:  # user_id 별 이름 get
        if not info.startswith("Leave"):  # 이름이 바뀔 수 있는 경우는 다시 들어오거나 Change인 경우
            _, user_id, name = info.split()
            id2name[user_id] = name

    for info in record:  # Enter인지, Leave인지에 따라 메시지를 담는다.
        if info.startswith("Enter"):
            _, user_id, _ = info.split()
            result.append(f"{id2name[user_id]}님이 들어왔습니다.")
        elif info.startswith("Leave"):
            _, user_id = info.split()
            result.append(f"{id2name[user_id]}님이 나갔습니다.")

    return result


def main() -> None:
    case1 = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]

    print(
        solution(case1)
    )  # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


main()
