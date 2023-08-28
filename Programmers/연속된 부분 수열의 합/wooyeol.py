"""
    연속된 부분 수열의 합
    https://school.programmers.co.kr/learn/courses/30/lessons/178870?

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 투 포인터
    
    - 정렬된 데이터와 연속된 부분 집합을 보았을 때 투 포인터 문제임을 직감 할 수 있었다.
    - 테스트 케이스에 대해서 16,25번이 계속 틀려서 확인해보니 min_interval을 999995로 설정하였는데 값에 대한 범위이기에 1000001이 되어야했었다.
    - 투 포인터의 전형적인 케이스는 일정 값을 기준으로 작거나 클때 start,end 포인트를 조정하는 방식이었는데 이번에는 start 지점을 증가시키는 방향을 고정하고 진행했어야 풀이가 진행될 수 있었다.
    
    - 풀이 참고 (https://velog.io/@wodnr0710/프로그래머스-LV.2-연속된-부분-수열의-합)
"""


def solution(sequence: list, k: int):
    # 정답 반환
    answer: list = []

    # 투 포인터의 end 지점
    end: int = 0

    # 누적합
    cumsum: int = 0

    # 간격이 1000000가 최대 값
    min_interval: int = 1000001
    s_length: int = len(sequence)

    # 조건에서 "길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다."이기 때문에 앞쪽부터 탐색을 진행한다.
    # 시작점을 기준으로 탐색을 진행한다.
    for start in range(s_length):
        # 시작점을 기준으로 누적합이 K를 넘지 않는지 확인하며 end 증가 시키기
        while cumsum < k and end < s_length:
            cumsum += sequence[end]
            end += 1

        # 누적합 결과가 k와 같다면
        if cumsum == k:
            # start와 end의 간격을 확인하고
            interval: int = end - start - 1

            # 최소 간격보다 작으면 정답과 최소 간격을 업데이트한다.
            if interval < min_interval:
                min_interval = interval
                answer = [start, end - 1]

        # 시작점 변경하기 위해 포함되지 않는 start 값을
        cumsum -= sequence[start]

    return answer


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2], 6))
