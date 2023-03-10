from itertools import combinations
from collections import deque
import sys, copy
input = sys.stdin.readline

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0]
dy = [-1, 0, 1]

def shoot(wall, y, arr_temp):
    queue = deque()
    queue.append([wall, y])
    
    start_x = wall
    start_y = int(y)
    visited = [[0 for _ in range(M)] for _ in range(wall + 1)]
    visited[wall][y] = 1

    while queue:
        x, y = queue.popleft()
        dist = abs(x - start_x) + abs(y - start_y)
        if dist == D:
            return 0
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < wall and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if arr_temp[nx][ny] == 0:
                    queue.append([nx, ny])
                
                elif arr_temp[nx][ny] == 1:
                    return (nx, ny)
    return 0

max_cnt = 0
nums = [i for i in range(M)]
for tpl in combinations(nums, 3):
    cnt = 0
    wall = int(N)
    arr_temp = copy.deepcopy(arr)

    while wall > 0:
        # 목표 확인
        lst_temp = []
        for y in tpl:
            attack = shoot(wall, y, arr_temp)
            if attack == 0:
                continue
            lst_temp.append(attack)
        attack_points = list(set(lst_temp))

        # 목표 제거
        len_attack_points = len(attack_points)
        for i in range(len_attack_points):
            a, b = attack_points[i]
            arr_temp[a][b] = 0
            cnt += 1
        
        # 적 이동.(실제 적이 아래로 내려간 경우 == 성벽이 위로 올라간 경우)
        wall -= 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)