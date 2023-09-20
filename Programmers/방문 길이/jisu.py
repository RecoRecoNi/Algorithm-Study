"""
풀이 시작 : 2023-09-20 10:24

#### 제한사항 : dirs(명령어 수)는 500, 상관 없을 것 같다.

#### 풀이
- 수동 BFS..?
- 이동하면서 matrix에다가 방문 체크를 하고, matrix 범위 내 방문 체크가 안되어있는 곳을 밟을 때 카운트
- -5~5범위를 -> 0 ~ 10로 대체
- 주의할 점
    - 특정 점을 새로 방문했는지의 여부가 아닌, 그 길을 처음 갔는지에 대해서이다.
    - 좌표 별 어디서 그 좌표에 도달했는지 set으로 관리한다.
        - (0, 0) -> (1, 1)로 갔다면 (1, 1)의 set에 (0, 0)을 add
        - 이때 (1, 1) -> (0, 0)도 같은 길이므로 (0, 0)의 set에 (1, 1)도 add

풀이 완료 : 2023-09-20 10:49 (풀이 시간 : 25분)
"""


def solution(dirs: str) -> int:
    matrix = [[set() for _ in range(11)] for _ in range(11)]
    y, x = 5, 5  # 초기 위치
    directions = {
        direction: dydx
        for direction, dydx in zip("UDLR", [(-1, 0), (1, 0), (0, -1), (0, 1)])
    }  # 이동 방향 별 움직여야 할 좌표
    cnt = 0

    for direction in dirs:
        dy, dx = directions[direction]
        if 0 <= y + dy < 11 and 0 <= x + dx < 11:  # 다음 좌표가 범위 내이면
            by, bx = y, x  # 이동 전 좌표
            y += dy  # 이동 후 좌표
            x += dx
            if not (by, bx) in matrix[y][x]:  # 처음 걸어보는 길이면
                cnt += 1
                matrix[y][x].add((by, bx))  # 이전 좌표 -> 현재 좌표 방문 처리
                matrix[by][bx].add((y, x))  # 현재 좌표 -> 이전 좌표도 같은 길이므로 방문 처리

    return cnt


def main() -> None:
    case1 = "ULURRDLLU"
    case2 = "LULLLLLLU"
    case3 = "UDUDUDUDU"

    print(solution(case1))  # 7
    print(solution(case2))  # 7
    print(solution(case3))  # 7


main()
