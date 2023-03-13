import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

save_lst = []
visited = [0 for _ in range(N)]
score_lst = []
def back_tracking(save_lst, visited):
    if len(save_lst) == N:
        score = 0
        for i in range(N - 1):
            score += abs(save_lst[i] - save_lst[i + 1])
        score_lst.append(score)
        return 0
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(nums[i])

            back_tracking(save_lst, visited)

            visited[i] = 0
            save_lst.pop()

back_tracking(save_lst, visited)

ans = max(score_lst)

print(ans)