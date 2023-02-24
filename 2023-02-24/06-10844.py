N = int(input())

dp = [0 for _ in range(N + 1)]

# dp[] = [0과 9로 끝나는 수, 1과 8로 끝나는 수, 2과 7로 끝나는 수, 3과 6로 끝나는 수, 4과 5로 끝나는 수]

dp[1] = [1, 2, 2, 2, 2]

for i in range(2, N + 1):
    last_09 = (dp[i - 1][1]) % 10 ** 9
    last_18 = (dp[i - 1][0] + dp[i - 1][2]) % 10 ** 9
    last_27 = (dp[i - 1][1] + dp[i - 1][3]) % 10 ** 9
    last_36 = (dp[i - 1][2] + dp[i - 1][4]) % 10 ** 9
    last_45 = (dp[i - 1][3] + dp[i - 1][4]) % 10 ** 9
    
    dp[i] = [last_09, last_18, last_27, last_36, last_45]

ans = sum(dp[N]) % 10 ** 9

print(ans)