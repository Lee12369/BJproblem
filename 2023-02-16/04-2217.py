import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

max_sum = 0
for i in range(N):
    sum = nums[i] * (N - i)
    max_sum = max(max_sum, sum)

print(max_sum)  