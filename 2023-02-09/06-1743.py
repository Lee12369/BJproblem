from collections import deque
def dfs(arr, x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    cnt = 1
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    cnt += 1
    return cnt

N, M, K = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1

max_size = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            size = dfs(arr, i, j, visited)
            max_size = max(max_size, size)

print(max_size)