"""
- [프로그래머스 - 표 병합](https://school.programmers.co.kr/learn/courses/30/lessons/150366)
- 소요 시간: 1시간 반 정도
- 접근 방법
 - update, print는 쉽게 문제 그대로 구현
 - merge 시 연결된 셀들을 집합으로 저장해두어 unmerge에 활용하려 했으나 실패
 - 계속 merge, unmerge을 제대로 구현하는 것에서 어려움을 겪어 [블로그](https://wondev.tistory.com/153) 참고
   - ufTable로 셀 위치를 따로 저장하는 테이블을 만들어 Union-Find로 merge, unmerge를 구현하는 것이 핵심
"""

answer = []
table = [["EMPTY" for _ in range(51)] for _ in range(51)] # 셀의 위치를 나타내는 r, c의 범위가 1~50 범위이므로 range(51)로 설정
ufTable = [[(r, c) for c in range(51)] for r in range(51)] # Union-Find에 사용할, 셀 위치 테이블


def update(r, c, value):
    nr, nc = find(r, c) # 연결(병합)된 제일 상위 root 셀을 찾음
    table[nr][nc] = value

    
def updateValue(value1, value2):
    # 모든 셀의 값을 검색하며 update
    for i in range(51):
        for j in range(51):
            if table[i][j] == value1:
                table[i][j] = value2

                
def merge(r1, c1, r2, c2):
    nr1, nc1 = find(r1, c1)
    nr2, nc2 = find(r2, c2)
    
    if table[nr1][nc1] != "EMPTY": # (r1, c1)에 값이 있는 경우, (r1, c1)의 값으로 병합
        union(nr1, nc1, nr2, nc2) # 셀 위치 (r2, c2)를 (r1, c1)로 대체
        
    else: # (r1, c1)에 값이 비어있고 (r2, c2)에만 값이 있는 경우, (r2, c2)의 값으로 병합
        if table[nr2][nc2] != "EMPTY":
            table[nr1][nc1] = table[nr2][nc2]
        
        union(nr1, nc1, nr2, nc2)

        
def unmerge(r, c):
    nr, nc = find(r, c)
    temp = table[nr][nc] # 병합 해제 전, (r, c) 위치의 셀의 값은 남겨둬야 하므로 저장해 둠

    # 병합 해제를 위해, 병합으로 연결된 셀들을 모두 찾아 list에 저장
    # * 찾을 때마다 바로 병합 해제를 하면, 연결된 모든 셀을 찾을 수 없으므로 저장해뒀다가 한번에 해제
    tempList = []
    for i in range(51):
        for j in range(51):
            if find(i, j) == (nr, nc):
                tempList.append((i, j))
    
    # 병합 해제 - 연결된 셀들의 값을 모두 초기화
    for t in tempList:
        i, j = t
        table[i][j] = "EMPTY" # 셀 값을 비워 초기화
        ufTable[i][j] = (i, j) # 본래 셀 위치를 갖도록 초기화

    table[r][c] = temp # 아까 저장해 둔 (r, c) 위치의 셀의 값 저장 


def print_(r, c):
    nr, nc = find(r, c)
    answer.append(table[nr][nc])

    
# Union-Find
def find(r, c):
    if (r, c) == ufTable[r][c]: # 병합되어 있지 않은 경우, 혹은 병합된 셀들의 root 셀인 경우
        return ufTable[r][c]

    nr, nc = ufTable[r][c] # 병합된 셀인 경우, root 셀을 재귀적으로 계속 찾아 나감
    ufTable[r][c] = find(nr, nc)
    return ufTable[r][c]
 

def union(r1, c1, r2, c2):
    ufTable[r2][c2] = ufTable[r1][c1]


def solution(commands):
    for command in commands:
        cmd = command.split()
        
        # update
        if cmd[0] == "UPDATE": # 명령어 형식이 2가지

            if len(cmd) == 4: 
                # 명령어 형식 : "UPDATE r c value"
                update(int(cmd[1]), int(cmd[2]), cmd[3])

            else:             
                # 명령어 형식 : "UPDATE value1 value2"
                updateValue(cmd[1], cmd[2])

        
        # merge
        elif cmd[0] == "MERGE": 
            # 명령어 형식 : "MERGE r1 c1 r2 c2"
            merge(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))


        # unmerge
        elif cmd[0] == "UNMERGE": 
            # 명령어 형식 : "UNMERGE r c"
            unmerge(int(cmd[1]), int(cmd[2]))
            
        # print               
        elif cmd[0] == "PRINT": 
            # 명령어 형식 : "PRINT r c"
            print_(int(cmd[1]), int(cmd[2]))

            
    return answer
