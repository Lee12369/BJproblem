import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip('\n').split())

nums = list(map(int, input().rstrip('\n').split()))

M = nums.count(1)

if M >= K:
    left = nums.index(1)
    right = left + 1
    min_len = N
    cnt = 1
    while right < N and left < N:
        if cnt < K:
            while right < N and nums[right] != 1:
                right += 1
            cnt += 1
            if right == N and nums[right - 1] == 2:
                cnt -= 1
                
        if cnt == K:
            length = right - left + 1
            min_len = min(min_len, length)
            left += 1
            cnt -= 1
            while left < N and nums[left] != 1:
                left += 1
        
        right += 1
            
else:
    min_len = -1

print(min_len)