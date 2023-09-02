from collections import deque
import sys
input = sys.stdin.readline

class time:
    def __init__(self, row_time, column_time) -> None:
        self.info = {
            'row' : row_time,
            'column' : column_time
        }

# 통나무가 가로로 움직일 경우, 또는 회전해서 가로가 될 경우.
def row_move(nx, ny, x, y, n_shape, shape, check_dx, check_dy):
    if 0 <= nx < N and 1 <= ny < N - 1:
        # 조건 별 범위의 공간이 전부 비어 있어야지만 이동이 가능하다.
        for i in range(len(check_dx)):
            check_x = nx + check_dx[i]
            check_y = ny + check_dy[i]
            if board[check_x][check_y] == '1':
                return
        # 이동이 가능한지 확인을 마친 후 이동하는 위치와 그 이전 위치의 시간을 비교해서 더 적게 걸린다면 값을 저장하고 queue에 추가한다.
        if visited[nx][ny].info[n_shape] > visited[x][y].info[shape] + 1:
            visited[nx][ny].info[n_shape] = visited[x][y].info[shape] + 1
            queue.append((nx, ny, n_shape))

# 통나무가 세로로 움직일 경우, 또는 회전해서 세로가 될 경우.
def column_move(nx, ny, x, y, n_shape, shape, check_dx, check_dy):
    if 1 <= nx < N - 1 and 0 <= ny < N:
        for i in range(len(check_dx)):
            check_x = nx + check_dx[i]
            check_y = ny + check_dy[i]
            if board[check_x][check_y] == '1':
                return
        if visited[nx][ny].info[n_shape] > visited[x][y].info[shape] + 1:
            visited[nx][ny].info[n_shape] = visited[x][y].info[shape] + 1
            queue.append((nx, ny, n_shape))

# N = 5
# INF = int(1e9)
# board = [['B', '0','0','1','1'], ['B','0','0','0','0'],['B','0','0','0','0'], ['1','1','0','0','0'],['E','E','E','0','0']]
# visited = [[time(INF, INF) for _ in range(N)] for _ in range(N)]

N = int(input())
INF = int(1e9)
board = [list(input().rstrip()) for _ in range(N)]
visited = [[time(INF, INF) for _ in range(N)] for _ in range(N)]

# B 3개 E 3개를 얻는다. 이 중에서 1번 인덱스가 중앙에 위치한 나무의 중심이 된다.
Bs = []
Es = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            Bs.append((i, j))
        elif board[i][j] == 'E':
            Es.append((i, j))

# 나무가 가로로 되어 있는지 세로로 되어있는지 확인하는 작업.
tree_center = Bs[1]
if Bs[0][0] == Bs[1][0] == Bs[2][0]:
    tree_shape = 'row'
else:
    tree_shape = 'column'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y = tree_center
queue = deque()
queue.append((x, y, tree_shape))
visited[x][y].info[tree_shape] = 0
while queue:
    x, y, shape = queue.popleft()
    # up, down, left, right
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if shape == 'row':
            check_dx = [0, 0, 0]
            check_dy = [1, -1, 0]
            row_move(nx, ny, x, y, shape, shape, check_dx, check_dy)

        elif shape == 'column':
            check_dx = [1, -1, 0]
            check_dy = [0, 0, 0]
            column_move(nx, ny, x, y, shape, shape, check_dx, check_dy)
    
    # turn
    # 턴의 경우 중심을 기준으로 3 * 3이 전부 비어 있어야 회전이 가능하다.
    check_dx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    check_dy = [0, 1, -1, 0, 1, -1, 0, 1, -1]  
    if shape == 'row':
        turn_shape = 'column'
        column_move(x, y, x, y, turn_shape, shape, check_dx, check_dy)

    else:
        turn_shape = 'row'
        row_move(x, y, x, y, turn_shape, shape, check_dx, check_dy)

# 목표 지점의 중심의 좌표와 모양
target_center = Es[1] 
if Es[0][0] == Es[1][0] == Es[2][0]:
    target_shape = 'row'
else:
    target_shape = 'column'

target_x, target_y = target_center
ans = visited[target_x][target_y].info[target_shape]
# 목표 지점에 도달할 수 없으면 0을 출력
if ans == INF:
    ans = 0

print(ans)