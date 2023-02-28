N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

default = 10001
dp = [default for _ in range(K + 1)]

for num in nums:
    for i in range(num, K + 1):
        M = i // num
        res = i % num
        if res == 0:
            dp[i] = M
            continue
        if dp[i - num] != default:
            dp[i] = min(dp[i], dp[i - num] + 1) 

ans = dp[K]
if ans == default:
    ans = -1