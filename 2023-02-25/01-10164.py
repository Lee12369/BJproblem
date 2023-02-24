N, M, K = map(int, input().split())

if K > 0:
    circle_x = K // M
    circle_y = K % M - 1
    if circle_y < 0:
        circle_x -= 1
        circle_y += M
else:
    circle_x = 0
    circle_y = 0

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1

dx = [0, -1]
dy = [-1, 0]
for i in range(circle_x + 1):
    for j in range(circle_y + 1):
        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < M:
                dp[i][j] += dp[ni][nj]

for i in range(circle_x, N):
    for j in range(circle_y, M):
        if i == circle_x and j == circle_y:
            continue
        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < M:
                dp[i][j] += dp[ni][nj]

ans = dp[N - 1][M - 1]

print(ans)


