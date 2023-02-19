N = int(input())
nums = [int(input()) for _ in range(N)]

if N > 2:
    dp = [[nums[0], nums[0]], [nums[0] + nums[1], nums[1]], [nums[0] + nums[1], nums[0] + nums[2], nums[1] + nums[2]]]
    max_num = dp[1][0]
    for i in range(3, N):
        a = dp[i - 1][2]
        b = nums[i] + dp[i - 1][0]
        c = nums[i] + dp[i - 1][1]
        dp.append([a, b, c])
        max_num = max(max_num, a, b, c)
else:
    max_num = nums[0] + nums[1]

print(max_num)
