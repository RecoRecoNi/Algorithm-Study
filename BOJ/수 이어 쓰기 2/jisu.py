"""
풀이 시작 : 2023-09-14 19:39

숫자 길이 -> 숫자 개수
1 -> 9          9
2 -> 90         180
3 -> 900        2700
4 -> 9000       36000
5 -> 90000      450000
...             ...

- 이를 배열에 담고 누적합을 구하면 1부터 i자리 수 끝까지 수의 길이를 알 수 있다.
  - ex) 1부터 2자리 끝 수까지의 길이 : 9 + 180 = 189
- 바로 직전 자리수 끝까지 수의 길이를 K에서 빼준다.
  - ex) K가 23일 때 직전 자리 수(1자리 수)의 길이인 9를 빼면 14
- (K-1)을 직전 자리수 +1(현재 자리 수)로 나눠준 몫은 현재 자리 수에서 몇 번째 수까지 구해야 하는지에 해당된다.
    - K-1(13) // 2(직전 자리 수 +1) = 6
    - 두번째 자리수에서 6번쨰 수까지 => 10 11 12 13 14 15 16 까지 구해야 한다.
    - 이 때 이 수가 N 보다 작으면 -1 출력
- (K-1)을 직전 자리수 +1(현재 자리 수)로 나눈 나머지는 마지막 구한 수의 자리 수에 해당된다.
    - 마지막 구한 수 : 16
    - K-1(13) % 2(직전 자리 수 +1) = 1
    - "16"[1] = 6

너무 어거지로 정답을 이끌어낸 느낌인데, 다른 풀이도 이 풀이와 다른 점은 없었음
i자리 수를 끝까지 이어붙였을 때 길이를 구해 활용하는 게 핵심인 것 같다.


풀이 완료 : 2023-09-14 20:59 (풀이 시간 : 1시간 20분)
"""

N, K = map(int, input().split())

mem = [0] + [9 * (i + 1) * (10**i) for i in range(9)]
for i in range(1, len(mem)):  # 개수 누적 합 구하기
    mem[i] += mem[i - 1]

for idx, num_length in enumerate(mem):
    if num_length >= K:
        cut = idx - 1  # 직전 자리수
        break

K -= mem[cut]  # 이전 자리수까지 수 개수 빼기

m, r = divmod((K - 1), cut + 1)  # 16, 20 line 참고
answer_num = 10 ** (cut) + m

print(str(answer_num)[r] if N >= answer_num else -1)
