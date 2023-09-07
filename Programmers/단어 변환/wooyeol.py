"""
    단어 변환
    https://school.programmers.co.kr/learn/courses/30/lessons/43163

    풀이시간 
    23:00 ~ 00:20 (1시간 20분)

    문제 조건
    3 <= W : 단어의 길이 <= 10
    3 <= N : len(words) <= 50

    시간 복잡도 : 
    O(N * W(dfs 탐색) * N(재귀문 최대 Depth))
    O(W*N^2) = O(25,000)


    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> DFS

    - 예외처리 : target이 words 안에 없다면 0을 반환

    1. dfs 탐색을 사용하여 백 트래킹을 사용한다.
        1-1. Base Condition 탐색 노드와 target 값이 같다면 정답에 count 추가하기
        1-2. is_similar를 통해 두 단어가 한 알파벳 차이인지 확인 및 방문한 단어인지 검사
            - 다음 단어들 확인
"""
from typing import List


def is_similiar(word1: str, word2: str) -> bool:
    """
    두 단어가 알파벳 하나 차이인지 확인

    Args:
        word1 (str)
        word2 (str)

    Returns:
        bool: 하나 차이는 True 아니면 False
    """

    count = 1
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            count -= 1
            if count < 0:
                return False
    return True


def dfs(
    node: str, target: str, count: int, counts: list, words: set, visited_words: set
):
    # 탐색하는 노드가 target와 같다면 count를 추가
    if node == target:
        counts.append(count)
        return

    # 단어를 순회하며 방문하지 않은 단어 중에 알파벳 하나 차이나는 알파벳을 탐색
    for word in words:
        if word not in visited_words and is_similiar(word1=node, word2=word):
            visited_words.add(word)
            dfs(word, target, count + 1, counts, words, visited_words)
            visited_words.remove(word)


def solution(begin: str, target: str, words: List):
    words = set(words)

    # 만약 target이 words 내부에 없다면 0을 Return
    if target not in words:
        return 0

    # dfs 탐색
    counts = []
    dfs(begin, target, 0, counts, words, set([begin]))

    return min(counts)


case1 = ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
case2 = ("hit", "cog", ["hot", "dot", "dog", "lot", "log"])

print(solution(*case1))  # 4
print(solution(*case2))  # 0
