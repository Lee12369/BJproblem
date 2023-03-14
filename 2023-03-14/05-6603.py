import sys
input = sys.stdin.readline

def back_tracking(start, save_lst):
    if len(save_lst) == 6:
        for x in save_lst:
            print(x, end=' ')
        print()
        return 0

    for i in range(start, N + 1):
        save_lst.append(nums[i])

        back_tracking(i + 1, save_lst)

        save_lst.pop() 

nums = list(map(int, input().split()))    
while nums != [0]:
    N = nums[0]
    save_lst = []
    back_tracking(1, save_lst)

    nums = list(map(int, input().split()))
    
    if nums != [0]:
        print()