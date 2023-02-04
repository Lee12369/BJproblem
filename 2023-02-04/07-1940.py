import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
sirial_nums = list(map(int, input().rstrip('\n').split()))
sirial_nums.sort()

left = 0
right = N - 1
cnt = 0
while left != right:
    L = sirial_nums[left]
    R = sirial_nums[right]

    LR = L + R
  
    if LR > M:
        right -= 1
    elif LR < M:
        left += 1
    elif LR == M:
        left += 1
        cnt += 1

print(cnt)