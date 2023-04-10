A = int(input())
T = int(input())
word = int(input())

N = 1
total_cnt = -1
word_cnt = 0
while word_cnt < T:
    lst = [0, 1] * 2 + [0] * (N + 1) + [1] * (N + 1)
    for x in lst:
        total_cnt += 1
        if x == word:
            word_cnt += 1

        if word_cnt == T:
            break
    N += 1

ans = total_cnt % A

print(ans)