N = int(input())
dic = {1:0}


for x in range(2, N + 1):
    cnt_1 = 10 ** 6
    cnt_2 = 10 ** 6
    if x % 2 == 0:
        cnt_1 = dic[x // 2] + 1
    if x % 3 == 0:
        cnt_2 = dic[x // 3] + 1

    cnt_3 = dic[x - 1] + 1
    dic[x] = min(cnt_1, cnt_2, cnt_3)

ans = dic[N]

print(ans)