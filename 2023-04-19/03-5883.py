N = int(input())
nums = [int(input()) for _ in range(N)]
storage = list(set(nums))

max_length = 1
for x in storage:
    prev_num = nums[0]
    length = 1
    for i in range(1, N):
        if x == nums[i]:
            continue

        if nums[i] == prev_num:
            length += 1
            max_length = max(max_length, length)
            
        else:
            prev_num = nums[i]
            length = 1

print(max_length)