"""
    파일명 정렬
    https://school.programmers.co.kr/learn/courses/30/lessons/17686

    풀이시간 
    00:05 ~ 00:42 (37분)
    
    문제 조건
    1<= files <= 1,000
    각 파일명의 길이는 100글자 이하 (영문 대소문자, 숫자, 공백, 마침표, 빼기 부호)

    시간 복잡도 :
    O(1000 * 100 + 1000 * log1000 + 1000 * 100)
    log1000 ≈ 3

    O(203,000)
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 정렬

    1. 최대 1000개의 파일명을 HEAD, Number, Tail의 형태로 나눠야합니다.
        - 빈 문자열 3개를 가지는 리스트 생성
        - 세 부분 각각은 숫자의 등장 여부에 따라 달라진다.
            - 이전 부분의 문자가 숫자였으나 지금은 아닐 경우 혹은 이전 부분의 문자가 숫자가 아니었으나 현재는 맞을 경우 다음 부분으로 이동
        - 각 부분에 문자 추가

    2. 나눠진 파일명을 기준으로 정렬을 진행합니다.
        - HEAD의 사전 순(대소문자 구별 X)
        - Number의 숫자 오름차순
    
    3. 분리된 파일 다시 Join
"""

def solution(files):

    # 파일 이름을 HEAD, NUMBER, TAIL 세 가지의 요소로 만들 리스트 생성
    files_list = []

    # 1. 최대 1000개의 파일명을 HEAD, Number, Tail의 형태로 나눠야합니다.
    # 주어진 모든 파일 이름에 대하여
    for file_name in files:

        # HEAD,NUMBER,TAIL로 구분
        file_list = ["","",""]

        # 현재 문자의 삽입될 부분(HEAD,NUMBER,TAIL)
        file_list_idx = 0

        # 이전 문자가 숫자였는지 여부 확인
        prev_isnumeric = False

        # 파일 이름에서 각각의 문자를 확인하며
        for character in file_name:
            # 현재 문자가 숫자인지 확인하고
            cur_isnumeric = character.isnumeric()

            # 인덱스를 초과하지 않은 상태에서 이전 문자와 현재 문자의 숫자 여부가 동일하지 않다면 다음 부분으로 이동
            if file_list_idx < 2 and prev_isnumeric != cur_isnumeric:
                file_list_idx += 1
            
            # 해당되는 부분에 현재 문자 추가
            file_list[file_list_idx] += character

            # 현재 문자의 숫자 여부를 이전 문자의 숫자 여부로 업데이트
            prev_isnumeric = cur_isnumeric
        
        # 세 부분으로 분리된 파일 이름을 전체 파일 리스트에 추가
        files_list.append(file_list)

    # 2. 나눠진 파일명을 기준으로 정렬을 진행 - HEAD의 사전 순(대소문자 구별 X), Number의 숫자 오름차순
    files_list.sort(key=lambda x: (x[0].lower(), int(x[1])))

    # 3. 분리된 파일 다시 Join
    answer = list(map("".join, files_list))

    return answer

case1 =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
case2 =  ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

print(solution(case1)) # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print()
print(solution(case2)) #  ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]