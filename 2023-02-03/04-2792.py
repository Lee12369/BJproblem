import sys
import math
input = sys.stdin.readline
N, M = map(int, input().rstrip('\n').split())
nums = [int(input()) for _ in range(M)]

max_jeal = 0
left = 1
right = (10 ** 9) + 1
while True:
    mid = (left + right) // 2

    cnt = 0
    for x in nums:
        cnt += math.ceil(x / mid)

    if mid == left:
        if left == 1:
            print(left)
    
        else:
            print(right)        
        break
    if cnt <= N:
        right = mid

    elif cnt > N:
        left = mid
