from collections import deque
def bfs(arr, x, y, M, visited = []):
    queue = deque()
    queue.append([x, y])
    visited[x][y] == 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > M:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
for M in range(101):
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] > M:
                bfs(arr, i, j, M, visited)
                cnt += 1
    max_cnt = max(max_cnt, cnt)        

print(max_cnt)