from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, N, M, visited = []):
    queue = deque()
    queue.append((0, 0))
    visited.append([0, 0])
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
  
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    queue.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1

    return arr[N -1][M - 1] 

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip('\n'))) for _ in range(N)]

answer = bfs(arr, N, M)

print(answer)
