"""
<시간>
20분

<input>
- 5 ≤ sequence의 길이 ≤ 1,000,000
- sequence는 비내림차순으로 정렬

<solution>
- 투포인터의 가장 기본적인 문제
- start, end 포인터를 0번 인덱스부터 시작해서 부분합을 확인한다.
    - start부터 end까지의 부분합이 k와 같을 때까지 증가 end를 1 증가시킨다. (왜냐하면, sequence의 원소는 항상 자연수이기 때문에 가능)
    - k는 항상 sequence의 부분 수열로 만들 수 있는 값이기 때문에 만들 수 없는 경우를 고려할 필요 없다.
    - 부분합이 k와 같다면, 길이를 갱신해줘야 할 때만 갱신해주면 된다.
    - 이후, 같은 과정을 start를 한 칸 씩 이동하면서 확인해주면 된다.

시간복잡도 : O(n)
- start를 0번 인덱스부터 마지막 인덱스까지 모두 확인한다.
- 내부 while문은 for문에 비례하여 n번 실행되는 것이 아니기 때문이다.("end"의 증가 횟수가 "start"의 증가 횟수와 독립적)
"""


def solution(sequence, k):
    diff = n # 길이는 최대로 초기화
    end = 0
    interval_sum = 0  # 부분합

    # start를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한만큼 이동시키기
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1
        # 부분합이 k이면서, 길이가 짧을 때 갱신
        if interval_sum == k and end - 1 - start < diff:
            answer = [start, end - 1]
            diff = end - 1 - start
        interval_sum -= sequence[start]

    return answer


sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5


print(solution(sequence, k))