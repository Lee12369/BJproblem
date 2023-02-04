import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip('\n').split())
nums = list(map(int, input().rstrip('\n').split()))

pre = 0
for i in range(K):
    pre += nums[i]
answer = pre

for i in range(1, N- K + 1):
    curr = pre - nums[i - 1] + nums[i - 1 + K]
    answer = max(answer, curr)
    pre = curr
    
print(answer)