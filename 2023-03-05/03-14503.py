import sys
input = sys.stdin.readline

N, M = map(int, input().split())
robot_x, robot_y, look = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    if arr[robot_x][robot_y] == 0:
        arr[robot_x][robot_y] = 2
        cnt += 1
    
    check = False
    for i in range(look, look + 4):
        if i > 3:
            i -= 4
        nx = robot_x + dx[i]
        ny = robot_y + dy[i]
        if arr[nx][ny] == 0:
            check = True
    
    if check == True:
        look -= 1
        if look < 0:
            look += 4
        nx = robot_x + dx[look]
        ny = robot_y + dy[look]
        if arr[nx][ny] == 0:
            robot_x = nx
            robot_y = ny 
    else:
        back = look - 2
        if back < 0:
            back += 4
        
        nx = robot_x + dx[back]
        ny = robot_y + dy[back]
        if arr[nx][ny] == 0 or arr[nx][ny] == 2:
            robot_x = nx
            robot_y = ny
        else:
            break

print(cnt)
