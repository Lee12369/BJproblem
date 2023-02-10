N = int(input())
nums = [int(input()) for _ in range(N)]

cnt = 0
while True:
    max_num = max(nums)
    idx = nums.index(max_num)
    if idx != 0:
        nums[idx] -= 1
        nums[0] += 1
        cnt += 1
    
    elif idx == 0:
        if nums.count(max_num) == 1:
            answer = cnt
        else:
            answer = cnt + 1
        break

print(answer)