N = int(input())

dp = [-1 for _ in range(N + 1)]

for i in range(N + 1):
    if i % 5 == 0:
        dp[i] = i // 5
    elif i % 2 == 0:
        dp[i] = i // 2

for i in range(3, N + 1):
    k = i - i % 5
    for j in range(k, -1, -5):
        if dp[i - j] != -1:
            dp[i] = dp[j] + dp[i - j]
            break

ans = dp[N]

print(ans)