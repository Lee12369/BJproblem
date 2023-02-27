import sys
input = sys.stdin.readline

N ,D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [i for i in range(D + 1)]

for i in range(1, D + 1):
    for j in range(N):
        if arr[j][1] == i:
            M = dp[arr[j][0]] + arr[j][2]
            if dp[i] > M:
                dp[i] = M
    if dp[i] > dp[i - 1]:
        dp[i] = dp[i - 1] + 1

ans = dp[D]

print(ans)