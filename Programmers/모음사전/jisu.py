"""
풀이 시작 : 2023-09-17 15:38

#### 제한 사항
- 모든 단어는 길이 5이하이다.

#### 풀이
A : 1부터 시작
E : 782
I : 1563

AA : 2
AE : 158

AAA : 3
AAE : 34

AAAA : 4
AAAE : 10 

AAAAA : 5
AAAAE : 6

- 모음 사전을 DFS로 생성 후, index 메서드로 단어 길이 별 A와 E의 길이를 얻기
    - 첫 번째 자리의 알파벳 하나 차이 : 781
    - 두 번째 자리의 알파벳 하나 차이 : 156
    - 세 번째 자리의 알파벳 하나 차이 : 31
    - 네 번째 자리의 알파벳 하나 차이 : 6
    - 다섯 번째 자리의 알파벳 하나 차이 : 1
    - A와 E의 차이를 통해 알파벳 길이 별 모음 하나만큼의 개수를 알 수 있음
- 미리 구해놓은 차이만큼 알파벳을 계산해서 최종 모음사전 순서 얻기
    - 단어 순서는 1부터 시작함에 유의해야 한다. (T+1)의 악몽...

풀이 완료 : 2023-09-17 16:11 (풀이 시간 : 33분)
"""


def solution(word: str) -> int:
    """
    dfs 로 먼저 자리 별 단어 하나 차이의 단어 개수를 파악 후, word가 사전 몇 번쨰 수인지 반환한다.
    """
    # -------------------------------------------------
    """
    모음 사전을 DFS로 생성 후, index 메서드로 단어 길이 별 A와 E의 길이를 얻기
    """
    # answers = []
    # alpha = "AEIOU"

    # def dfs(tmp):
    #     if len(tmp) > 5:
    #         return
    #     if tmp:
    #         answers.append(tmp)

    #     for idx in range(5):
    #         dfs(tmp + alpha[idx])

    # dfs("")
    # answers.sort()

    # return answers.index(word) + 1
    # -------------------------------------------------

    dict_cut = [781, 156, 31, 6, 1]  # 자리 수 별 알파벳 차이
    dict_index = {ch: idx for ch, idx in zip("AEIOU", range(5))}

    result = 0
    for idx, w in enumerate(word):  # 몇 번째 단어인지 계산
        result += dict_cut[idx] * dict_index[w] + 1  # 단어 순서는 1부터 시작함에 유의

    return result


def main() -> None:
    case1 = "AAAAE"
    case2 = "AAAE"
    case3 = "I"
    case4 = "EIO"
    case5 = "AE"
    case6 = "AAE"

    print(solution(case1))  # 6
    print(solution(case2))  # 10
    print(solution(case3))  # 1563
    print(solution(case4))  # 1189
    print(solution(case5))
    print(solution(case6))


main()
