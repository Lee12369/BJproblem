N = int(input())
nums = list(map(int, input().split()))

curr = 2
cnt = 0
for i in range(N):
    if curr == 2 and nums[i] == 0:
        curr = 0
        cnt += 1
    
    elif curr == 0 and nums[i] == 1:
        curr = 1
        cnt += 1
    
    elif curr == 1 and nums[i] == 2:
        curr = 2
        cnt += 1

print(cnt)