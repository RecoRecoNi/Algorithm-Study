"""

풀이시간
- 50 분

접근법
- 주어진 변수들의 범위가 매우 적은 편 -> 구현에 집중
- 숫자를 계속 해서 빼는 작업을 해야함 -> 큐를 활용하면 시간복잡도에서 장점이 많을 것이라 판단
    - appendleft : 진법 변환할 때 따로 정렬하지 않아도 됨
    - popleft : 글자를 빼낼 때 유용

회고
- 다른 사람의 풀이를 보니 본인의 코드에서 차례를 초기화하는 과정을 슬라이싱을 잘 활용해서 조금 더 코드를 간결하게 한 것 같음
    - 개인적으로도 이 부분을 조금 더 간결하게 하고 싶어 고민했는데 ㅠㅠ 머리만 굴리지말고 조금 더 적어보면서 고민하기

"""

from collections import deque

def transform(number, k):
    """
    number : 변환하고 싶은 10진수
    k : 변환하고 싶은 k 진법
    """
    if number==0:
        return deque(['0'])
    
    replace_num_to_str = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    transformed_number = deque([])
    
    while number > 0:
        m = number % k
        number = number // k
        transformed_number.appendleft(f'{m}' if m not in replace_num_to_str else replace_num_to_str[m])

    return transformed_number

def solution(n, t, m, p):
    temp_m = 0
    answer = ''
    num = -1 # 0 부터 시작하기 위해 -1 

    while True:
        num += 1
        transformed_nums = transform(num, n) # n진수로 변환

        while transformed_nums: # 변환된 n진수가 비워질 때 까지 반복
            temp_m += 1 # 순서 +1
            transformed_num = transformed_nums.popleft() # 숫자 한 차례 제거

            if temp_m == p: # 튜브의 차례가 온다면
                answer += transformed_num # 정답에 한 글자 더하기
            
                if len(answer) == t: # 정답 조건을 만족하면
                    return answer # 정답을 반환하며 종료
            
            if temp_m == m: # 한 차례가 끝나고도 n진수가 비워지지 않았다면 다시 차례 초기화하기
                temp_m = 0
