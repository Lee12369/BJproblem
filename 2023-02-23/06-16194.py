N = int(input())

nums = [0]
lst = list(map(int, input().split()))
nums.extend(lst)

dp = [nums[i] for i in range(N + 1)]

for i in range(N + 1):
    for j in range(i + 1):
        M = dp[i - j] + dp[j]
        if dp[i] > M:
           dp[i] = M

ans = dp[N]

print(ans)
