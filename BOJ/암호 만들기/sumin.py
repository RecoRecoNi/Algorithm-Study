"""
풀이시간: 25분

<input>
- L, C (3 ≤ L ≤ C ≤ 15)

<solution>
- 주어진 알파벳 C개 중 L개를 중복없이 선택
- 만든 암호가 한 개 이상의 모음, 두 개 이상의 자음을 포함하고 있는지 확인

<시간 복잡도>
O(2^C * L): go 함수에서 각 재귀 호출마다 i가 start부터 c-1까지 변화하면서 두 가지 경우의 수가 발생하므로, 재귀 호출의 총 횟수는 2^C 번 * check 함수는 O(L)
"""

# l: 암호의 길이, c: 알파벳의 개수
l, c = map(int, input().split())
alpha = sorted(input().split())  # c개의 알파벳
pw = []  # 암호를 저장하는 리스트

# 한 개 이상의 모음, 두 개 이상의 자음이 있는지 확인하는 함수
def check(password: str) -> bool:
    ja, mo = 0, 0  # 자음, 모음
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def go(index: int, start: int) -> None:
    """
    index: 처리하고 있는 암호의 인덱스
    start: 다음에 올 암호의 시작 인덱스
    """
    if index == l:  # l개의 알파벳을 모두 선택하면 종료
        result = ''.join(pw)
        if check(result): # 자음, 모음 조건 충족한다면 출력
            print(result)
        return

    for i in range(start, c):
        pw.append(alpha[i])  # 알파벳을 암호에 추가
        go(index + 1, i + 1)  # 다음번째에 올 암호처리
        pw.pop()  # 마지막으로 추가한 알파벳 제거(백트래킹)

go(0, 0)