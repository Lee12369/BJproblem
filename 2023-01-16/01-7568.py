N = int(input())
lst = [list(map(int, input().split())) for i in range(N)]

rank = [0 for i in range(N)]
for i in range(N):
    cts = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cts += 1
    rank[i] = cts + 1
for i in rank:
    print(i, end=" ")