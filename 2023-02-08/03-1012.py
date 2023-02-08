from collections import deque
def bfs(arr, x, y, visited=[]):
    queue = deque()
    queue.append([x, y])
    visited.append([x, y])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    queue.append([nx, ny])

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    
    visited = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and [i, j] not in visited:
                bfs(arr, i, j, visited)
                cnt += 1
    
    print(cnt)