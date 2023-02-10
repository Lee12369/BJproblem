from collections import deque
def bfs(arr, x, y, visited = []):
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
            if 0 <= nx < M + 1 and 0 <= ny < N + 1 and arr[nx][ny] == 1:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    queue.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1

def get_idx(arr, length):
    for i in range(length):
        if arr[i][0] == 1:
            arr[i][0] = 0
        elif arr[i][0] == 2:
            arr[i][0] = M
        elif arr[i][0] == 3:
            arr[i][0] = arr[i][1]
            arr[i][1] = 0
        elif arr[i][0] == 4:
            arr[i][0] = arr[i][1]
            arr[i][1] = N

N, M = map(int, input().split()) # 가로, 세로
K = int(input())
store = [list(map(int, input().split())) for _ in range(K)]
dong_geun = [list(map(int, input().split()))]

arr = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
for i in range(M + 1):
    arr[i][0] = 1
    arr[i][N] = 1
for j in range(N + 1):
    arr[0][j] = 1
    arr[M][j] = 1

get_idx(store, K)
get_idx(dong_geun, 1)

x = dong_geun[0][0]
y = dong_geun[0][1]
arr[M - x][N - y] = -1

bfs(arr, x, y)

sum_dist = 0
for lst in store:
    distance = arr[lst[0]][lst[1]] -1
    if distance < 0:
        distance = N + M
    
    sum_dist += distance 

print(sum_dist)

