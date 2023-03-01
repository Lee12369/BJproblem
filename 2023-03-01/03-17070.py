N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

dx = [0, -1, -1]
dy = [-1, 0, -1]

# dp[][] = [가로, 세로, 대각선]
dp[0][1] = [1, 0 , 0]
for i in range(N):
    for j in range(2, N):
        if arr[i][j] == 1:
            continue
        for k in range(3):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < N:
                if k == 0:
                    dp[i][j][0] += dp[ni][nj][0] + dp[ni][nj][2] 

                elif k == 1:
                    dp[i][j][1] += dp[ni][nj][1] + dp[ni][nj][2]
                    
                elif k == 2 and arr[ni + 1][nj] == 0 and arr[ni][nj + 1] == 0:
                    dp[i][j][2] += dp[ni][nj][0] + dp[ni][nj][1] + dp[ni][nj][2]

ans = sum(dp[N - 1][N - 1])

print(ans)


                