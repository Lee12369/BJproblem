N = int(input())

nums = list(map(int, input().split()))

i = 0
len_asc = 1
len_des = 1
max_len = 1
same_num = 0

while i < N - 1:    
    if nums[i] < nums[i+1]:
        len_des = 1
        while i < N - 1 and nums[i] < nums[i + 1]:
            i += 1
            len_asc += 1
        
        max_len = max(max_len, len_asc)

    elif nums[i] > nums[i + 1]:
        len_asc = 1 
        while i < N - 1 and nums[i] > nums[i + 1]:
            i += 1
            len_des += 1

        max_len = max(max_len, len_des)

    elif nums[i] == nums[i + 1]:
        same_num = 0
        while i < N - 1 and nums[i] == nums[i + 1]:
            i += 1
            same_num += 1
        
        len_asc += same_num
        len_des += same_num
        
        max_len = max(max_len, len_asc, len_des)

print(max_len)    