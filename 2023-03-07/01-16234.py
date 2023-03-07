from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, check, visited):
    queue = deque()
    queue.append([x, y])

    visited[x][y] = True
    sum = arr[x][y]
    union = [(x, y)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    sum += arr[nx][ny]
                    union.append((nx, ny))
                    check = 1
    
    population = sum // len(union)
    for tpl in union:
        x, y = tpl
        arr[x][y] = population
    return check

day = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    check = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                check = dfs(i, j, check, visited)

    if check == 0:
        break

    day += 1

print(day)