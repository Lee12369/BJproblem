from collections import deque
def bfs(arr, x, y, visited = []):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1

T = int(input())
for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    arr = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and visited[i][j] == 0:
                bfs(arr, start_x, start_y, visited)
    
    answer = arr[end_x][end_y]

    print(answer)