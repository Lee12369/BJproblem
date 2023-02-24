N = int(input())

dp = [1 for _ in range(N + 1)]
dp[0] = 0

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = dp[N]

print(ans)
