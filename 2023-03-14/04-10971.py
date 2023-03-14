import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [0 for _ in range(N)]
save_lst = []
score = 0
ans_lst = []
def back_tracking(score, save_lst, visited):
    if len(save_lst) == N:
        if arr[save_lst[-1]][save_lst[0]] > 0:
            final_score = score + arr[save_lst[-1]][save_lst[0]]
            ans_lst.append(final_score)
        return 0
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(i)

            if len(save_lst) > 1:
                if arr[save_lst[-2]][save_lst[-1]] > 0:
                    save_score = score + arr[save_lst[-2]][save_lst[-1]]
                else:
                    visited[i] = 0
                    save_lst.pop()
                    return 0
            else:
                save_score = int(score)

            back_tracking(save_score, save_lst, visited)

            visited[i] = 0
            save_lst.pop()
            
back_tracking(score, save_lst, visited)

ans = min(ans_lst)

print(ans)