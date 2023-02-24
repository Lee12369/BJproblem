N = int(input())
nums = [float(input()) for _ in range(N)]

dp = [nums[i] for i in range(N)]

for i in range(1, N):
    if nums[i] == 0.0:
        continue

    M = dp[i - 1] * nums[i]
    if dp[i] < M:
        dp[i] = M

# 파이썬 round 함수 사용 시 5로 끝나면 올리는게 아닌 버리기 때문에 아래와 같은 처리를 함. 
max_dp = max(dp) + 0.000000000000001
max_dp = round(max_dp, 3)

print("{:.3f}".format(max_dp))
