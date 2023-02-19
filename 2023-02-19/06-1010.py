T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(i, M + 1):
            if i == 1:
                dp[i][j] = j
                continue

            if i == j:
                dp[i][j] = 1
            elif j > i:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    ans = dp[N][M]
    
    print(ans)
