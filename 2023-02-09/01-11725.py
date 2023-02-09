import sys
from collections import defaultdict, deque
def bfs(dic, start, visited):
    dic_ans = {}
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        x = queue.popleft()
        for y in dic[x]:
            if visited[y] == 0:
                visited[y] = 1
                queue.append(y)
                dic_ans[y] = x
    
    return dic_ans 

N = int(input())

dic = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] += [b]
    dic[b] += [a]

visited = [0 for i in range(N + 1)]

lst_answer = bfs(dic, 1, visited)

for i in range(2, N + 1):
    print(lst_answer[i]) 
    
