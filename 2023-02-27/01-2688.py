dp = [[1 for _ in range(10)] for _ in range(64)]

for i in range(1, 64):
    for j in range(10):
        if j > 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        else:
             dp[i][j] = 1
        
T = int(input())
for _ in range(T):
    N = int(input())

    ans = sum(dp[N - 1])

    print(ans)