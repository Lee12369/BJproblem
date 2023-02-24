import sys
input = sys.stdin.readline

# dp[] = [끝자리가 1인 수의 개수, 끝자리가 2인 수의 개수, 끝자리가 3인 수의 개수]
dp = [0 for _ in range(100001)]
dp[0] = [0, 0, 0]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    a = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    b = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    c = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009
    dp[i] = [a, b, c]

T = int(input())
for _ in range(T):
    N = int(input())
    
    ans = sum(dp[N]) % 1000000009

    print(ans)