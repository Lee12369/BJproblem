def get_sort():
    for j in range(i - 1):
        if lst[j] == i - 1:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

N = int(input())
dic = {input() : i for i in range(N)}
lst = [dic[input()] for _ in range(N)]


cnt = 0
for i in range(N, 0, -1):
    if lst[i - 1] != i - 1:
        get_sort()
        cnt += 1

print(cnt)