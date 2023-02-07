from collections import defaultdict

def dfs(dic, start, visited=[]):
    visited.append(start)
    for x in dic[start]:
        if x not in visited:
            dfs(dic, x, visited)
    return len(visited) - 1

N = int(input())
M = int(input())

dic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a] += [b]
    dic[b] += [a]

answer = dfs(dic, 1)

print(answer)

