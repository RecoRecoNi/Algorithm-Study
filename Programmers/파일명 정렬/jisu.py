"""
풀이 시작 : 2023-10-03 18:46

#### 제한 사항
- files는 1000개 이하
- 각 파일 명은 100글자 이하
- 1000 * 100 -> 100000... 완탐은 간당간당하거나 안되겠다.
- 일단 구현에 초점을 두고 시작

#### 풀이
- 파일명을 HEAD, NUMBER, TALE로 split후 조건에 맞춰 정렬하면 되겠다.
- 정규표현식? 2개는 되는데 3개는 어떻게 자르지?
- 문제에서 문자 이후 숫자 나오는 게 보장되어 있으므로, 그냥 순회하여 idx를 활용
- split 후 조건에 맞춰 정렬, 정렬과정에서 실제 변환은 없어야 한다.

풀이 완료 : 2023-10-03 19:13 (풀이 시간 : 27분)
"""
from typing import List, Tuple


def files_name_split(file_name: str) -> Tuple[str]:
    """
    문제에서 문자 이후 숫자 나오는 게 보장되어 있으므로, idx를 활용해 split을 수행한다.
    """
    head_done = False
    number_done = False
    head, number, tail = "", "", ""
    for idx, ch in enumerate(file_name):
        if not head_done and ch.isdigit():  # 처음 숫자 나오기 이전까지 head
            head = file_name[:idx]
            number_idx_init = idx  # number 시작 idx
            head_done = True
        if head_done and not ch.isdigit():  # 처음 숫자 까지가 number
            number = file_name[number_idx_init:idx]
            tail = file_name[idx:]
            number_done = True
            break

    if not number_done:  # 파일명 끝까지가 number인 경우 예외처리
        number, tail = file_name[number_idx_init:], ""

    return (head, number, tail)


def solution(files: List[str]) -> List[str]:
    """
    파일명 split 후 조건에 맞춰 정렬하여 리스트로 반환한다.
    """
    files_split = list(map(files_name_split, files))  # 파일명 전체 split
    files_split.sort(key=lambda x: (x[0].lower(), int(x[1])))  # 조건에 맞춰 정렬 (실제 변환 x)

    return ["".join(file) for file in files_split]  # 정렬된 파일명 출력


def main() -> None:
    case1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    case2 = [
        "F-5 Freedom Fighter",
        "B-50 Superfortress",
        "A-10 Thunderbolt II",
        "F-14 Tomcat",
    ]

    print(solution(case1))
    print(solution(case2))


main()
