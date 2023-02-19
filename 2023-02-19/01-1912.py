N = int(input())
nums = list(map(int, input().split()))
dp = [0 for _ in range(N)]

dp[0] = nums[0]
for i in range(1, N):
    dp[i] = dp[i - 1] + nums[i]
    if dp[i] < nums[i]:
        dp[i] = nums[i]

ans = max(dp)

print(ans)