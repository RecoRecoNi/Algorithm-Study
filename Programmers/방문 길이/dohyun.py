"""

풀이시간
- 약 30분

접근법
- visit 배열을 활용하여 풀이 가능
- dirs < 500 으로 시간복잡도도 충분
- visit 딕셔너리의 키는 좌표와 좌표간의 연결

회고
- 모든 좌표간의 연결을 저장할 필요 없이 인접 좌표와의 연결만 표현하면 되므로 메모리 낭비
    - 다 풀고나서 visit 배열을 다시 정의해서 풀이

"""

def solution(dirs):
    answer = 0
    direction = {"U":(0,1), "R":(1,0), "D":(0,-1), "L":(-1,0)}

    all_location = [(x, y) for y in range(11) for x in range(11)] # 좌표 배열 생성
    # visit = {f"{loc_1}_{loc_2}":False for loc_1 in all_location for loc_2 in all_location} # 모든 좌표간의 간선 생성 (원래 풀이, 메모리 낭비)

    visit = {}
    for loc in all_location: # 인접한 좌표간의 간선 생성 (수정 풀이)
        for _, (dx, dy) in direction.items():
            new_loc = (loc[0] + dx, loc[1] + dy)
            visit[f"{loc}_{new_loc}"] = False

    nx, ny = 5, 5
    visit["(5, 5)_(5, 5)"] = True

    for dir in dirs:
        dx, dy = direction[dir]
        x, y = nx, ny # 이전 좌표
        nx, ny = x + dx, y + dy # 현재 좌표

        if ((nx < 0) or (nx >= 11)) or ((ny < 0) or (ny >= 11)): # 좌표경계를 넘으면 무시
            nx, ny = x, y # 이전 좌표로 다시 변환
            continue

        if not visit[f"({x}, {y})_({nx}, {ny})"]: # 방문한적이 없다면 count + 1
            visit[f"({x}, {y})_({nx}, {ny})"] = True # 간선을 True 로 변환
            visit[f"({nx}, {ny})_({x}, {y})"] = True # 방향에 상관없이 방문한 길은 마찬가지
            answer += 1
    
    return answer