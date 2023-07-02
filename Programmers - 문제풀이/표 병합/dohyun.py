def solution(commands):
    """
    
    풀이시간
    - 약 1시간 30분 가량 풀다가 답지를 보는게 나을 것 같아서 기존 풀이와 가장 비슷한 풀이 참고
      https://magentino.tistory.com/69

    접근법
    - r, c 는 좌표가 아닌 "번째" 를 말하고 있으므로 좌표로 해석하려면 1 을 빼줘야함
    - 표를 어떻게 표현해야할까? -> 그냥 행렬로 생각하고 빈 값은 "NULL" 로 표현하기로 약속하자
    - merge 를 어떻게 표현할까가 애매하다고 생각했는데, 값 뒤에 "_merged" 를 붙혀서 표기해보자고 생각
        - 또한 merge 조건이 복잡하므로 실수하지않고 잘 구현하겠다 생각
    - 전체적으로 복잡도가 적으므로 완전탐색 느낌으로 구현을 시작해도 될 것 같음

    회고
    - 인덱스를 관리하는 배열 (merged), 값을 관리하는 배열 (board)
      - 각 배열을 따로 만들어서 해결한 점이 인상적 -> 해당 방법으로 Merge 를 해결할 수 있었음

    """

def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    board = [["EMPTY"] * 50 for _ in range(50)]
    for command in commands:
        command = command.split(' ')
        if command[0] == 'UPDATE':
            if len(command) == 4:   # UPDATE r c value 조건
                r,c,value = int(command[1])-1,int(command[2])-1,command[3]  # command 분리
                x,y = merged[r][c]  # 인덱스 추출
                board[x][y] = value
            elif len(command) == 3: # UPDATE value1 value2 조건
                value1, value2 = command[1], command[2] # command 분리
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2    
        elif command[0] == 'MERGE':
            r1,c1,r2,c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1    # command 분리
            x1,y1 = merged[r1][c1]  # 인덱스 추출
            x2,y2 = merged[r2][c2]  # 인덱스 추출
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]   # 비어있는 값은 merge 할 때 존재하는 값으로 대체
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)  # merge 되었다는 것을 인덱스로 표현
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1,int(command[2])-1  # command 분리
            x, y = merged[r][c] #  인덱스 추출
            tmp = board[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x,y):
                        merged[i][j] = (i,j)    # unmerge 하여 기존 인덱스로 대체 
                        board[i][j] = "EMPTY"
            board[r][c] = tmp
        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(board[x][y])
    return answer

command1 = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
command2 = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]

print(solution(command1))  # result : ["EMPTY", "group"]
print(solution(command2))  # result : ["d", "EMPTY"]