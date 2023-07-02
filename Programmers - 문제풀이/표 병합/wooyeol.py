"""
    표 병합
    https://school.programmers.co.kr/learn/courses/30/lessons/150366
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> merge를 할 때 연결 리스트와 같은 형태로 진행하기

    commands 최대 1000번
    find : avg - 2번
    print : O(1)
    update : O(2500) or O(1 + alpha)
    merge : O(2500 + alpha)
    unmerge : O(2500 + alpha)
"""


def find(merged, row, col):
    """
    연결 리스트의 마지막 요소 반환
    """
    if (row, col) == merged[row][col]:
        return merged[row][col]

    row_m, col_m = merged[row][col]
    merged[row][col] = find(merged, row_m, col_m)
    return merged[row][col]


def update_value(tables, target1, target2):
    for row in range(50):
        for col in range(50):
            if tables[row][col] == target1:
                tables[row][col] = target2


def solution(commands):
    answer = []

    # table 생성 50 x 50 크기 선언
    tables = [["EMPTY" for _ in range(50)] for _ in range(50)]

    # merge table 연결 리스트 개념
    merged = [[(i, j) for j in range(50)] for i in range(50)]

    # Command 하나씩 처리하기
    for command in commands:
        command = command.split()

        # Print
        if command[0] == "PRINT":
            # 연결리스트의 마지막 요소 Print
            row, col = int(command[1]) - 1, int(command[2]) - 1
            x, y = find(merged, row, col)
            answer.append(tables[x][y])

        # Update
        elif command[0] == "UPDATE":
            # length = 3일 때 update는 모든 값 없데이트
            if len(command) < 4:
                update_value(tables, command[1], command[2])
            # length = 4일 때 update 해당 cell
            else:
                # 연결리스트의 마지막 요소 Update
                row, col = int(command[1]) - 1, int(command[2]) - 1
                x, y = find(merged, row, col)
                tables[x][y] = command[3]

        # Merge
        elif command[0] == "MERGE":
            row1, col1, row2, col2 = (
                int(command[1]) - 1,
                int(command[2]) - 1,
                int(command[3]) - 1,
                int(command[4]) - 1,
            )
            x1, y1 = find(merged, row1, col1)
            x2, y2 = find(merged, row2, col2)

            # 각 연결 리스트의 마지막 요소를 병합
            if tables[x1][y1] == "EMPTY":
                tables[x1][y1] = tables[x2][y2]

            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)

        # UNMERGE
        elif command[0] == "UNMERGE":
            row, col = int(command[1]) - 1, int(command[2]) - 1
            x, y = find(merged, row, col)

            # 연결 리스트의 마지막 요소들이 같은 요소들을 병합 해제 후 입력받은 인덱스에는 원래 값 저장
            value = tables[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        tables[i][j] = "EMPTY"
            tables[row][col] = value

    return answer


def solution_fail(commands):
    answer = []

    # table 생성 50 x 50 크기 선언
    tables = [["EMPTY" for _ in range(50)] for _ in range(50)]

    # merge table
    merged = []

    # Command 하나씩 처리하기
    for command in commands:
        # command를 분해 후 명령어 구분을 위한 요소 갯수 확인
        command = command.split()
        length = len(command)

        # Print
        if command[0] == "PRINT":
            row, col = int(command[1]) - 1, int(command[2]) - 1
            answer.append(tables[row][col])

        # Update
        elif command[0] == "UPDATE":
            # length = 3일 때 update는 모든 값 없데이트
            if length < 4:
                update_value(tables, command[1], command[2])
            # length = 4일 때 update 해당 cell
            else:
                row, col = int(command[1]) - 1, int(command[2]) - 1
                tables[row][col] = command[3]

        # Merge
        elif command[0] == "MERGE":
            flag = True
            row1, col1, row2, col2 = (
                int(command[1]) - 1,
                int(command[2]) - 1,
                int(command[3]) - 1,
                int(command[4]) - 1,
            )
            # merge 그룹을 확인하면 해당 그룹에 셀 추가하기
            for idx, merge in enumerate(merged):
                if (row1, col1) in merge:
                    flag = False
                    # merge 하는 셀들에 같은 값 대입하기
                    tables[row2][col2] = tables[row1][col1]
                    # merged에 merge되는 모든 셀을 list에 추가하기
                    merged[idx].append((row2, col2))
                    # merged를 진행할 때 가장 인덱스가 먼저 올 수 있도록 정렬
                    # merged[idx].sort(key=lambda x: (x[0], x[1]), reverse=True)
                    break

            # 만약 그룹을 확인하지 못했다면 리스트 추가
            if flag:
                merged.append([(row1, col1), (row2, col2)])

        # UNMERGE
        elif command[0] == "UNMERGE":
            for idx, merge in enumerate(merged):
                row, col = int(command[1]) - 1, int(command[2]) - 1
                if (row, col) in merge:
                    merge.remove((row, col))
                    for r, c in merge:
                        tables[r][c] = "EMPTY"
                merged.pop(idx)

    #     print(merged)

    # print("######### table #########")
    # for table in tables:
    #     print(table)

    return answer


# ["EMPTY", "group"]
input1 = [
    "UPDATE 1 1 menu",
    "UPDATE 1 2 category",
    "UPDATE 2 1 bibimbap",
    "UPDATE 2 2 korean",
    "UPDATE 2 3 rice",
    "UPDATE 3 1 ramyeon",
    "UPDATE 3 2 korean",
    "UPDATE 3 3 noodle",
    "UPDATE 3 4 instant",
    "UPDATE 4 1 pasta",
    "UPDATE 4 2 italian",
    "UPDATE 4 3 noodle",
    "MERGE 1 2 1 3",
    "MERGE 1 3 1 4",
    "UPDATE korean hansik",
    "UPDATE 1 3 group",
    "UNMERGE 1 4",
    "PRINT 1 3",
    "PRINT 1 4",
]

# ["d", "EMPTY"]
input2 = [
    "UPDATE 1 1 a",
    "UPDATE 1 2 b",
    "UPDATE 2 1 c",
    "UPDATE 2 2 d",
    "MERGE 1 1 1 2",
    "MERGE 2 2 2 1",
    "MERGE 2 1 1 1",
    "PRINT 1 1",
    "UNMERGE 2 2",
    "PRINT 1 1",
]

sample = ["UPDATE 1 1 menu", "UPDATE menu table", "PRINT 1 1"]

print(solution(sample))
print(solution(input1))
print(solution(input2))


# 테스트 1 〉	통과 (1.48ms, 10.6MB)
# 테스트 2 〉	통과 (1.33ms, 10.5MB)
# 테스트 3 〉	통과 (0.67ms, 10.4MB)
# 테스트 4 〉	통과 (0.38ms, 10.3MB)
# 테스트 5 〉	통과 (0.91ms, 10.5MB)
# 테스트 6 〉	통과 (1.85ms, 10.5MB)
# 테스트 7 〉	통과 (1.21ms, 10.4MB)
# 테스트 8 〉	통과 (1.78ms, 10.4MB)
# 테스트 9 〉	통과 (5.32ms, 10.5MB)
# 테스트 10 〉	통과 (9.99ms, 10.6MB)
# 테스트 11 〉	통과 (9.06ms, 10.4MB)
# 테스트 12 〉	통과 (21.33ms, 10.5MB)
# 테스트 13 〉	통과 (59.45ms, 10.6MB)
# 테스트 14 〉	통과 (69.69ms, 10.4MB)
# 테스트 15 〉	통과 (87.86ms, 10.4MB)
# 테스트 16 〉	통과 (90.58ms, 10.6MB)
# 테스트 17 〉	통과 (118.69ms, 10.6MB)
# 테스트 18 〉	통과 (125.62ms, 10.6MB)
# 테스트 19 〉	통과 (107.99ms, 10.6MB)
# 테스트 20 〉	통과 (170.92ms, 10.6MB)
# 테스트 21 〉	통과 (234.63ms, 10.6MB)
# 테스트 22 〉	통과 (100.80ms, 10.6MB)
