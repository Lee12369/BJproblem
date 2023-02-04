import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().rstrip('\n').split()))
nums.sort()
x = int(input())

left = 0
right = n - 1
cnt = 0
while left != right:
    left_num = nums[left]
    right_num = nums[right]
    sum_num = left_num + right_num

    if sum_num > x:
        right -= 1
    
    elif sum_num < x:
        left += 1

    elif sum_num == x:
        left += 1
        cnt += 1

print(cnt)