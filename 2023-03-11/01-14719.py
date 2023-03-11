import sys
input = sys.stdin.readline

H, W = map(int, input().split())
nums = list(map(int, input().split()))

rain = 0

for i in range(1, W - 1):
    left = max(nums[:i])
    right = max(nums[i + 1:])

    N = min(left, right)
    if nums[i] <= N:
        rain += N - nums[i]

print(rain)