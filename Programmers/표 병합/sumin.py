"""
시간: 1시간

<조건>
- 50x50의 표는 초기에 모든 셀이 비어있음
- 각 셀은 문자열 값을 가질 수 있고, 다른 셀과 병합될 수 있음

<input>
commands: 실행할 명령어들이 담긴 1차원 문자열 배열 (1 ≤ commands의 길이 ≤ 1,000)
- UPDATE r c value
- UPDATE value1, value2
- MERGE r1 c1 r2 c2
- UNMERGE r c
- PRINT r c

<solution>
구현 문제(문제가 어렵다기보다는 구현할 조건이 많아서 귀찮음.. 테케 13, 14에서 15분 넘게 쓴 것 같음)
- 어떤 자료형으로 접근할 것인가?
    - 딕셔너리? 2차원 배열?
    - 50x50이라 둘 다 TLE는 안 뜰거같아서 걍 딕셔너리로 풀이함
    - 시간복잡도: O(commands의 크기 * N^2) -> 최대 1000 * 50 * 50 = 2,500,000

- 다른 사람들 풀이를 보다보니 대부분 union-find로 풀이했길래 union-find로도 풀어 볼 예정
"""

# 딕셔너리로 푼 풀이
def solution(commands):
    answer = []
    chart = {} # 표
    merge = {} # 병합상태
    for i in range(1, 51): # 표의 크기는 50x50
        for j in range(1, 51):
            chart[(i, j)] = "EMPTY" # 초기에 모든 셀은 비어있음
            merge[(i, j)] = (i, j) # 모든 셀이 병합돼있지 않음

    for com in commands: # 명령어 하나씩 확인
        command = com.split()[0] # 공백을 기준으로 나눔
        # 1. UPDATE
        if command == 'UPDATE':
            # 1-1. UPDATE r c value
            if len(com.split()) == 4:
                # (r,c) 위치의 셀의 값을 value로 바꿔준다.
                _, r, c, value = com.split()
                r, c = int(r), int(c)
                x, y = merge[(r, c)]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if merge[(i, j)] == (x, y):
                            chart[(i, j)] = value
            # 1-2. UPDATE value1 value2
            else:
                _, value1, value2 = com.split()
                for i in range(1, 51):
                    for j in range(1, 51):
                        if chart[(i, j)] == value1:
                            chart[(i, j)] = value2

        # 2. MERGE r1 c1 r2 c2
        if command == 'MERGE': # (r1, c1) 셀과 (r2, c2) 셀을 병합
            r1, c1, r2, c2 = map(int, com.split()[1:])
            x1, y1 = merge[(r1, c1)]; x2, y2 = merge[(r2, c2)]

            if (x1, y1) != (x2, y2): # 두 위치의 셀이 같은 셀일 경우 무시 -> 두 위치의 셀이 다른 셀일 경우만 merge
                # 인접하지 않을 경우, 두 셀만 영향을 받으며 그 사이에 위치한 셀들은 영향을 받지 않는다.
                merge[(r2, c2)] = x1, y1
                for i in range(1, 51):
                    for j in range(1, 51):
                        if merge[(i, j)] == (x2, y2):
                            merge[(i, j)] = (x1, y1)

                if chart[(x1, y1)] != 'EMPTY': # (r1, c1)값이 있으면 그 값으로 변경
                    chart[(x2, y2)] = chart[(x1, y1)]
                else: # (r1, c1)값이 없으면 (r2, c2)값으로 변경
                    chart[(x1, y1)] = chart[(x2, y2)]

        # 3. UNMERGE r c
        if command == 'UNMERGE':
            r, c = map(int, com.split()[1:])
            x, y = merge[(r, c)]
            tmp = chart[(x, y)]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[(i, j)] == (x, y):
                        merge[(i, j)] = (i, j)
                        chart[(i, j)] = 'EMPTY'
            chart[(r, c)] = tmp

        # 4. PRINT r c
        if command == 'PRINT':
            r, c = map(int, com.split()[1:])
            x, y = merge[(r, c)]
            answer.append(chart[(x, y)])

        # for i in range(1, 5):
        #     for j in range(1, 5):
        #         print(f"{(i, j)}: {merge[(i, j)]}")
        # print('---------------------------------------')

    return answer


"""
테스트 1 〉	통과 (7.46ms, 10.9MB)
테스트 2 〉	통과 (4.74ms, 11MB)
테스트 3 〉	통과 (3.42ms, 10.9MB)
테스트 4 〉	통과 (2.50ms, 10.8MB)
테스트 5 〉	통과 (4.83ms, 10.9MB)
테스트 6 〉	통과 (4.71ms, 11MB)
테스트 7 〉	통과 (8.41ms, 10.9MB)
테스트 8 〉	통과 (9.75ms, 10.8MB)
테스트 9 〉	통과 (25.05ms, 10.9MB)
테스트 10 〉	통과 (25.40ms, 10.8MB)
테스트 11 〉	통과 (21.52ms, 10.7MB)
테스트 12 〉	통과 (28.19ms, 10.8MB)
테스트 13 〉	통과 (232.66ms, 10.9MB)
테스트 14 〉	통과 (282.81ms, 11MB)
테스트 15 〉	통과 (285.42ms, 10.9MB)
테스트 16 〉	통과 (340.08ms, 11MB)
테스트 17 〉	통과 (451.50ms, 11MB)
테스트 18 〉	통과 (376.26ms, 10.9MB)
테스트 19 〉	통과 (346.04ms, 11MB)
테스트 20 〉	통과 (306.68ms, 11MB)
테스트 21 〉	통과 (313.23ms, 10.8MB)
테스트 22 〉	통과 (298.42ms, 11.1MB)
"""


