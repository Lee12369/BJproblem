N = int(input())
nums = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if nums[i] < nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

ans = N - max(dp)

print(ans)