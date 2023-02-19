N = int(input())
dp = [1, 3]
for i in range(2, N):
    M = dp[i - 1] + dp[i - 2] * 2
    dp.append(M)

ans = dp[N - 1] % 10007

print(ans)
