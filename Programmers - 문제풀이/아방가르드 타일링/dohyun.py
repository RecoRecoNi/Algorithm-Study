import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한을 풀어줌 (재귀문제에서 필수라고 함)

A = [0]*100001  # 문제에서 최대 n 의 크기만큼 A 배열 생성

def solution(n):
    """
    
    풀이시간
    - 약 1시간 가량 풀이 후 레퍼런스 참고
    - https://velog.io/@jinhoss/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EB%B0%A9%EA%B0%80%EB%A5%B4%EB%93%9C-%ED%83%80%EC%9D%BC%EB%A7%81python
    - https://velog.io/@mechauk418/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EB%B0%A9%EA%B0%80%EB%A5%B4%EB%93%9C-%ED%83%80%EC%9D%BC%EB%A7%81-%ED%8C%8C%EC%9D%B4%EC%8D%ACDP

    접근법
    - 도형을 맞추는 알고리즘을 구현하는 건 말이 안된다고 판단
    - 무조건 규칙이 있다고 생각했음 -> 규칙으로 재귀
    - n이 4까지는 어찌저찌 구하겠는데 5부터는 도저히 감이 안잡힌다 ...
    - 또한 n이 4일 때까지는 규칙을 도저히 못찾겠음
    - 참조한 레퍼런스에서는 새로운 유형의 블록의 개수로 규칙을 정의하여 점화식 구성
        - n=1 -> 1
        - n=2 -> 2
        - n=3 -> 5
        - n=4,7,10 -> 2
        - n=5,8,11 -> 2
        - n=6,9,12 -> 4
        - 최종적인 점화식은 $A(X) = \sum_{i=1}^{X-1}{A(X-i) \times s(i)} + s(X)$
        - $A(X) = A(X-1) + 2A(X-2) + 5A(X-3) + 2A(X-4) + 2A(X-5) + 4A(X-6) + \dots$
        - $A(X+3) = A(X+2) + 2A(X+1) + 5A(X) + 2A(X-1) + 2A(X-2) + 4A(X-3) + \dots$
        - $A(X) - A(X+3) = -A(X+2) - 2A(X+1) -5A(X) - A(X-1) + A(X-3)$
        - $A(X+3) = A(X+2) + 2A(X+1) + 6A(X) + A(X-1) - A(X-3)$
        - $A(X) = A(X-1) + 2A(X-2) + 6A(X-3) + A(X-4) - A(X-6)$
        
        - 이를 행렬식으로 표현 (링크 참고)
    
    회고
    - 평행이동을 활용해서 점화식을 깔끔하게 정리한 점이 인상적 (고등학교에서 수열 문제 푸는것 같아서 반가웠다!!)
    - 개인적으로는 실전에서 수 많은 블록 수 중(n이 5부터는 경우의 수가 62개인데) 저게 새로운 유형의 블록 개수라고 확신을 못할 것 같다 ,,,
        - 62 개의 블록을 다 찾아본 뒤 그 중 새로운 유형이 2개라는 것을 알아낸 것은 아닐텐데, 어떤 확신을 가지고 2개라고 생각하게 된건지 발상의 출발이 궁금
        - 문제를 잘 못 이해한건가? 싶기도 함

    """
    
    answer = block(n) % 1000000007

    return answer

def block(n):
    answer = 0
    
    # 인덱싱을 1 부터 시작해서 조금 더 직관적으로 사용
    A[1:7] = [1, 3, 10, 23, 62, 170]

    if n <= 6:
        return A[n]
    
    answer += A[n-1] if A[n-1] else block(n-1)              # 비어있지 않은 가장 가까운 A(X-1) 찾기
    answer += A[n-2]*2 if A[n-2] else block(n-2)*2          # 2A(X-2)
    answer += A[n-3]*6 if A[n-3] else block(n-3)*6          # 6A(X-3)
    answer += A[n-4] if A[n-4] else block(n-4)              # A(X-4)
    answer += A[n-6]*(-1) if A[n-6] else block(n-6)*(-1)    # -A(X-6)

    A[n] = answer   # A(X)

    return answer

print(solution(2))  # result : 3
print(solution(3))  # result : 10