T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    dp = [nums[i] for i in range(N)]
    for i in range(1, N):
        M = dp[i - 1] + nums[i]
        if dp[i] < M:
            dp[i] = M
    
    ans = max(dp)
    
    print(ans)