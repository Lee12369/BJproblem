import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]

dp = [0 for _ in range(N + 1)]
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    if i in vip or i - 1 in vip:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

ans = dp[N]

print(ans)