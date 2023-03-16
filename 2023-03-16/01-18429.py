import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

score = 500
cnt = 0
visited = [0 for _ in range(N)]
lst_ans = []
def back_tracking(score, cnt, visited):
    if score < 500:
        return 0
    
    if cnt == N:
        lst_ans.append(score)
        return 0
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            save_cnt = cnt + 1
            save_score = score - K + nums[i]

            back_tracking(save_score, save_cnt, visited)

            visited[i] = 0

back_tracking(score, cnt, visited)

print(len(lst_ans))