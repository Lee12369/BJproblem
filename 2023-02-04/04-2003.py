N, M = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
right = 0
cnt = 0
sum_nums = nums[0]

while right < N and left < N:    
    if right < N and sum_nums < M:
        right += 1
        if right > N - 1:
            break
        sum_nums += nums[right]
    
    elif sum_nums > M:
        sum_nums -= nums[left]
        left += 1
        
    elif sum_nums == M:
        sum_nums -= nums[left]
        left += 1
        cnt += 1
        
print(cnt)
        