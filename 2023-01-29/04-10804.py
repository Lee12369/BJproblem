nums = [i for i in range(1,21)]

for _ in range(10):
    i, j = map(int, input().split())
    if i == 1:
        nums[i - 1 : j] = nums[j - 1 :: -1]
    else:
        nums[i - 1 : j] = nums[j - 1 : i - 2 : -1]

for x in nums:
    print(x, end=' ')
