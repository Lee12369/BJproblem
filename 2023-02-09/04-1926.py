from collections import deque
def dfs(arr, x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    square = 1
    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    square += 1
    return square

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

max_square = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            square = dfs(arr, i, j, visited)
            max_square = max(max_square, square)
            cnt += 1

print(cnt)
print(max_square)