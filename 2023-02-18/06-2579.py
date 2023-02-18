N = int(input())
nums = [int(input()) for _ in range(N)]

if N > 1:
    arr = [[nums[0], nums[0]], [nums[0] + nums[1], nums[1]]]

    for i in range(2, N):
        x = nums[i] + arr[i - 1][1] 
        y = nums[i] + max(arr[i - 2][0], arr[i - 2][1]) 
        arr.append([x, y])

else:
    arr = [[nums[0], nums[0]]]
    
ans = max(arr[N - 1])

print(ans) 

