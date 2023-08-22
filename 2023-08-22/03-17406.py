import sys
input = sys.stdin.readline

def total_rotate(board, command):
    r, c, s = command
    for i in range(1, s + 1):
        row_start = r - i
        row_end = r + i
        column_start = c - i
        column_end = c + i
        
        board = partial_rotate(board, row_start, row_end, column_start, column_end)
    return board

def partial_rotate(board, row_start, row_end, column_start, column_end):
    new_board = [lst[:] for lst in board]
    # up
    for j in range(column_start + 1, column_end + 1):
        new_board[row_start][j] = board[row_start][j - 1]

    # down
    for j in range(column_start + 1, column_end + 1):
        new_board[row_end][j - 1] = board[row_end][j]

    # left
    for i in range(row_start + 1, row_end + 1):
        new_board[i - 1][column_start] = board[i][column_start]

    # right
    for i in range(row_start + 1, row_end + 1):
        new_board[i][column_end] = board[i - 1][column_end]

    return new_board

def back_tracking(board, commands, cnt, visited):
    if cnt == len(commands):
        min_num = 10000
        for lst in board:
            sum_num = sum(lst)
            if sum_num < min_num:
                min_num = sum_num
        answer.append(min_num)
        return

    T = len(commands)
    for i in range(T):
        if visited[i] == 0:
            visited[i] = 1
            command = commands[i]
            new_board = total_rotate(board, command)
            

            back_tracking(new_board, commands, cnt + 1, visited)

            visited[i] = 0
    return

# N, M, K = 5, 6, 2
# board = [[1,2,3,2,5,6],[3,8,7,2,1,3],[8,2,3,1,4,5],[3,4,5,1,1,1],[9,3,2,1,4,3]]
# commands = [(2,3,2),(3,1,1)]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

commands = []
for _ in range(K):
    r, c, s = map(int, input().split())
    commands.append((r - 1, c - 1, s))


visited = [0 for _ in range(len(commands))]
cnt = 0
answer = []

back_tracking(board, commands, cnt, visited)

## 출력
ans = min(answer)
print(ans)