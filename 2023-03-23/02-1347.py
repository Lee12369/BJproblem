_ = int(input())
move = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

look = 0

curr_x = 0
curr_y = 0
max_x = 0
min_x = 0
max_y = 0
min_y = 0
visited = [(0, 0)]
for x in move:
    if x == 'F':
        curr_x += dx[look]
        curr_y += dy[look]
        min_x = min(min_x, curr_x)
        max_x = max(max_x, curr_x)
        min_y = min(min_y, curr_y)
        max_y = max(max_y, curr_y)
        
        visited.append((curr_x, curr_y))

    elif x == 'R':
        look += 1
        if look > 3:
            look -= 4
    
    elif x == 'L':
        look -= 1
        if look < 0:
            look += 4

N = max_x - min_x + 1
M = max_y - min_y + 1
x_plus = -min_x
y_plus = -min_y

maze = [['#' for _ in range(M)] for _ in range(N)]
for tpl in visited:
    x, y = tpl
    maze[x + x_plus][y + y_plus] = '.'

for i in range(N):
    for j in range(M):
        print(maze[i][j], end='')
    print()
