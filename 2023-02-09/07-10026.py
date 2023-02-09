from collections import deque
def bfs(arr, x, y, visited, args1, args2 = ''):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (arr[nx][ny] == args1 or arr[nx][ny] == args2):
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])


N = int(input())
arr = [list(input()) for _ in range(N)]
case1_lst = ['R', 'G', 'B']

# 적록색약이 아닌 사람.
case1_cnt = 0
for x in case1_lst:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == x and visited[i][j] == 0:
                bfs(arr, i, j, visited, x)
                case1_cnt += 1

# 적록색약인 사람.
case2_cnt = 0
case2_lst = [['R','G'],['B','B']]
for x, y in case2_lst:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (arr[i][j] == x or arr[i][j] == y) and visited[i][j] == 0:
                bfs(arr, i, j, visited, x, y)
                case2_cnt += 1

print(case1_cnt)                
print(case2_cnt)