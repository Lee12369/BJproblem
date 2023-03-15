import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

save_lst = []
ans_lst = []
def back_tracking(start, save_lst):
    if len(save_lst) == M:
        ans_lst.append(tuple(save_lst))
        return 0
    
    for i in range(start, N):
        save_lst.append(nums[i])

        back_tracking(i + 1, save_lst)

        save_lst.pop()

back_tracking(0, save_lst)

ans_lst = list(dict.fromkeys(ans_lst))

for tpl in ans_lst:
    for x in tpl:
        print(x, end=' ')
    print()