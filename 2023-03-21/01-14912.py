N, d = map(int, input().split())

cnt = 0
for num in range(1, N + 1):
    lst = list(str(num))
    cnt += lst.count(str(d))

print(cnt)