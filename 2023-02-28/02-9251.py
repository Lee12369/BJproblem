std = input()
word = input()

M = len(std)
N = len(word)
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        if word[i] == std[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

ans = dp[N][M]

print(ans) 
