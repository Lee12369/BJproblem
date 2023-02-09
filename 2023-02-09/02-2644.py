from collections import defaultdict, deque
def dfs(dic, start, N, visited = []):
    queue = deque()
    queue.append(start)
    visited.append(start)
    lst = [0 for _ in range(N + 1)]
    while queue:
        x = queue.pop()
        for y in dic[x]:
            if y not in visited:
                visited.append(y)
                queue.append(y)
                lst[y] = lst[x] + 1

    return lst

N = int(input())
A, B = map(int, input().split())
M = int(input())

dic = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    dic[a] += [b]
    dic[b] += [a] 

lst_ans = dfs(dic, A, N)

answer = lst_ans[B]

if answer != 0:
    print(answer)
else:
    print(-1)
