"""
    프렌즈4블록
    https://school.programmers.co.kr/learn/courses/30/lessons/17679

    풀이시간 
    15:12 ~ 16:02 (50분)
    
    문제 조건
    높이 M, 폭 N
    2<= n,m <= 30

    시간 복잡도 :
    O((N * M * 3) + (N * M) + (N * 2M))
    O(N * M)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 시뮬레이션

    - 삭제 연산을 진행하였을 때 기억되는 주소값이 하나도 없다면 업데이트가 불가능한 상황이므로 종료

    1. 4칸씩 삭제되는 주소 값 기억하기
        - 바로 삭제하면 동시에 적용되는 칸들이 생략될 수 있기 때문에

    2. 기억된 주소값을 모두 "-"으로 변경하기 (삭제 연산)

    3.  "-"로 표기된 Col을 가장 상단으로 올리기
        - 각 Column 별로 "-"의 개수를 카운트하고 가장 상단에서부터 "-"를 채우기
        - 이후 deque에 기억된 알파벳 순서대로 배치

    ex) 시뮬레이션 과정
    ----------- Case #2 -----------

    -------------------------------
    ------ 1. Before Removed ------
    T T T A N T
    R R F A C C
    R R R F C C
    T R R R A A
    T T M M M F
    T M M T T J

    ------ 1. After Removed ------
    T T T A N T
    - - F A - -
    - - - F - -
    T - - R A A
    T T M M M F
    T M M T T J

    ------ 1. After Pull ------
    - - - A - -
    - - - A - -
    T - T F N T
    T T F R A A
    T T M M M F
    T M M T T J

    -------------------------------
    ------ 2. Before Removed ------
    - - - A - -
    - - - A - -
    T - T F N T
    T T F R A A
    T T M M M F
    T M M T T J

    ------ 2. After Removed ------
    - - - A - -
    - - - A - -
    T - T F N T
    - - F R A A
    - - M M M F
    T M M T T J

    ------ 2. After Pull ------
    - - - A - -
    - - - A - -
    - - T F N T
    - - F R A A
    T - M M M F
    T M M T T J

    -------------------------------
    ------ 3. Before Removed ------
    - - - A - -
    - - - A - -
    - - T F N T
    - - F R A A
    T - M M M F
    T M M T T J

"""
from collections import deque
            
def solution(m, n, board):
    answer = 0
    
    while True:
        # 현재 턴에 삭제될 주소값 집합
        removed = set()

        # 4칸이 삭제가 가능한지 확인 후 삭제 집합에 삭제 가능한 칸들 추가
        def remove_same(x, y):
            # 오른쪽, 오른 대각 아래, 아래
            directions = ((1, 0), (1, 1), (0, 1)) 

            # 비교할 타겟 값 확인
            target = board[x][y]

            # 예비 삭제 집합 생성
            temp_removed = set([(x, y)])

            # 3칸을 검사하여 타겟 값과 같을 때 예비 삭제 집합에 추가
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < m) and (0 <= ny < n) and (board[nx][ny] == target):
                    temp_removed.add((nx, ny))
                else:
                    break
            
            # 예비 삭제 집합의 크기가 4개라면 조건에 만족하기 때문에 삭제 집합에 추가
            if len(temp_removed) == 4:
                removed.update(temp_removed)

        # 1. 네 칸씩 탐색하는 코드 작성하기
        for x in range(m):
            # 각 board의 문자열을 리스트로 변환 (추후에 각을 변환하기 위해서)
            board[x] = list(board[x])

            for y in range(n):
                # "-" 삭제된 칸을 제외한 나머지 칸들은 삭제가 가능한지 확인
                if board[x][y] != "-":
                    remove_same(x, y)
        
        # 종료 조건 : 제거할 칸이 없다면 Break
        if not removed:
            break

        answer += len(removed)

        # 2. 기억된 주소 값 "-"으로 변경
        for rx, ry in removed:
            board[rx][ry] = "-"

        # 3. "-"로 표기된 Col을 생략시키기
        for y in range(n):
            # 덱에 추가해야할 알파벳 순서 기억
            item = deque()
            
            # 빈칸의 개수
            count = 0

            # 빈칸 갯수 및 알파벳 순서 기억
            for x in range(m):
                if board[x][y] == "-":
                    count += 1
                else:
                    item.append(board[x][y])
            
            # 가장 상단부터 빈칸 + 알파벳을 순서대로 추가
            for x in range(m):
                if x < count:
                    board[x][y] = "-"
                else:
                    board[x][y] = item.popleft()

    return answer

case1 = [4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]]
case2 = [6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]

print(solution(*case1))
print(solution(*case2))