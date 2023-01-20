import sys
N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

cnt = 0
for i in range(100):
    cnt += arr[i].count(1)

print(cnt)