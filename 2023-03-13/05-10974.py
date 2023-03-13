N = int(input())

save_lst = []
visited = [0 for _ in range(N + 1)]
def back_tracking(save_lst, visited):
    if len(save_lst) == N:
        for x in save_lst:
            print(x, end=' ')
        print()
        return 0

    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(i)

            back_tracking(save_lst, visited)

            visited[i] = 0
            save_lst.pop()

back_tracking(save_lst, visited)
