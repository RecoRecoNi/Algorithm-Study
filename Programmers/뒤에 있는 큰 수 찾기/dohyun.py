"""

풀이시간
- 약 1시간 풀이 후 실패로 답지 참조

접근법
- 구현 자체는 쉬워보이지만 N 이 최대 100만 -> O(N) 근처의 복잡도로 해결해야함
- result 와 numbers 의 길이가 같음 -> 뭔가 여러번 복잡한 순회보다는 인덱싱을 활용하면 최소한의 순회가 될 것 같음
- 두 세 문제에서 시간초과 문제를 해결하지 못해서 답지 참조 ㅠ_ㅠ

- 답지 풀이
    - 인덱싱으로 접근 자체는 비슷했던 것 같음
    - 스택을 활용하여 시간여행(?)을 가능케했음

회고
- 스택을 활용하여 시간여행(?) 한 것이 인상적인데 숙지한다면 꽤나 쓰게될 일이 있을 것 같다!!

"""

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num: # 스택이 비어있지 않고, 현재 숫자가 스택의 맨 위 숫자보다 큰 경우 (예전 인덱스에 위치한 number 보다 큰 경우)
            answer[stack.pop()] = num # 예전 인덱스에 해당하는 answer 의 값을 현재 값으로 바꿔줌
        stack.append(i) # 현재 숫자의 인덱스를 스택에 추가

    return answer