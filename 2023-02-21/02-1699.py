N = int(input())

dp = [100000 for _ in range(N + 1)]
M = 0
while M ** 2 < N + 1:
    dp[M ** 2] = 1
    M += 1

for i in range(N + 1):
    if dp[i] == 1:
        continue
    
    k = 0
    j = 0
    while k < i:
        if dp[i] > dp[i - k] + 1:
            dp[i] = 1 + dp[i - k] 
        j += 1
        k = j * j 
print(dp[N])