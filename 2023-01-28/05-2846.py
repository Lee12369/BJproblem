N = int(input())
nums = list(map(int,input().split()))

curr = nums[0]
high = 0
ans_lst = []
for x in nums[1:]:
    if x > curr:
        high += x - curr    
    else:
        high = 0
    
    ans_lst.append(high)
    curr = x

print(max(ans_lst))