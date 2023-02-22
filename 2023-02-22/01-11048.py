import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j] + arr[i - 1][j - 1]
        
        else:
            dp[i][j] = dp[i][j - 1] + arr[i - 1][j - 1]

ans = dp[N][M]

print(ans)       