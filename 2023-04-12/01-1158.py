N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]

ans = '<'
curr = -1
while nums:
    curr += K
    curr %= N
    ans += str(nums[curr]) +', '
    nums = nums[:curr] + nums[curr + 1:]
    curr -= 1
    N -= 1

ans = ans[:-2] + '>'

print(ans)