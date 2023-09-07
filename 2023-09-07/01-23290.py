# 물고기의 방향이 같다면 이동 위치 역시 동일하기에 8개의 방향을 기준으로 물고기의 숫자를 파악하고 물고기가 이동할 방향에 물고기의 수를 더해주는 것으로 계산 횟수를 줄이는 방식으로 진행
from collections import defaultdict
import sys
input = sys.stdin.readline

class Shark:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

# 물고기 이동.
def move_fish(board, new_board, direct, i, j):
    for k in range(8):
        move_direct = direct - k
        if move_direct < 0:
            move_direct += 8
        nx = i + dx[move_direct]
        ny = j + dy[move_direct]
        # 범위 내에서 냄새가 없고 상어가 없는 곳만 이동 가능
        if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 and not (nx == shark.row and ny == shark.column):
            new_board[nx][ny][move_direct] += board[i][j][direct]
            return
    # 이동이 불가능하면 원래 위치와 방향에 물고기 추가 
    new_board[i][j][direct] += board[i][j][direct]
    return

def move_fishes(board):
    new_board = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            fishes = board[i][j]
            for direct in fishes.keys():
                move_fish(board, new_board, direct, i, j)
    return new_board

# 상어의 이동 경로를 추적해서 먹은 물고기의 개수와 방향을 저장
def find_move_shark_path(board, x, y, direct, cnt):
    board_cnt = [[sum(list(board[i][j].values())) for j in range(4)] for i in range(4)]
    if len(direct) == 3:
        directions.append([cnt] + direct)
        return
    
    for i in range(4):
        nx = x + shark_dx[i]
        ny = y + shark_dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            save = board[nx][ny]
            board[nx][ny] = defaultdict(int)
            find_move_shark_path(board, nx, ny, direct + [i], cnt + board_cnt[nx][ny])
            board[nx][ny] = save

# 상어 이동.
def move_shark(board, direction):
    x, y = shark.row, shark.column
    for i in range(3):
        direct = direction[i]
        x += shark_dx[direct]
        y += shark_dy[direct]
        fish_cnt = sum(list(board[x][y].values()))
        # 물고기가 있다면 냄새를 3으로 한다. 3으로 한 이유는 과정 마지막에 냄새를 1씩 빼줄 예정이라 이를 고려하여 2가 아닌 3으로 하였다.
        if fish_cnt > 0:
            smell[x][y] = 3
        board[x][y] = defaultdict(int)

    shark.row = int(x)
    shark.column = int(y)
    return board

# 물고기 복사
def copy_magic(board, copy_board):
    for i in range(4):
        for j in range(4):
            for k in range(8):
                board[i][j][k] += copy_board[i][j][k]

# 냄새를 1씩 감소
def down_smell(smell):
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

# 전체 물고기 합.
def sum_board(board):
    total = 0
    for i in range(4):
        for j in range(4):
            total += sum(board[i][j].values())
    return total

# 인덱스 처리를 간편하게 하기 위해 시작을 0으로 하여 진행
shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# board = [[defaultdict(int) for _ in range(4)] for _ in range(4)]

# M, S = 5, 26
# inputs = [[4, 3, 5], [1, 3,5 ], [2, 4,2 ],[2, 1, 6],[3, 4, 4]]
# for lst in inputs:
#     fx, fy, d = lst
#     fx -= 1
#     fy -= 1
#     d -= 1
#     board[fx][fy][d] += 1

# smell = [[0 for _ in range(4)] for _ in range(4)]
# sx, sy = 4, 2
# sx -= 1
# sy -= 1
# shark = Shark(sx, sy)


# board = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
# M, S = 10, 25
# inputs = [[1,1,1], [1,1,2], [1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[2,1,1],[2,1,1]]
# for lst in inputs:
#     fx, fy, d = lst
#     fx -= 1
#     fy -= 1
#     d -= 1
#     board[fx][fy][d] += 1

# smell = [[0 for _ in range(4)] for _ in range(4)]
# sx, sy = 2,1
# sx -= 1
# sy -= 1
# shark = Shark(sx, sy)

board = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
M, S = map(int, input().split())
for _ in range(M):
    fx, fy, d = map(int, input().split())
    # 인덱스 조정
    fx -= 1
    fy -= 1
    d -= 1
    board[fx][fy][d] += 1

smell = [[0 for _ in range(4)] for _ in range(4)]
sx, sy = map(int, input().split())
# 인덱스 조정
sx -= 1
sy -= 1
shark = Shark(sx, sy)

for _ in range(S):
    copy_board = [row[::] for row in board]
    board = move_fishes(board)

    directions = []
    find_move_shark_path(board, shark.row, shark.column, [], 0)
    directions.sort(key=lambda x : -x[0])
    direction = directions[0][1:]
    
    board = move_shark(board, direction)

    copy_magic(board, copy_board)
    down_smell(smell)   

board_cnt = [[sum(list(board[i][j].values())) for j in range(4)] for i in range(4)]

ans = sum_board(board)

print(ans)