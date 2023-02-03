import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().rstrip('\n').split()))
nums.sort()

left = 0
right = N - 1
min_M = abs(nums[N-1] + nums[0])
while True:
    M = nums[right] + nums[left]
    M_abs = abs(M)
    if min_M >= M_abs:
        min_M = M_abs   
        min_L, min_R = nums[left], nums[right]

    if M > 0:
        right -= 1

    elif M < 0:
        left += 1
    
    elif M == 0:
        print(nums[left], nums[right])
        break

    if left == right:
        print(min_L, min_R)
        break