def solution(r1, r2):
    """

    풀이시간
    - 약 1시간

    접근법
    - 모든 정수 좌표 배열을 구해서 거리를 구하면 될까? -> 주어진 반지름의 길이가 매우 크기 때문에 시간 복잡도로 인한 오류가 날 가능성이 크다!
    - 이중 반복문으로 반지름 조건만 만족하면 += 1 을 할까? -> 이것도 시간 복잡도가...
    - 최소 하나의 반복문을 쓰는건 불가피하다고 생각, 남은 하나의 좌표는 조건에 맞도록 유동적으로 변경해야겠다
    - 정수의 개수이기 때문에 count 방식으로 해결해나가기 보다는 length 느낌으로 풀어 나갈 수 있겠다!

    회고
    - 이것저것 많은 방식을 시도하느라 생각보다 오래걸렸는데 엄청 어려운 문제는 아니었던것 같다.
    - ~~ 방식은 시간복잡도 문제가 생길걸 알면서도 시도해봤는데 안좋은 습관인 것 같음. 문제 접근법에 대해 고민하는 시간 늘리기

    """

    answer = 0
    max_y = 0 ; min_y = 0

    for x in range(r2, 0, -1):                  # 오른쪽 x 부터 카운트 시작
        while (x**2 + min_y**2) < r1**2:        # 작은 원 내부에 들어오면 최소 y 좌표를 상승
            min_y += 1
        while (x**2 + (max_y+1)**2) <= r2**2:   # 큰 원 내부에 있는 한 최대 y 좌표를 상승
            max_y += 1
        answer += (max_y - min_y) + 1           # 길이를 더해주는 것이 정수의 개수를 더하는 것과 같음

    return answer * 4                           # 1사분면의 개수만 구하면 4사분면의 개수는 대칭성
