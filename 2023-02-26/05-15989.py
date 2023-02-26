import sys
input = sys.stdin.readline

dp = [0 for _ in range(10001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 10001):
    dp[i] = dp[i - 1] + dp[i - 2] - dp[i - 3]
    if i % 3 == 0:
        dp[i] += 1

T = int(input())
for _ in range(T):
    N = int(input())

    ans = dp[N]

    print(ans)