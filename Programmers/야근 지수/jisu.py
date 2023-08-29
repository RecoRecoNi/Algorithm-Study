'''
문제 풀이 시작 : 2023-08-22 16:18

야근 피로도 = (남은 일의 작업량)^2
N시간 동안 야근 피로도를 최소화하도록 
1시간 -> 작업량 1

- 결국 도합 N 만큼을 works에서 뺄 때 제곱의 합의 최소를 구하면 되는 문제
  - 최대값의 크기를 최대한 줄이는 방향으로 알고리즘을 짜면 될 것 같다.
- 남은 작업량의 합이 n을 넘지 않으면 피로도는 0임 (예외 처리)
- 접근 1 : n -> 0이 될 때까지 최대값 1씩 빼서 다시 정렬
    - N*Nlog(N) -> 시간 초과
- 접근 2 : 0 ~ max(works) 중 최대값을 num으로 설정했을 때 빼야 하는 수의 합이 n을 넘지 않는 최대 num을 구하기
    - 해당 num으로 works의 최대값을 맞추기
    - 빨꺼 다 빼고 남은 n은 어떻게 처리?  
        - 예를 들어 works = [4, 3, 3, 1], n=6)일 때 
        - 최대값은 2로 맞춰지고([2, 2, 2, 1]) n은 2가 남을 때 => [1, 1, 2, 1]을 만들어야 함
        - n이 남아있는 동안 제일 큰 것부터 골고루 빼주기, 이 과정에서 음수가 되면 안됨

문제 풀이 중단 : 2023-08-22 17:50 (1시간 30분 경과)
문제 풀이 재개 : 2023-08-23 10:50
문제 풀이 완료 : 2023-08-23 11:10 (문제 풀이 시간 : 1시간 50분)


'''
from typing import List

def solution1(n: int, works: List[int]) -> int:
    '''
    효율성 시간 초과 코드
    매번 정렬해서 최대값을 줄여주는 방식
    '''
    if sum(works) <= n:                 # 예외 처리 : 남은 작업량의 합이 n을 넘지 않으면 피로도는 0임
        return 0
    
    works.sort(reverse=True)            # 내림차순 정렬
    
    while n > 0:                        # n이 남아있는동안
        works[0] -= 1                       # 최대값 -1
        works.sort(reverse=True)            # 최대값 인덱스 업데이트
        n-=1

    return sum(map(lambda x:x**2, works))

# -------------------------------------------------------------------
# -------------------------------------------------------------------

def get_need_decrease(works: List[int], max_value: int) -> int:
    '''
    최대값을 max_value로 설정했을 때 works에서 빼어야 할 크기를 반환한다.
    '''
    need_decrease: int = 0

    for work in works:
        if work > max_value:
            need_decrease += (work - max_value)
    
    return need_decrease


def solution(n: int, works: List[int]) -> int:
    if sum(works) <= n:             
        return 0
    
    works.sort()
    
    start, end = 0, max(works)

    while start <= end:                             # 최대 값을 num으로 설정할 때 빼어야 하는 수가 n을 넘지 않는
        mid = (start+end)//2                        # 최대 num을 찾기
        if get_need_decrease(works, mid) <= n:
            end = mid-1
        else:
            start = mid+1                           # 이 경우 최종 최대 num은 start에 담김

    for i in range(len(works)-1, -1, -1):           # 최대값을 start로 두고 실제 works에서 빼주기
        if works[i] > start:
            n -= (works[i]-start)
            works[i] = start
        else:
            break

    i = len(works)-1                                # 최대값을 num으로 맞춰주었을 때 n이 남은 경우
    while n > 0 and i >=0:                          # 가장 큰 수부터 골고루 빼줘야 함(현재 오름차순 정렬되어 있음)
        works[i]-=1
        n-=1
        if not works[i] or works[i]<works[i-1]:     # 음수가 될 순 없음, 전체 1씩 낮출 수 없음이 보장되어있기 떄문에
            i-=1                                                      # 큰 수부터 골고루 낮춰야 한다.


    return sum(map(lambda x:x**2, works))
        

def main() -> None:
    case1 = [4, [4, 3, 3]]
    case2 = [1, [2, 1, 2]]
    case3 = [3, [1, 1]]

    print(solution(*case1))     # 12
    print(solution(*case2))     # 6
    print(solution(*case3))     # 0

main()
