"""
- 표의 크기는 50x50, commands의 길이는 최대 1000이므로 구현만 해내면 크게 문제는 없을 것 같았음
- 소요시간
    - 1차 접근 : 1시간
    - 레퍼런스 참고 및 Union-Find 코드 이해 : 1시간
    - 레퍼런스 적용 : 1시간
- 1차 접근
    - MERGE 방식을 다음의 두 dict와 Merged Point를 관리하는 list를 활용하여 구현
        - pv dict : key - point, value - value
        - vp dict : key - value, value - set(points)
        - merged_list : list(merge points list(merged points))
    - 뭐라는지 모르겠죠? 저도 하다가 헷갈려서 엎었습니다.
- 레퍼런스 참고
    - [레퍼런스](https://magentino.tistory.com/69)에서 MERGE & UNMERGE에 대한 KEY IDEA는 union&find임을 알게 됨
    - [Union-Find 알고리즘](https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html)
    - Disjoint set을 표현하는 알고리즘인 Union-Find 방식을 이해하고 구현할 수 있게 됨
- 적용
    - 주석과 위 레퍼런스 참고
    - Disjoint Set의 표현 방식인 Union-Find를 이해해야 해당 풀이가 이해됩니다!
"""

table = [['' for _ in range(51)] for _ in range(51)]    # r, c 좌표를 그대로 사용하기 위해 51x51로 선언
P = [[(r, c) for c in range(51)] for r in range(51)]    # Union-Find Parent Table(find 함수에서 자세히 설명)
                                                        # 좌표가 루트인 경우 자신의 값을 가짐, 병합된 경우 상위 좌표를 가짐
answer = []     # 출력을 담을 정답 리스트

def PRINT(r, c):
    """
    - (r, c) 위치의 셀을 선택하여 셀의 값을 출력, 선택한 셀이 비었을 경우 "EMPTY를 출력한다."
    - 셀이 병합된 경우 루트 좌표만 값을 가지고 있으므로 find를 통해 루트 좌표를 가져와서 해당 값을 출력해야 한다.
    - 출력은 answer 리스트에 담는 것으로 대체한다.
    """
    r, c = int(r), int(c)
    r, c = find(r, c)       # 셀이 병합된 경우 루트 좌표만 값을 가지고 있으므로 find를 통해 루트 좌표를 가져와서 해당 값을 출력
    answer.append(table[r][c]) if table[r][c] else answer.append("EMPTY")

def UPDATE_POINT(r, c, value):
    """
    - (r, c) 위치의 셀을 선택해 value로 값을 바꾼다.
    - 셀이 병합된 경우 루트 좌표만 값을 가지고 있으므로 find를 통해 루트 좌표를 가져와서 해당 값을 변경해야 한다.
    """
    r, c = int(r), int(c)
    r, c = find(r, c)       # 셀이 병합된 경우 루트 좌표만 값을 가지고 있으므로 find를 통해 루트 좌표를 가져와서 해당 값을 변경
    table[r][c] = value

def UPDATE_VALUE(v1, v2):
    """
    - v1을 값으로 가지고 있는 모든 셀의 값을 v2로 변경
    - 51x51 크기이므로 bruth force로 가능
    - 셀이 병합된경우 루트 좌표만 값을 가지고 있으므로 현재 루트이면서, 값이 v1인 셀들을 변경해줘야함
    - 루트 노드를 찾기 위한 find가 여기서도 역시 필요하다.
    """
    for row in range(51):
        for col in range(51):
            pr, pc = find(row, col)     # 셀이 병합된경우 루트 좌표만 값을 가지고 있으므로
            if table[pr][pc] == v1:     # 현재 루트이면서, 값이 v1인 셀들을 변경해줘야함
                table[pr][pc] = v2

