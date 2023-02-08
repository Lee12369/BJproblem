from collections import deque
def bfs(lst = [], x = 0, visited = []):
    queue = deque()
    queue.append(x)
    visited.append(x)

    while queue:
        x = queue.popleft()
        dx = [-1, 1, x]

        for i in range(3):
            nx = x + dx[i]

            if 0 <= nx < 100001 and lst[nx] == 0:
                if nx not in visited:
                    queue.append(nx)
                    visited.append(nx)
                    lst[nx] = lst[x] + 1
        
        if lst[K] != 0:
            return lst[K]

N, K = map(int, input().split())

lst = [0 for _ in range(100001)]

answer = bfs(lst, N)

print(answer)