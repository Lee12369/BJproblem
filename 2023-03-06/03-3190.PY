from collections import deque
import sys
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j = map(int,input().split())
    arr[i - 1][j - 1] = "apple"

move = []
L = int(input())
for _ in range(L):
    sec, LD = input().split()
    sec = int(sec)
    move.append((sec, LD))

# 마지막으로 방향 전환 후 벽에 부딪치게 만들기 위한 용도
move.append((100, ''))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

head_x = 0
head_y = 0
queue = deque()
queue.append([head_x, head_y])
time = 0
look_idx = 0
for tpl in move:
    sec, change = tpl
    next_head_x = head_x + dx[look_idx]
    next_head_y = head_y + dy[look_idx]
    while time < sec and 0 <= next_head_x < N and 0 <= next_head_y < N and [next_head_x, next_head_y] not in queue: 
        head_x += dx[look_idx]
        head_y += dy[look_idx]
        
        if arr[head_x][head_y] != 'apple':
            queue.popleft()
        else:
            arr[head_x][head_y] = 0
        
        queue.append([head_x, head_y])
        time += 1
        next_head_x = head_x + dx[look_idx]
        next_head_y = head_y + dy[look_idx]
    
    if time == sec:
        if change == 'L':
            look_idx -= 1
        elif change == 'D':
            look_idx += 1
        
        if look_idx < 0:
            look_idx += 4
        elif look_idx > 3:
            look_idx -= 4
        next_head_x = head_x + dx[look_idx]
        next_head_y = head_y + dy[look_idx]

    if next_head_x < 0 or next_head_x >= N or next_head_y < 0 or next_head_y >= N or [next_head_x, next_head_y] in queue:
        time += 1
        break

print(time)