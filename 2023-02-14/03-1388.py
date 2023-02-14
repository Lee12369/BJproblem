from collections import deque
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dy = [1, -1]
dx = [1, -1]

def check_row(x, y, visited):
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '-':
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

def check_column(x, y, visited):
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '|':
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            visited[i][j] = True
            if arr[i][j] == '-':
                check_row(i, j, visited)
                cnt += 1         
            elif arr[i][j] == '|':
                check_column(i, j, visited)
                cnt += 1

print(cnt)