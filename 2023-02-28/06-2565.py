N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x :x[0])

dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1) 

ans = N - max(dp)

print(ans)