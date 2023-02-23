N = int(input())

dp = [0 for _ in range(N + 1)]
dp[1] = 0

for i in range(2, N + 1):
    case_1 = N
    case_2 = N
    if i % 3 == 0:
        case_1 = dp[i // 3] + 1
    
    if i % 2 == 0:
        case_2 = dp[i // 2] + 1
    
    case_3 = dp[i - 1] + 1

    cases = [case_1, case_2, case_3]

    dp[i] = min(cases)

ans = [N]
while N > 1:
    M = dp[N] - 1
    if N % 3 == 0 and dp[N // 3] == M:
        N //= 3

    elif N % 2 == 0 and dp[N // 2] == M:
        N //= 2

    elif dp[N - 1] == M:
        N -= 1
    
    ans.append(N)
    
print(dp[-1])
for x in ans:
    print(x, end=' ')