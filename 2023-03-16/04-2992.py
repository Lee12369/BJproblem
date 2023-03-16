X = input()

len_X = len(X)
save_lst = []
visited = [0 for _ in range(len_X)]
ans_lst = []

def back_tracking(save_lst, visited):
    if len(save_lst) == len_X:
        num = ''
        for y in save_lst:
            num += y
        ans_lst.append(int(num))

    for i in range(len_X):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(X[i])

            back_tracking(save_lst, visited)

            visited[i] = 0
            save_lst.pop()

back_tracking(save_lst, visited)

ans_lst = list(dict.fromkeys(ans_lst))
ans_lst.sort()
ans_idx = ans_lst.index(int(X)) + 1

if ans_idx < len(ans_lst):
    print(ans_lst[ans_idx])
else:
    print(0)
