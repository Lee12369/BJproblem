from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_xy = []
empty_xy = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty_xy.append((i, j))
        if arr[i][j] == 2:
            virus_xy.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp_arr[nx][ny] == 0:
                temp_arr[nx][ny] = 2
                queue.append((nx, ny))
                cnt += 1
    return cnt

max_safety_zone = 0
for lst in combinations(empty_xy, 3):
    temp_arr = [[arr[i][j] for j in range(M)] for i in range(N)]
    for tpl in lst:
        empty_x, empty_y = tpl
        temp_arr[empty_x][empty_y] = 1
    
    # 0 인 공간을 1 로 3개 바꿨기 때문
    safety_zone = len(empty_xy) - 3
    for x in range(N):
        for y in range(M):
            if temp_arr[x][y] == 2:
                safety_zone -= dfs(x, y)

    max_safety_zone = max(max_safety_zone, safety_zone)

print(max_safety_zone)    
