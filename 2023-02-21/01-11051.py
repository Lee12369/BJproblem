N, K = map(int, input().split())
arr = [[0 for _ in range(i + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i + 1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = (arr[i - 1][j] + arr[i - 1][j - 1]) % 10007

ans = arr[N][K]  % 10007

print(ans)