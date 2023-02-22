import sys
input = sys.stdin.readline

dp = [[[1 for _ in range(21)] for _ in range(21)]  for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1,21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]

            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    
    if a <= 0 or b <= 0 or c <= 0:
        ans = 1

    elif a > 20 or b > 20 or c > 20:
        ans = dp[20][20][20]

    else:
        ans = dp[a][b][c]

    print("w({}, {}, {}) = {}".format(a, b, c, ans))

