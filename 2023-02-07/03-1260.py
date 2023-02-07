from collections import defaultdict, deque
N, M, V = map(int, input().split())

dic = defaultdict(deque)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a] += [b]
    dic[b] += [a]

for key, val in dic.items():
    dic[key] = sorted(val)

def dfs(dic, start, visited = []):
    visited.append(start)
    for x in dic[start]:
        if x not in visited:
            dfs(dic, x, visited)

    return visited

def bfs(dic, start, visited=[]):
    queue = deque()
    queue.append(start)
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for x in dic[n]:
                queue.append(x)

    return visited

dfs_ans = dfs(dic, V)
bfs_ans = bfs(dic, V)

for x in dfs_ans:
    print(x, end=' ')
print()    
for y in bfs_ans:
    print(y, end=' ')