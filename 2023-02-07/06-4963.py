from collections import deque
def bfs(x, y):
    visited.append([x, y])
    queue = deque([x, y])

    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    queue.append(nx)
                    queue.append(ny)
                    
while True:    
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    
    cnt = 0
    visited = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and [i, j] not in visited:
                bfs(i, j)
                cnt += 1
    print(cnt)