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

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    queue.append([nx, ny])

    return len(visited)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = []
house = []
pre = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and [i, j] not in visited:
            house_cnt = bfs(arr, i, j, visited) - pre
            house.append(house_cnt)
            pre += house_cnt

house.sort()
villa_cnt = len(house)

print(villa_cnt)
for x in house:
    print(x)
