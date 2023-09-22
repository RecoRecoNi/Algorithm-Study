"""
    뒤에 있는 큰 수 찾기
    https://school.programmers.co.kr/learn/courses/30/lessons/154539

    풀이시간 
    11 :42~48 13:38 ~ 14:10 (풀이 포기)

    풀이 참고 : https://maximum-curry30.tistory.com/515
    
    문제 조건
    4 <= len(numbers) : N <= 1,000,000

    시간 복잡도 : 
    O(N)

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> stack
    
    - 오큰수 처리 알고리즘이 존재
    - Stack을 사용하여 가장 위의 원소에 해당하는 값보다 현재 검사하는 원소의 값이 작을 때 해당 수가 오 큰수이다.
"""

def solution_fail(numbers):
    answer = []
    N = len(numbers)

    for i in range(N):
        flag = True
        for j in range(i+1, N):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                flag = False
                break
        
        if flag:
            answer.append(-1)

    return answer

def solution(numbers):
    answer = [-1] * len(numbers)

    # 현재 처리 중인 원소들의 인덱스를 저장하기 위한 스택
    stack = []
    
    for idx, num in enumerate(numbers):
        # 스택의 가장 위 원소에 해당하는 값이 현재 원소보다 작을 때, 스택에서 원소를 꺼내오면서 오 큰수 찾기
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num

        # 스택의 가장 위 원소보다 크거나 같다면, 스택에 현재 인덱스를 추가
        stack.append(idx)
    return answer

case1 = [2, 3, 3, 5]
case2 = [9, 1, 5, 3, 6, 2]
case3 = [10,9,8,7,6,5,4,3,2,1]

print(solution(case1)) # [3, 5, 5, -1]
print(solution(case2)) # [-1, 5, 6, 6, -1, -1]
print(solution(case3)) # [-1, 5, 6, 6, -1, -1]