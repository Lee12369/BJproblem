N = int(input())
mine_board = [list(input()) for _ in range(N)]
x_board = [list(input()) for _ in range(N)]
ans_board = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

step_mine = 0
for i in range(N):
    for j in range(N):
        if x_board[i][j] == 'x' and mine_board[i][j] == '.':
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N and mine_board[nx][ny] == '*':
                    ans_board[i][j] += 1
        
        elif x_board[i][j] == 'x' and mine_board[i][j] == '*':
            step_mine = 1
        else:
            ans_board[i][j] = '.'

# 지뢰 밟을 경우 지뢰 표시.
if step_mine == 1:
    for i in range(N):
        for j in range(N):
            if mine_board[i][j] == '*':
                ans_board[i][j] = '*'

for lst in ans_board:
    for x in lst:
        print(x, end='') 
    print()