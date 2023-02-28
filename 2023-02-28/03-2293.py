import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [0 for _ in range(K + 1)]
dp[0] = 1
for _ in range(N):
    num = int(input())
    for i in range(num, K + 1):
        dp[i] += dp[i - num]

ans = dp[K]

print(ans)



