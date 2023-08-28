"""

풀이시간
- 약 40분

접근법
- N = 100만 -> O(NlogN) / O(N)
- 네가지 경우를 줬지만 생각해보니 이건 사실상 경우를 나누라는 뜻이 아니라 0 사이에 껴있는 소수를 찾으라는 말임
- 테케 1 문제에서 시간초과가 났음
    - 아무리 생각해봐도 시간을 줄일 부분은 소수 확인 부분 밖에 없다고 판단
    - 옛날 옛적 소수를 판별하는 데 효율적인 방법이 있었다고 기억이 남 -> 도저히 뭔지 기억 안나서 구글링 했습니다 ..ㅎ -> 바꿨더니 시간초과 해결!

회고
- 십진수에서 n진수 변환하는 법을 까먹었네요..ㅎㅎ
- 소수, 진수에 대한 문제들을 몇번 봤던 것 같아서 이번 기회에 까먹은 개념들을 다시 톺아봐야할 것 같음

"""

# n 진수 변환
def translate(n, k):
    num = []
    mok = n    
    while mok!=0: # 몫이 0 이 될때 진수변환 끝
        remain = mok % k
        mok //= k
        num.append(str(remain))
    num = ''.join(num[::-1])
    return num

# 소수인지 확인
def check_sosu(num):
    for n in range(2, int(num**(1/2)) + 1): # 해당 수의 제곱근까지만 확인해보아도 판별 가능! 원래는 range(2, num) 으로서 O(N)의 코드를 작성했었습니다.
        if num % n ==0:
            return False
    return True
        
def solution(n, k):
    num = translate(n, k)
    num = num.split('0') # 0 을 떨굼
    answer = 0
    
    for n in num:
        if n=='' or n=='1':
            continue
        
        if check_sosu(int(n)):
            answer += 1
        
    return answer


print(solution(n=437674, k=3)) # 3
print('----------')
print(solution(n=110011, k=10)) # 2