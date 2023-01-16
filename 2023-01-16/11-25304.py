X, N = [int(input()) for _ in range(2)]

lst = [list(map(int, input().split())) for _ in range(N)]

all_sum = 0
for i in range(N):
    all_sum += lst[i][0] * lst[i][1]

if all_sum == X:
    print('Yes')
else:
    print('No')
