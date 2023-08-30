'''
풀이 시작 : 2023-08-28 10:30

퀸이 다른 말을 잡을 수 있는 경우
    - 세로 같은 열에 있는 경우
    - 가로 같은 열에 있는 경우
    - 대각선 같은 열에 있는 경우

- 체스판을 순회하며 퀸을 놓는 경우와 놓지 않는 경우로 재귀한다.
- 이때 재귀를 진행하다 해당 위치에 퀸을 놓는 경우 위의 사항에 해당 된다면 해당 분기는 잘라내기(백트래킹)
- 체스판 순회가 끝날 때까지 퀸을 N개 놓으면 경우의 수 추가

풀이 중단 : 2023-08-28 11:00 (30분 경과)
풀이 재개 : 2023-08-28 13:55

- Hint : 어차피 NxN 체스판에서 한 row에 한 퀸 밖에 둘 수 없음
    - 이러면 NxN Matrix를 구성 안하고, 길이 N의 리스트에 각 요소는 퀸이 위치한 column의 값을 가지게 두면 된다.
    - 예를 들어 2x2 체스판이라고 가정 하고, (0, 0), (1, 1)에 퀸을 배치하면 [0, 1] 요런식
        - 이러면 가로 제약조건은 자동 만족
        - 세로 제약조건은 같은 열만 아니면 됨
        - 대각선은 |현재 인덱스 - 비교 인덱스| == |현재 인덱스의 값 - 비교 인덱스의 값| 을 검사하면 됨
            - 예를 들어 (0, 0), (1, 1)에 배치하여 [0, 1]인 경우
            - |현재 인덱스 - 비교 인덱스| = |0 - 1| = 1
            - |현재 인덱스의 값 - 비교 인덱스의 값| = |0 - 1| = 1
            - 같으므로 대각선에 위치하는 것

- 풀이 완료 : 2023-08-28 15:45 (2시간 20분 소요)
    - python3는 통과 못하고 pypy만 통과
    - python3 통과시켜보고 싶었으나 실패, 전역변수 설정에 따른 시간 초과 유무 확인
        - 현재 solution처럼 함수 바깥에 솔루션 코드를 적는 건 통과
        - but 프로그래머스처럼 main 함수 역할을 하는 solution 함수를 만들어 전역으로 변수 설정 시 시칸 초과

'''
import sys

input = sys.stdin.readline

def check_condition(row_idx: int) -> bool:
    '''
    퀸이 같은 열에 있는지 or 대각선 상에 배치되었는지 검사한다.
    '''
    for comp_idx in range(row_idx):     # 현재 row_idx 행까지 퀸이 배치되어 있음
        # 비교 과정 20행 부터 참고
        if matrix[row_idx]==matrix[comp_idx] or abs(row_idx-comp_idx)==abs(matrix[row_idx]-matrix[comp_idx]):
            return False
        
    return True

def recur(row_idx: int) -> None:
    '''
    재귀에 활용할 함수, 인자로 받은 row_idx 행에 col 값을 넣어보며 조건 검사에 만족하는 경우 퀸을 배치한다.
    '''
    global result

    if row_idx == N:            # N-1행까지 퀸이 배치 완료된 경우
        result += 1                 # 카운트 후 함수 종료
        return
    
    for col in range(N):                # row_idx행의 모든 컬럼에 퀸 배치해보기
        matrix[row_idx] = col           # 일단 배치 후

        if check_condition(row_idx):    # 조건에 만족하면
            recur(row_idx+1)            # 퀸을 배치 후 다음 row_idx+1행 탐색
    

N = int(input())
result = 0
matrix = [-1 for _ in range(N)]         # 문제 특성상 이와 같은 체스판 구성 가능, 16행 부터 참고
recur(0)
print(result)                           
