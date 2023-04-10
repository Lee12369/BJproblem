import math, sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

def round(number):
    if (number * 10) % 10 >= 5:
        return math.ceil(number)
    else:
        return math.floor(number)

M = round(N * 0.15)
nums = nums[M: N - M]
if len(nums) > 0:
    average = sum(nums) / len(nums)
    ans = round(average)

else:
    ans = 0

print(ans)