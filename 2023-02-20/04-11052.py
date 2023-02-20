import sys
input = sys.stdin.readline

N = int(input())
temp = list(map(int, input().split()))
nums = [0]
nums.extend(temp)

dp = [0 for _ in range(N + 1)]
dp[0] = nums[0]
for i in range(1, N + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i], dp[j] + nums[i - j])

ans = max(dp)

print(ans)

