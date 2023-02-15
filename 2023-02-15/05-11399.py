N = int(input())
nums = list(map(int, input().split()))
nums.sort()

time = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    time[i] = time[i-1] + nums[i - 1]

answer = sum(time)

print(answer)