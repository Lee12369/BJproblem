import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

dp = [0 for _ in range(N)]

min_num = 5
for i in range(N):
    cnt = 5
    lst = nums[i:i + 5]
    check_lst = [i for i in range(nums[i], nums[i] + 5)]
    for x in lst:
        if x in check_lst:
            cnt -= 1
    
    min_num = min(min_num, cnt)

print(min_num)
