from collections import deque
import sys
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs():
    cheese_dis = 0
    queue = deque()
    queue.append([0, 0])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1

    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[x][y] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if arr[nx][ny] == 1:
                        temp[nx][ny] = 0
                        cheese_dis += 1
                    elif arr[nx][ny] == 0:
                        queue.append([nx, ny])
                        
    return cheese_dis

cnt = 0
for i in range(N):
    cnt += arr[i].count(1)
pre_cnt = int(cnt)

time = 0
while True:    
    temp = arr.copy()
    cheese_dis = dfs()

    if cnt == 0:
        print(time, pre_cnt)
        break
    
    time += 1
    pre_cnt = int(cnt)
    cnt = cnt - cheese_dis
    arr = temp.copy()