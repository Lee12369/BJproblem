N = int(input())
nums = list(map(int, input().split()))

dp = [-1 for _ in range(N)]
dp[0] = 0
for i in range(N):
    if dp[i] == -1:
        continue
    M = i + nums[i] + 1
    if M > N:
        M = N
    for j in range(i + 1, M):
        if dp[j] == -1 or dp[j] > dp[i] + 1:
            dp[j] = dp[i] + 1

ans = dp[N - 1]

print(ans)
        
            