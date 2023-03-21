from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1]
dy = [1, 0]

visited = [[0 for _ in range(N)] for _ in range(N)]

def dfs(x, y):
    queue = deque()
    queue.append([x, y])
    
    visited[x][y] = 1
    
    while queue:
        x, y = queue.pop()
        for i in range(2):
            nx = x + dx[i] * arr[x][y]
            ny = y + dy[i] * arr[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

dfs(0, 0)

if visited[N - 1][N - 1] == 1:
    print('HaruHaru')
else:
    print('Hing')