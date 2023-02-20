N = int(input())
arr = [[1 for _ in range(10)] for _ in range(N)]

for i in range(1, N):
    for j in range(1, 10):
        arr[i][j] = (arr[i - 1][j] + arr[i][j - 1]) % 10007

ans = sum(arr[N - 1]) % 10007

print(ans)