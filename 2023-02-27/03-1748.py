N = int(input())

if N > 0:
    dp = [0 for _ in range(N + 1)]
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % (10 ** 9)
    
    ans_check = 1
    ans = dp[N]

elif N < 0:
    dp = [0 for _ in range(2 - N)]
    dp[0] = 1
    for i in range(2, 2 - N):
        dp[i] = dp[i - 2] - dp[i - 1]

    if dp[-1] > 0:
        ans_check = 1
        ans = dp[-1]

    elif dp[-1] < 0:
        ans_check = -1
        ans = -dp[-1]
    
    else:
        ans_check = 0
        ans = 0

elif N == 0:
    ans_check = 0
    ans = 0

print(ans_check)
print(ans)