import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1
    for x in coins:
        for i in range(x, M + 1):        
            dp[i] += dp[i - x] 
    
    ans = dp[M]

    print(ans)
