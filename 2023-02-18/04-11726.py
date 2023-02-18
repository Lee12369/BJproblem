N = int(input())

dic = {
    1:1,
    2:2,
}
for x in range(3, N + 1):
    dic[x] = dic[x - 1] + dic[x - 2]

ans = dic[N] % 10007

print(ans)