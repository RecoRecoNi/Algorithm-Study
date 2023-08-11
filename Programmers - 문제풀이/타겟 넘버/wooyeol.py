"""
    타겟 넘버
    https://school.programmers.co.kr/learn/courses/30/lessons/43165

    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 2^50이라 완전탐색이 불가능 그렇기에 BFS/DFS 탐색을 고려
    
    해당 값에 - / + 부호를 붙일지에 따라 이진 트리로 그래프를 생각할 수 있음
    모든 그래프를 생각할 직전에 계산된 값들만 기억하게 한다면 메모리 효율도 높일 수 있다.

    다른 풀이를 찾아보던 중 메모이제이션을 사용하여 속도를 개선하는 답을 확인 할 수 있었고 적용해보았는데
    속도 개선이 많이 되었다.
"""


def solution(numbers, target):
    memo_answers = [0]
    # BFS
    for num in numbers:
        answers = []
        for answer in memo_answers:
            answers.append(answer + num)
            answers.append(answer - num)
        memo_answers = answers

    return memo_answers.count(target)


def solution2(numbers, target):
    from collections import defaultdict

    # 0-1+1+1+1+1 = 3
    # 0+1-1+1+1+1 = 3
    # 0+1+1-1+1+1 = 3
    # 0+1+1+1-1+1 = 3
    # 0+1+1+1+1-1 = 3
    # 을 위해서 0 값을 가장 상단에 위치시킴
    answers = [0]

    # 해당 answer가 몇번 나왔는지 확인해주는 dict
    memo = defaultdict(int)

    # 0의 값의 출현 횟수
    memo[0] = 1

    for num in numbers:
        dynamic_memo = defaultdict(int)
        dynamic_answers = []

        for answer in answers:
            if answer + num not in dynamic_memo:
                dynamic_answers.append(answer + num)
            if answer - num not in dynamic_memo:
                dynamic_answers.append(answer - num)

            # 그런데 이러게 풀이하면 모든 num가 반영되지 않은 계산 결과값도 같이 카운트하지 않나?
            dynamic_memo[answer + num] += memo[answer]
            dynamic_memo[answer - num] += memo[answer]

        memo = dynamic_memo
        answers = dynamic_answers
    return memo[target]


case1 = ([1, 1, 1, 1, 1], 3)  # 5
print(solution(*case1))

# 테스트 1 〉	통과 (193.54ms, 50MB)
# 테스트 2 〉	통과 (219.01ms, 49.3MB)
# 테스트 3 〉	통과 (0.16ms, 9.99MB)
# 테스트 4 〉	통과 (0.62ms, 10.3MB)
# 테스트 5 〉	통과 (5.20ms, 11MB)
# 테스트 6 〉	통과 (0.32ms, 10MB)
# 테스트 7 〉	통과 (0.16ms, 10.2MB)
# 테스트 8 〉	통과 (2.60ms, 10.2MB)

print(solution2(*case1))

# 테스트 1 〉	통과 (2.44ms, 10.2MB)
# 테스트 2 〉	통과 (2.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.38ms, 10.2MB)
# 테스트 4 〉	통과 (0.63ms, 10.2MB)
# 테스트 5 〉	통과 (1.22ms, 10.2MB)
# 테스트 6 〉	통과 (0.48ms, 10.1MB)
# 테스트 7 〉	통과 (0.34ms, 10.2MB)
# 테스트 8 〉	통과 (1.49ms, 10.1MB)
