P = [1,1,1,2,2]
dp = [0 for _ in range(100)]

for i in range(100):
    if i >= 5: 
        dp[i] = dp[i - 1] + dp[i - 5]
    else:
        dp[i] = P[i]

T = int(input())
for _ in range(T):
    N = int(input())
    
    ans = dp[N - 1]

    print(ans)