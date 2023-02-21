N = int(input())
nums = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
            dp[i] = dp[j] + nums[i]

ans = max(dp)

print(ans)