from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(5 * N + 1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, visited):
    queue = deque()
    queue.append([x, y])

    visited[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 * N + 1 and 0 <= ny < 5 * M + 1 and visited[nx][ny] == 0 and arr[nx][ny] != '#':
                visited[nx][ny] = 1
                queue.append([nx, ny])
                if arr[nx][ny] == '*':
                    cnt += 1

    return cnt

visited = [[0 for _ in range(5 * M + 1)] for _ in range(5 * N + 1)]

blind_type = [0, 0, 0, 0, 0]

for i in range(5 * N + 1):
    for j in range(5 * M + 1):
        if arr[i][j] != '#' and visited[i][j] == 0:
            cnt = dfs(i, j, visited)
            blind_type[cnt // 4] += 1

for x in blind_type:
    print(x, end=' ')

            