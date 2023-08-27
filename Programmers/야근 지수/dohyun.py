"""

풀이시간
- 1시간 30분

접근법
- 사전 시간복잡도 계산을 어떻게 해야하나..?
    - 우선 works 의 길이로 확인해야한다고 생각 -> 20000 이하로 대략 O(N^2) 까지 가능?
- 야근 피로도 = sum(남은 일 작업량**2)
    - 합의 최대최소를 구하는 문제 -> 고딩 때 배운 산술기하 생각남
    - 산술기하평균의 등호 조건에 따르면 합의 최소값은 모든 원소가 같을 때! -> 평균값 및 몫과 나머지 활용
- 경계해야하는 것은 works 의 원소들이 몫보다 작으면 모든 원소를 같게할 수 없음
    - 즉 "최대한" 같게하는 것이 관건 -> 해당 조건처리 필요
    - 조건에 부합하는(값이 몫보다 큰) 애들만 몫과 나머지를 적절히 나누어주면 됨

회고
- 값이 몫보다 작은 경우를 생각하지 못해서 시간이 좀 오래 걸렸음
    - 자꾸 테케에서 몇개가 오류가 나서 예제를 여러 개 생각해보니 반례 찾는것에 성공
    - 주어진 예제 이외의 예제들도 만들어서 디버깅하는 습관 더 연습하기

"""

def solution(n, works):
    total_works = sum(works) # sum 의 시간복잡도가 O(n) 이므로 미리 계산

    if total_works <= n: # 잔여 업무가 없는 경우
        return 0

    remain_works = total_works - n
    mean_value = round(remain_works / len(works)) # 잔여시간의 평균을 구해서 "최대한 같게" 만들어야하는 값의 임계치 설정
    
    works.sort()

    for idx in range(len(works)):
        if works[idx] > mean_value: # 만약 임계치 조건을 넘어선다면 몫과 나머지 계산
            quotient, remainder = divmod(sum(works[idx:]) - n, len(works) - idx)
            if quotient > works[idx]: # 예외 조건인 원소가 몫보다 작은 경우라면 패스
                continue
            else: # 예외 조건이 성립하지 않는다면 몫과 나머지 적절히 분배
                break

    # 예외 상황인 원래 값들과 예외 상황에 부합하지 않는 값들의 몫과 나머지 분배 -> 최대한 같은 값을 갖는 원소 배열 성립
    answer = [x**2 for x in works[:idx]] + [quotient**2] * (len(works) - remainder - idx) + [(quotient + 1)**2] * (remainder)
    return sum(answer)


print(solution(4, [4,3,3])) # 12
print('----------')
print(solution(1, [2,1,2])) # 6
print('----------')
print(solution(4, [8,2,2])) # 24
print('----------')
print(solution(4, [8,1,1])) # 18
print('----------')
print(solution(3, [2,2,1])) # 2
print('----------')
print(solution(5, [5,5,5])) # 34
print('----------')
print(solution(8, [10, 5, 1])) # 26
print('----------')
print(solution(20, [100, 50, 10])) # 9000