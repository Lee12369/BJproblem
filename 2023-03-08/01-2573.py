#pypy3로 통과, python3로는 시간 초과
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] > 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])

time = 0
while True:
    # 빙산 주위의 0의 개수를 저장.
    cnt_0 = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        cnt_0[i][j] += 1

    # 빙산의 크기를 줄인다.
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                arr[i][j] -= cnt_0[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0
    time += 1

    # 빙산의 개수를 dfs로 확인.
    cnt = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0:
                dfs(i, j, visited)
                cnt += 1
    
    if cnt > 1:
        print(time)
        break
    
    elif cnt == 0:
        print(0)
        break
        