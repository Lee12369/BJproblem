N = int(input())

dp = [0 for _ in range(N + 1)]
dp[0] = 1

for i in range(1, N + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]

ans = dp[N]

print(ans)