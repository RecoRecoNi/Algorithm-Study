"""
풀이 시간: 35분

<input>
두 문자열
- 문자열은 알파벳 대문자(최대 1000글자)

<solution>
d[i][j]: word1의 i까지, word2의 j까지 있을 때 LCS(최장 공통 부분 수열)의 길이
1) word1[i] == word2[j]
- d[i][j] = d[i-1][j-1] + 1

2) word1[i] != word2[j]
- d[i][j] = max(d[i-1][j], d[i][j-1])

<시간 복잡도>
o(N^2)
"""
import sys
input = sys.stdin.readline


word1 = input().rstrip()
word2 = input().rstrip()

h, w = len(word1), len(word2)
d = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word1[i-1] == word2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])
print(d[h][w])