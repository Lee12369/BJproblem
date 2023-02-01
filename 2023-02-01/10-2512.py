import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().rstrip('\n').split()))
able_total_num = int(input())

max_num = max(nums)
min_num = 0

sum_nums = sum(nums)
if sum_nums > able_total_num:
    while True:
        pivot = (max_num + min_num) // 2
        sum_needs = 0
        for x in nums:
            if x > pivot:
                sum_needs += pivot
            else:
                sum_needs += x
                
        if sum_needs == able_total_num or min_num == pivot:
            break
        
        elif sum_needs > able_total_num:
            max_num = pivot

        elif sum_needs < able_total_num:
            min_num = pivot

else:
    pivot = max_num
    
print(pivot)