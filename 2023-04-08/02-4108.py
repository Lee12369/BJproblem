import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break

    mine_board = [list(input().strip()) for _ in range(R)]
    ans_board = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if mine_board[i][j] == '.':
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and mine_board[nx][ny] == '*':
                        ans_board[i][j] += 1
            
            elif mine_board[i][j] == '*':
                ans_board[i][j] = '*'

    for lst in ans_board:
        for ans in lst:
            print(ans, end='')
        print()
