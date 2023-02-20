N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N)]

for x in range(N):
    if x + arr[x][0] - 1 < N:
        dp[x] = max(dp[x], arr[x][1])

    next = x + arr[x][0]
    for y in range(next, N):
        if y + arr[y][0] - 1 < N:
            dp[y] = max(dp[y], dp[x] + arr[y][1])

ans = max(dp)

print(ans)
