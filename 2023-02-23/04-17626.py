N = int(input())

dp = [i for i in range(N + 1)]

M = 1
K = 1
while K <= N:
    dp[K] = 1
    M += 1
    K = M * M 

for i in range(1, N + 1):
    M = 1
    K = 1
    while K <= i:
        if dp[i] > 1 + dp[i - K]:
            dp[i] = 1 + dp[i - K]
        M += 1
        K = M * M 

ans = dp[N]

print(ans)