D, K = map(int, input().split())

dp = [0 for _ in range(31)]
dp[1] = [1, 0]
dp[2] = [0, 1]
for i in range(3, D + 1):
    A = dp[i - 1][0] + dp[i - 2][0]
    B = dp[i - 1][1] + dp[i - 2][1]
    dp[i] = [A, B]


N = K // dp[D][0] 
for i in range(1, N):
    M = K - i * dp[D][0]
    if M % dp[D][1] == 0:
        ans_A = i
        ans_B = M // dp[D][1]
        break

print(ans_A)
print(ans_B)
