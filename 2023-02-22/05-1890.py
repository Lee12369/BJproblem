N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
dx = [0, 1]
dy = [1, 0]
for i in range(N):
    for j in range(N):
        if dp[i][j] > 0:
            for k in range(2):
                ni = i + dx[k] * arr[i][j]
                nj = j + dy[k] * arr[i][j]
                if 0 <= ni < N and 0 <= nj < N and arr[i][j] > 0:
                    dp[ni][nj] += dp[i][j]
                    
ans = dp[N - 1][N - 1]

print(ans)

