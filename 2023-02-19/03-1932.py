N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(i)] for i in range(1, N + 1)]
dp[0][0] = arr[0][0]

for i in range(1, N):
    for j in range(i + 1):
        case_1 = 0
        case_2 = 0
        if j > 0:
            case_1 = arr[i][j] + dp[i - 1][j - 1]
            
        if j < i:
            case_2 = arr[i][j] + dp[i - 1][j]
        
        dp[i][j] = max(case_1, case_2)

ans = max(dp[N - 1])

print(ans)