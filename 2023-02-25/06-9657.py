N = int(input())

dp = [0 for _ in range(1001)]
dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'
dp[4] = 'SK'

for i in range(5, N + 1):
    if dp[i - 1] == 'CY' or dp[i - 3] == 'CY' or dp[i - 4] == 'CY':
        dp[i] = 'SK'
    else:
        dp[i] = 'CY'

ans = dp[N]

print(ans)