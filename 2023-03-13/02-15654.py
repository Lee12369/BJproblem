import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

save_lst = []
visited = [0 for _ in range(N)]
def back_tracking(save_lst, visited):
    if len(save_lst) == M:
        for x in save_lst:
            print(x, end=' ')
        print()
        return 0
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(nums[i])

            back_tracking(save_lst, visited) 

            visited[i] = 0
            save_lst.pop()

back_tracking(save_lst, visited)

