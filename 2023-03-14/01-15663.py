import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

save_lst = []
visit_arr = []
visited = [0 for _ in range(N)]

def back_tracking(save_lst, visited, visit_arr):
    if len(save_lst) == M:
        temp = tuple(save_lst.copy())
        visit_arr.append(temp)
        return 0
            
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(nums[i])
            
            back_tracking(save_lst, visited, visit_arr)

            visited[i] = 0
            save_lst.pop()

back_tracking(save_lst, visited, visit_arr)
visit_arr = list(dict.fromkeys(visit_arr))

for tpl in visit_arr:
    for ans in tpl:
        print(ans, end=' ')
    print()