N = int(input())

dp = [0 for _ in range(N)]
dp[0] = 1
if N > 1:
    dp[1] = 1

for i in range(2, N):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = dp[N - 1]

print(ans)