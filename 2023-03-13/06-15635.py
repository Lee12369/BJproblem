N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

save_lst = []
def back_tracking(start, save_lst):
    if len(save_lst) == M:
        for x in save_lst:
            print(x, end=' ')
        print()
        return 0
    
    for i in range(start, N):
        save_lst.append(nums[i])

        back_tracking(i + 1, save_lst)

        save_lst.pop()

back_tracking(0, save_lst)