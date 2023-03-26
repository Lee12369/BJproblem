import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    
    max_num = 0
    max_idx_lst = []
    total_score = 0

    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_idx_lst = [i + 1]
        elif nums[i] == max_num:
            max_idx_lst.append(i + 1)
    
        total_score += nums[i]
    
    if len(max_idx_lst) == 1:
        if max_num > total_score / 2:
            print("majority winner {}".format(max_idx_lst[0]))

        else:
            print("minority winner {}".format(max_idx_lst[0]))

    else:
        print("no winner")