R, C = map(int, input().split())

room = [['*' for _ in range(C)] for _ in range(R)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    room[x][y] = 'x'

robot_x, robot_y = map(int, input().split())
room[robot_x][robot_y] = 1
moves = list(map(int, input().split()))

# 위, 아래, 왼쪽, 오른쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

while True:
    for move in moves:
        while True:
            nx = robot_x + dx[move]
            ny = robot_y + dy[move]
            if 0 <= nx < R and 0 <= ny < C and room[nx][ny] == '*':
                room[nx][ny] = 1
                robot_x = nx
                robot_y = ny    
            else:
                break    
    
    check = 0
    for i in range(5):
        nx = robot_x + dx[i]
        ny = robot_y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and room[nx][ny] == '*':
            check = 1
            break
    
    if check == 0:
        break

print(robot_x, robot_y)  
