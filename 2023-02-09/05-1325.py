from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dfs(data, start, visited = []):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    cnt = 0
    while queue:
        x = queue.pop()
        for y in data[x]:
            if visited[y] == 0:
                visited[y] = 1
                queue.append(y)
                cnt += 1

    return start, cnt

N, M = map(int, input().split())

dic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[b] += [a]

max_cnt = 0
start_lst = []
visited = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    start, cnt = dfs(dic, i)
    if cnt > max_cnt:
        max_cnt = cnt
        start_lst = [start]
    elif cnt == max_cnt:
        start_lst.append(start)

for x in start_lst:
    print(x, end=' ')