def find(r, c):
    """
    - Parent table `P`의 각 셀은 좌표를 값으로 가지고 있음
    - 셀의 위치와 값이 같은 경우 해당 좌표는 루트 노드
    - 다른 좌표를 값으로 가진 경우 해당 값은 상위(부모)노드의 좌표이며, 값은 상위(부모) 노드를 따라감
    - find는 값으로 본인의 좌표를 가지는 루트 노드를 탐색해 루트 노드의 좌표를 반환함
    """
    r, c = int(r), int(c)
    while (r, c) != P[r][c]:        # 자기 자신의 좌표를 값으로 가지는 루트 노드가 나올 때까지
        r, c = P[r][c]              # 상위(부모) 노드를 타고 루트로 올라감
    return r, c                     # 루트 노드 좌표 반환

def union(r1, c1, r2, c2):
    """
    - 두 disjoint set의 루트 노드를 병합함 (r1, c1) <- (r2, c2)
    - (r1, c1), (r2, c2)는 각 set의 루트 노드임을 가정
    """
    P[r2][c2] = P[r1][c1]           # (r2, c2)의 Parent Table 값을 (r1, c1)으로 변경하므로써 두 노드 병합

def MERGE(r1, c1, r2, c2):
    """
    - (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합
    - (r1, c1) 위치에 값이 있으면 해당 셀의 값을 따라감
    - 두 좌표가 각각 병합되어있을 수 있으므로 find를 통해 두 좌표의 루트를 찾아 병합
    """
    r1, c1 = find(r1, c1)                       # 두 좌표가 각각 병합되어있을 수 있으므로 find를 통해 두 좌표의 루트를 찾아 병합
    r2, c2 = find(r2, c2)

    if r1==r2 and c1==c2 : return               # 같은 셀일 경우 무시
    if table[r1][c1]:
        union(r1, c1, r2, c2)                   # 위치에 값이 있으면 해당 셀의 값을 따라감
    else:
        union(r2, c2, r1, c1)

def UNMERGE(r, c):
    """
    - (r, c) 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제
    - 병합되어있던 모든 셀은 (r, c)를 제외하고 모두 초기값('')을 가짐
    - (r, c)는 기존 값을 가짐
    - 모든 좌표를 순회해 (r, c)의 루트 노드(pr, pc)의 하위 노드를 모두 초기화 해야 함
        - 이 때, 좌표를 먼저 모두 구한 후 다시 그 좌표들을 순회하는 순서로 초기화를 진행해야 함
        - 좌표를 구하면서 초기화를 진행하면 해당 좌표를 상위(부모)노드로 갖고 있던 좌표는 루트를 잃어버림 
    """
    r, c = int(r), int(c)
    pr, pc = find(r, c)                             # (r, c)의 부모노드 (pr, pc)
    value = table[pr][pc]
    unmerge_list = []

    for row in range(51):                           # (pr, pc)를 루트로 가지는 좌표를 먼저 모두 구한 후
        for col in range(51):
            if find(row, col) == (pr, pc):
                unmerge_list.append((row, col))          
    
    for row, col in unmerge_list:                   # 다시 그 좌표들을 순회하는 순서로 초기화를 진행
        P[row][col] = (row, col)
        table[row][col] = ''

    table[r][c] = value                             # (r, c)는 기존 값을 가짐

def solution(commands):
    for command in commands:
        command = command.split()
        if command[0] == 'PRINT':               # PRINT
            _, r, c = command                   # PRINT r c
            PRINT(r, c)  
        elif command[0] == 'UPDATE':            # UPDATE
            if len(command) == 4:               
                _, r, c, value = command        # case 1 : UPDATE r c value
                UPDATE_POINT(r, c, value)
            else:                               
                _, v1, v2 = command             # case 2 : UPDATE value1 value2
                UPDATE_VALUE(v1, v2)
        elif command[0] == 'MERGE':             # MERGE
            _, r1, c1, r2, c2 = command         # MERGE r1, c1, r2, c2
            MERGE(r1, c1, r2, c2)
        elif command[0] == 'UNMERGE':           # UNMERGE
            _, r, c = command                   # UNMERGE r c
            UNMERGE(r, c)

    return  answer

if __name__ == '__main__':
    case1 = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
    case2 = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
    print(solution(case1))  # ["EMPTY", "group"]
    answer = []
    print(solution(case2))  # ["d", "EMPTY"]