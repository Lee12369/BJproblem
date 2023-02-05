import sys
input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().rstrip('\n').split()))
nums.sort(reverse=True)

left = 0
right = 0
cnt = 0
while left < N:
    while right < N and nums[right] >= nums[left] * 0.9:
        right += 1
    if right == N and nums[right - 1] == nums[left] * 0.9:
        cnt += right - left
    else:
        cnt += right -left - 1

    left += 1

print(cnt)