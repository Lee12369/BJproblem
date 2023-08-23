import sys
input = sys.stdin.readline

class shark:
    def __init__(self, speed, direction, size):
        self.speed = speed
        self.direction = direction
        self.size = size

def get_shark(board, human):
    for i in range(R):
        target = board[i][human]
        if isinstance(target, shark):
            shark_size = target.size
            board[i][human] = 0
            return shark_size
    return 0

def move_sharks(board):
    new_board = [[0 for _ in range(C)] for _ in range(R)]
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if isinstance(board[i][j], shark):
                target_shark = board[i][j]
                direct = target_shark.direction

                # 원래 자리로 돌아오는 수를 나누어 나머지만으로 이동하면 시간을 절약할 수 있다.
                if dx[direct] == 0:
                    # 이동하는 길이, 처음에서 끝으로 가는데 필요한 거리, 처음에 한 칸을 차지하고 있기 때문에 끝에 도착하는데는 전체 길이에서 1을 빼야한다.
                    move_cnt = target_shark.speed % ((C - 1) * 2)
                elif dy[direct] == 0:
                    move_cnt = target_shark.speed % ((R - 1) * 2)

                move_i, move_j, target_shark = move_shark(i, j, move_cnt, target_shark)

                # 새로운 보드에 이미 상어가 있고 크기가 크다면 target상어는 잡아먹힌다.
                if isinstance(new_board[move_i][move_j], shark) and target_shark.size < new_board[move_i][move_j].size:
                    continue    
                new_board[move_i][move_j] = target_shark

    return new_board

def move_shark(i, j, move_cnt, target_shark):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]

    change_direct = {
        1:2,
        2:1,
        3:4,
        4:3
    }

    move_i = int(i)
    move_j = int(j)
    direct = target_shark.direction   
    # up
    if dx[direct] == -1:
        if 0 <= move_cnt <= i:
            move_i = i - move_cnt
        elif i < move_cnt <= i + R - 1:
            move_i = move_cnt - i
            target_shark.direction = change_direct[direct]
        elif i + R - 1 < move_cnt:
            move_i = 2 * (R - 1) - (move_cnt - i)

    # down 
    elif dx[direct] == 1:
        if 0 <= move_cnt <= R - 1 - i:
            move_i = i + move_cnt
        
        elif R - 1 - i < move_cnt <= 2 * (R - 1) - i:
            move_i = 2 * (R - 1) - (move_cnt + i)
            target_shark.direction = change_direct[direct]

        elif  2 * (R - 1) - i < move_cnt:
            move_i = move_cnt + i - 2 * (R - 1)

    # left
    elif dy[direct] == -1:
        if 0 <= move_cnt <= j:
            move_j = j - move_cnt
        elif j < move_cnt <= j + C - 1:
            move_j = move_cnt - j
            target_shark.direction = change_direct[direct]
        elif j + C - 1 < move_cnt:
            move_j = 2 * (C - 1) - (move_cnt - j)
    
    # right
    elif dy[direct] == 1:
        if move_cnt <= C - 1 - j:
            move_j = j + move_cnt
        
        elif C - 1 - j < move_cnt <= 2 * (C - 1) - j:
            move_j = 2 * (C - 1) - (move_cnt + j) 
            target_shark.direction = change_direct[direct]

        elif  2 * (C - 1) - j < move_cnt:
            move_j = move_cnt + j - 2 * (C - 1)

    # 시간 초과 발생
    # for _ in range(move_cnt):
    #     direct = target_shark.direction    
    #     nx = i + dx[direct]
    #     ny = j + dy[direct]
    #     if not (0 <= nx < R and 0 <= ny < C):
    #         direct = change_direct[direct]
    #         target_shark.direction = direct 
    #         nx = i + dx[direct]
    #         ny = j + dy[direct]
        
    #     i = int(nx)
    #     j = int(ny)

    return move_i, move_j, target_shark

R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c] = shark(s, d, z)


# R, C, M = 4,6,8
# board = [[0 for _ in range(C)] for _ in range(R)]
# inputs = [(4,1,3,3,8),(1,3,5,2,9),(2,4,8,4,1),(4,5,0,1,4),(3,3,1,2,7),(1,5,8,4,3),(3,6,2,1,2),(2,2,2,3,5)]
# for tpl in inputs:
#     r, c, s, d, z = tpl
#     r -= 1
#     c -= 1
#     board[r][c] = shark(s, d, z)


ans = 0
for j in range(C):
    ans += get_shark(board, j)
    board = move_sharks(board)

print(ans)
