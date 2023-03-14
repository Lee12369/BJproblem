import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

save_lst = []

def back_tracking(save_lst):
    if len(save_lst) == M:
        for ans in save_lst:
            print(ans, end=' ')
        print()
        return 0
    
    for i in range(N):
        save_lst.append(nums[i])

        back_tracking(save_lst)

        save_lst.pop()

back_tracking(save_lst)