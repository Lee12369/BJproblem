N, K = map(int, input().split())
dp = [[0 for _ in range(i)] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i):
        if j == 0 or j == i - 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

ans = dp[N][K - 1]

print(ans)

