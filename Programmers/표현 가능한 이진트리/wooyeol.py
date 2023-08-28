"""
    표현 가능한 이진트리
    https://school.programmers.co.kr/learn/courses/30/lessons/150367?language=python3
    
    해결법 참조 : https://velog.io/@top1506/2023-KAKAO-표현-가능한-이진트리python
    

    접근법
    1. 주어진 수를 이진수로 변환하기
    2. 이진수로 만들어진 수가 In-order 순회식이라고 생각하고 이진 트리 내용의 값을 검사하기
        1. 이때 필요한 조건 : 현재 가지는 이진수의 자리수를 포화 포화 이진트리의 노드수와 같게 만들어주기
            - With 0을 삽입하는 방식으로
    3. 이진 트리를 순회하며 부모 노드가 0인데 자식노드가 1인 경우를 찾아서 반환
"""
import math


def decimal_to_binary(n):
    # 십진수 to 이진수
    if n == 0:
        return "0"

    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n = n // 2

    return binary


def check_binary_inter_tree(start, end, inorder):
    # 포화 이진트리의 경우에만 탐색이 가능
    global FLAG

    if start == end:
        return inorder[start]

    # 중간 인덱스 계산
    mid = (start + end) // 2

    if inorder[mid] == "0":
        for i in range(start, mid):
            if inorder[i] == "1":
                FLAG = False
                return
        for i in range(mid + 1, end + 1):
            if inorder[i] == "1":
                FLAG = False
                return

    check_binary_inter_tree(start, mid - 1, inorder)
    check_binary_inter_tree(mid + 1, end, inorder)


def solution(numbers):
    global FLAG
    answer = []
    for number in numbers:
        FLAG = True

        # numbers의 값을 2진수로 변환
        number_binary = decimal_to_binary(number)

        # 포화 이진 트리 Level
        level = int(math.log(len(number_binary), 2)) + 1

        # 포화 이진 트리 크기는 각 Level에 대해서 2^(Level) - 1를 나타낼 수 있다.
        digit = 2 ** (level) - 1

        # 자릿수를 0으로 채워주기
        number_binary = number_binary + ["0"] * (digit - len(number_binary))

        # 이진트리의 in-order 기준으로 탐색
        check_binary_inter_tree(0, len(number_binary) - 1, number_binary)

        # 가능한지 여부 반환
        if FLAG:
            answer.append(1)
        else:
            answer.append(0)
    return answer


# 1 Case #1
numbers = [7, 42, 5]
result = [1, 1, 0]
print(solution(numbers))

# 2 Case #2
numbers = [63, 110, 95]
result = [1, 1, 0]
print(solution(numbers))

"""
테스트 1 〉	통과 (0.02ms, 10.5MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.09ms, 10.4MB)
테스트 4 〉	통과 (0.28ms, 10.4MB)
테스트 5 〉	통과 (0.61ms, 10.2MB)
테스트 6 〉	통과 (2.08ms, 10.5MB)
테스트 7 〉	통과 (1.64ms, 10.5MB)
테스트 8 〉	통과 (1.57ms, 10.3MB)
테스트 9 〉	통과 (10.01ms, 10.5MB)
테스트 10 〉	통과 (84.02ms, 11.1MB)
테스트 11 〉	통과 (94.91ms, 11.5MB)
테스트 12 〉	통과 (90.31ms, 11.5MB)
테스트 13 〉	통과 (83.13ms, 11.2MB)
테스트 14 〉	통과 (75.94ms, 11.2MB)
테스트 15 〉	통과 (85.01ms, 11MB)
테스트 16 〉	통과 (183.43ms, 11.5MB)
테스트 17 〉	통과 (169.40ms, 11.6MB)
테스트 18 〉	통과 (163.40ms, 11.2MB)
테스트 19 〉	통과 (144.52ms, 11.2MB)
테스트 20 〉	통과 (90.29ms, 10.8MB)
"""
