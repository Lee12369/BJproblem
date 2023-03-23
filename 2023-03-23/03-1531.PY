N, M = map(int, input().split())

arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    start_x, start_y, end_x, end_y = map(int, input().split())
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            arr[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] > M:
            cnt += 1

print(cnt)