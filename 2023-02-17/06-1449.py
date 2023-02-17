N, L = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

start = nums[0] - 0.5
end = start + L
cnt = 1
for x in nums:
    if start <= x < end:
        pass

    else:
        start = x - 0.5
        end = start + L
        cnt += 1

print(cnt)
