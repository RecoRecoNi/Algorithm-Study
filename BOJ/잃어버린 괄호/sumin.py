"""
풀이시간: 10분

<input>
숫자 0~9, +, -로 이루어진 최대 길이 50인 식
가장 처음과 마지막 문자는 숫자

<solution>
어떻게 괄호를 넣어야 수식의 값이 최소값이 될 수 있을까?
-를 기준으로 괄호를 넣을 때 수식의 결과가 가장 작아질 수 있음
ex. 5-35+20-45라면 5-(35+20)-45처럼 -와 - 사이의 35+20을 빼주는 것이 되기 때문에!

<시간 복잡도>
O(N)
"""
exp = input().split('-')

nums = [] # + 연산을 처리한 숫자들
for x in exp:
    num = 0 # 괄호로 묶은 수식들의 결과값
    s = x.split('+') # +가 있는 경우를 위해 다시 +로 split
    for j in s: # '+'가 없을 때 split하면 원래값 반환됨
        num += int(j)
    nums.append(num)

ans = nums[0] # 최종 결과값
for i in nums[1:]: # 수를 순회하며 ans에서 빼주면 된다.
    ans -= i

print(ans)
