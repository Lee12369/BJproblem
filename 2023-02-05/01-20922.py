from collections import defaultdict
import sys
input = sys.stdin.readline

def get_end_length():
    if dic[nums[right]] <= K:
        length = right - left + 1
    else:
        length = right - left

    return length


N, K = map(int, input().rstrip('\n').split())
nums = list(map(int, input().rstrip('\n').split()))

dic = defaultdict(int)
    
if N == 1:
    max_length = 1
    
else:
    left = 0
    right = 0
    dic[nums[left]] += 1
    
    max_length = 0
    while True:
        L = nums[left]
        R = nums[right]
        
        if dic[R] <= K:
            right += 1
            dic[nums[right]] += 1
            if right == N - 1:
                length = get_end_length()
                max_length = max(max_length, length)
                break     
        else:
            length = right - left
            dic[L] -= 1
            left += 1
            max_length = max(max_length, length)

print(max_length)
