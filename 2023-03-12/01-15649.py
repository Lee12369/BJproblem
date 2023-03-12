N, M = map(int, input().split())

visited = [0 for _ in range(N + 1)]

lst = []
def back_tracking(lst, visited):
    if len(lst) == M:
        for x in lst:
            print(x, end=' ')
        print()
        return 0

    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            lst.append(i)
            back_tracking(lst, visited)

            visited[i] = 0
            lst.pop()

back_tracking(lst,visited)