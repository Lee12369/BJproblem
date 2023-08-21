import sys, copy
input = sys.stdin.readline

def dust_spread(board):
    save_board = copy.deepcopy(board)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(N):
        for j in range(M):
            if board[i][j] <= 0:
                continue

            split_dust = board[i][j] // 5
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] >= 0:
                    save_board[nx][ny] += split_dust
                    save_board[i][j] -= split_dust
    
    return save_board

def dust_rotate(board, up_cleaner, down_cleaner):
    save_board = copy.deepcopy(board)

    up_cleaner_rotate(up_cleaner, board, save_board)
    down_cleaner_rotate(down_cleaner, board, save_board)

    return save_board

def info_cleaner(board):
    for i in range(N):
        if board[i][0] == -1:
            up_cleaner = (i, 0)
            down_cleaner = (i + 1, 0)
            return up_cleaner, down_cleaner

def up_cleaner_rotate(up_cleaner, board, save_board):
    x, _ = up_cleaner
    ## 범위를 4등분으로 나눠서 진행.
    for i in range(x + 1):
        for j in range(M):
            # up
            if i == 0 and j > 0:
                save_board[i][j - 1] = board[i][j]
            # down
            elif i == x and j < M - 1:
                # 공기 청정기 위치 일 때, 바로 옆의 먼지는 0이 된다.
                if j == 0:
                    save_board[i][j + 1] = 0
                    continue
                save_board[i][j + 1] = board[i][j]
            # left
            elif j == 0 and i < x - 1:
                save_board[i + 1][j] = board[i][j]
            # right
            elif j == M - 1 and i > 0:
                save_board[i - 1][j] = board[i][j]

    return save_board

def down_cleaner_rotate(down_cleaner, board, save_board):
    x, _ = down_cleaner
    ## 범위를 4등분으로 나눠서 진행.
    for i in range(x, N):
        for j in range(M):
            # up
            if i == x and j < M - 1:
                # 공기 청정기 위치 일 때, 바로 옆의 먼지는 0이 된다.
                if j == 0:
                    save_board[i][j + 1] = 0
                    continue
                save_board[i][j + 1] = board[i][j]
            # down
            elif i == N - 1 and j > 0:
                save_board[i][j - 1] = board[i][j]
            # left
            elif j == 0 and i > x + 1:
                save_board[i - 1][j] = board[i][j]
            # right
            elif j == M - 1 and i < N - 1:
                save_board[i + 1][j] = board[i][j]

    return save_board

def sum_dust(board):
    total = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                total += board[i][j]
    
    return total


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
up_cleaner, down_cleaner = info_cleaner(board)
while time < T:
    board = dust_spread(board)
    board = dust_rotate(board, up_cleaner, down_cleaner)

    time += 1

answer = sum_dust(board)

print(answer)

