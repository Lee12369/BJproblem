import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# [위, 동, 서, 북, 남, 아래]
dice = [0, 0, 0, 0, 0, 0]

for move in moves:
    nx = x + dx[move]
    ny = y + dy[move]
    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
    else:
        continue
    
    if move == 1:
        dice[1], dice[5], dice[2], dice[0] = dice[5], dice[2], dice[0], dice[1]  
    elif move == 2:
        dice[2], dice[5], dice[1], dice[0] = dice[5], dice[1], dice[0], dice[2]
    elif move == 3:
        dice[3], dice[5], dice[4], dice[0] = dice[5], dice[4], dice[0], dice[3]
    elif move == 4:
        dice[4], dice[5], dice[3], dice[0] = dice[5], dice[3], dice[0], dice[4]
    
    if arr[x][y] == 0:
        arr[x][y] = dice[5]
    else:
        dice[5] = arr[x][y]
        arr[x][y] = 0
    
    print(dice[0])