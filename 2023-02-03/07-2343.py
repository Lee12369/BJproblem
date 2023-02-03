import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip('\n').split())
nums = list(map(int, input().rstrip('\n').split()))

max_num = max(nums)
left = max_num
right = 100000 * 9999

while True:
    mid = (left + right) // 2
    
    sum = 0
    cnt = 0
    for x in nums:
        sum += x
        if sum > mid: 
            cnt += 1
            sum = x
            
        elif sum == mid:
            cnt += 1
            sum = 0      
    if sum != 0:
        cnt += 1

    if left == mid:
        if left == max_num and cnt <= M:
            print(left)
        else:
            print(right)
        break

    if cnt <= M:
        right = mid
    elif cnt > M:
        left = mid  
