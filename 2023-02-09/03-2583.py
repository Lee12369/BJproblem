from collections import deque
import sys
input = sys.stdin.readline

def dfs(arr, x, y, visited = []):
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
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    square += 1    
    return square

M, N, K = map(int, input().split())
arr = [[1 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[M - i - 1][j] = 0

visited = [[0 for _ in range(N)] for _ in range(M)]
cnt = 0
square_lst = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            square = dfs(arr, i, j, visited)
            square_lst.append(square)
            cnt += 1

square_lst.sort()

print(cnt)
for x in square_lst:
    print(x, end=' ')