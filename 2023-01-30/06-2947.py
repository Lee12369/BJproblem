nums = list(map(int, input().split()))
sort_nums = [i for i in range(1, 6)]
N = 0

while nums != sort_nums:
    for j in range(4 - N):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
            for x in nums:
                print(x, end=' ')

            print()
    N += 1
