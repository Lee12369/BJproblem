import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

save_lst = []
visit_lst = []

def back_tracking(start, save_lst, visit_lst):
    if len(save_lst) == M:
        temp = tuple(save_lst.copy())
        visit_lst.append(temp)
        return 0
    
    for i in range(start, N):
        save_lst.append(nums[i])

        back_tracking(i, save_lst, visit_lst)

        save_lst.pop()


back_tracking(0, save_lst, visit_lst)

visit_lst = list(dict.fromkeys(visit_lst))

for tpl in visit_lst:
    for x in tpl:
        print(x, end=' ')
    print()

