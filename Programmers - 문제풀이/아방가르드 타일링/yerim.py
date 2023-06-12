"""
[프로그래머스 - 아방가르드 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/181186)
- 풀이 시간 : -
- 접근 방법 : 10분 동안 고민해봤는데 와 그냥 못풀 것 같아서 바로 풀이 확인했습니다..
- 참고 : https://velog.io/@jinhoss/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EB%B0%A9%EA%B0%80%EB%A5%B4%EB%93%9C-%ED%83%80%EC%9D%BC%EB%A7%81python

[접근 방법]
- n에 따라 타일링 할 수 있는 새로운 블록 개수를 계산해 보면, 일정한 규칙이 있음
- 따라서 새로운 블록 개수에 대해 점화식 작성 가능 (블로그 링크 참고)
- 점화식을 정리하여 행렬로 표현 가능
- 해당 행렬을 코드로 구현하여 구하고자 하는 새로운 블록 개수(A(X))를 계산 가능

- 근데 사실 아직도 이해가 다 안됐습니다,,, 넘 어렵네요,,,
"""

mod = 1000000007


def matrix_product(arr1, arr2):
    l = len(arr1)
    new_arr = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
            new_arr[i][j] %= mod
    return new_arr


def matrix_product2(arr, lst):
    l = len(arr)
    result = [0] * l
    for i in range(l):
        for j in range(l):
            result[i] += arr[i][j] * lst[-j - 1]
            result[i] %= mod
    return result


def solution(n):
    A = [1, 3, 10, 23, 62, 170]

    if n <= 6:
        return A[n - 1]

    arr = [[1, 2, 6, 1, 0, -1]]
    for i in range(5):
        lst = [0] * 6
        lst[i] = 1
        arr.append(lst)

    mat = [row[:] for row in arr]
    r_matrix = [[0] * 6 for _ in range(6)]
    for i in range(6):
        r_matrix[i][i] = 1

    cnt = n - 3
    while cnt > 0:
        if cnt % 2:
            r_matrix = matrix_product(r_matrix, mat)
        mat = matrix_product(mat, mat)
        cnt //= 2

    result = matrix_product2(r_matrix, A)
    return result[3]
