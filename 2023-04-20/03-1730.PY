def check_UD(x, y):
    if board[x][y] == '.':
        board[x][y] = '|'

    elif board[x][y] == '-':
        board[x][y] = '+' 

def check_LR(x, y):
    if board[x][y] == '.':
        board[x][y] = '-'

    elif board[x][y] == '|':
        board[x][y] = '+' 

N = int(input())
moves = list(input())

board = [['.' for _ in range(N)] for _ in range(N)]

x = 0
y = 0
for move in moves:
    if move == 'U' and 0 <= x - 1 < N:
        check_UD(x, y)
        check_UD(x - 1, y)
        x -= 1
    
    elif move == 'D' and 0 <= x + 1 < N:
        check_UD(x, y)
        check_UD(x + 1, y)
        x += 1
    
    elif move == 'L' and 0 <= y - 1 < N:
        check_LR(x, y)
        check_LR(x, y - 1)
        y -= 1
    
    elif move == 'R' and 0 <= y + 1 < N:
        check_LR(x, y)
        check_LR(x, y + 1)
        y += 1

for i in range(N):
    for j in range(N):
        print(board[i][j], end='')
    print()
    
    