import sys
input = sys.stdin.readline

# 상어의 클래스를 만들어 priority에는 배열을 집어넣어 1행에 위를 보고 있을 때의 priority를 넣는 식으로 방향 전부에 대한 priority를 저장한다. look은 현재 보는 방향을 의미한다. 
class Shark:
    def __init__(self, number, priority, look) -> None:
        self.number = number
        self.priority = priority
        self.look = look

# 빈 공간이 있는지 찾는다.
# new_board에 만들어 기록하는 것은 기존의 빈 공간인지 파악하기 위함.
def empty_move(num, x, y, new_board):
    shark = sharks[num]
    look = shark.look
    priority = shark.priority[look]
    for idx in priority:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if new_board[nx][ny] == 0 or (new_board[nx][ny] > 0 and board[nx][ny] == 0 and num < new_board[nx][ny]):
                new_board[nx][ny] = num
                sharks[num].look = idx 
            new_board[x][y] = 0          
            return True
    return False

# 빈 공간이 없다면 자신이 냄새를 남긴 곳으로 돌아간다.
def comeback_move(num, x, y, new_board):
    shark = sharks[num]
    look = shark.look
    priority = shark.priority[look]
    for idx in priority:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == num:
            new_board[nx][ny] = num
            new_board[x][y] = 0
            visited[nx][ny] = num
            smell_time[nx][ny] = k
            sharks[num].look = idx       
            return True
    return False

# 상어가 있는 자리를 제외하고는 냄새의 시간을 줄인다. 시간이 0이되면 누구의 냄새인지를 기록하는 visited에서도 0으로 만들어준다.
def smell_down():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and smell_time[i][j] > 0 :
                smell_time[i][j] -= 1
                if smell_time[i][j] == 0:
                    visited[i][j] = 0 



def move_sharks(board):
    new_board = [row[::] for row in board]
    for i in range(N):
        for j in range(N):
            num = board[i][j]
            if num > 0:
                if empty_move(num, i, j, new_board):
                    continue
                comeback_move(num, i, j, new_board)
    return new_board

# 상어가 몇 마리 남았는지 확인하고 1마리 남았다면 True를 아니면 False를 반환한다.
def check_sharks(board):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                cnt += 1

    if cnt == 1:
        return True
    else:
        return False

# 현재 보드를 기준으로 상어가 위치한 곳에 방문표시가 없다면 방문기록이랑, 냄새를 업데이트한다.
def update_visited_smell_time(): 
    for i in range(N):
        for j in range(N):
                num = board[i][j]
                if num > 0 and visited[i][j] == 0:
                    visited[i][j] = num
                    smell_time[i][j] = k

dx = {
    1 : -1,
    2 : 1,
    3 : 0,
    4 : 0
}

dy = {
    1 : 0,
    2 : 0,
    3 : -1,
    4 : 1 
}

# N, M, k = 5, 4, 4
# board = [[0,0,0,0,3],[0,2,0,0,0],[1,0,0,0,4],[0,0,0,0,0],[0,0,0,0,0]]
# looks = [4,4,3,1]
# sharks = [0]
# directions = [[2,3,1,4],[4,1,2,3],[3,4,2,1],[4,3,1,2],[2,4,3,1],[2,1,3,4],[3,4,1,2],[4,1,2,3],[4,3,2,1],[1,4,3,2],[1,3,2,4],[3,2,1,4],[3,4,1,2],[3,2,4,1],[1,4,2,3],[1,4,2,3]]
# idx = 0
# for i in range(1, M + 1):
#     priority = [0]
#     for _ in range(4):
#         priority.append(directions[idx])
#         idx += 1
#     sharks.append(Shark(i, priority, looks[i - 1]))

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
looks = list(map(int, input().split()))
sharks = [0]
for i in range(1, M + 1):
    priority = [0]
    for _ in range(4):
        priority.append(list(map(int, input().split())))
    sharks.append(Shark(i, priority, looks[i - 1]))

visited = [row[:] for row in board]
smell_time = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            smell_time[i][j] = k

time = 1
while time < 1001:
    board = move_sharks(board)
    update_visited_smell_time()
    smell_down()
    if check_sharks(board):
        break
    time += 1

if time > 1000:
    time = -1

print(time)