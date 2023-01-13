while True:
    nums = input('')
    if nums != '0 0':
        nums = nums.split()
        A = int(nums[0])
        B = int(nums[1])
        print(A + B)
    else:
        break