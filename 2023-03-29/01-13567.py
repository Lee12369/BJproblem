import sys
input = sys.stdin.readline

M, N = map(int, input().split())

x = 0
y = 0

# 동, 남, 서, 북 순서. 시작은 동쪽을 바라보기에 look = 0
look = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

check = 1
robot_moves = []
for _ in range(N):
    command, num = input().split()
    robot_moves.append((command, int(num)))

for tpl in robot_moves:
    command, num = tpl
    if command == 'MOVE':
        nx = x + dx[look] * num
        ny = y + dy[look] * num
        if 0 <= nx <= M and 0 <= ny <= M:
            x = int(nx)
            y = int(ny)
            
        else:
            check = 0
            break
            
    elif command == 'TURN':
        if num == 0:
            look -= 1
            if look < 0:
                look += 4 

        elif num == 1:
            look += 1
            if look > 3:
                look -= 4
    
if check == 1:
    print(x, y)
else:
    print(-1)                   