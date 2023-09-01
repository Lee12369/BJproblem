import sys, copy
input = sys.stdin.readline

def get_bead(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red_bead = (i, j)
            if board[i][j] == 'B':
                blue_bead = (i, j)
    
    return red_bead, blue_bead

def back_tracking(board, red_bead, blue_bead, time):
    if time > 10:
        return
    
    for i in range(4):
        rx, ry = red_bead
        bx, by = blue_bead
        
        move_rx, move_ry = move_bead(red_bead, dx[i], dy[i])
        move_bx, move_by = move_bead(blue_bead, dx[i], dy[i])

        # 파란 구슬이 구멍에 들어갈 경우 현재 case 종료
        if board[move_bx][move_by] == 'O':
            continue

        # 빨간 구슬이 구멍에 들어간 것이 확인되면 시간 저장 후 종료
        if board[move_rx][move_ry] == 'O':
            answer.append(time)
            return

        # 빨간 구슬과 파란 구슬의 위치가 같을 때
        if move_rx == move_bx and move_ry == move_by:
            # 위로 이동할 때 초기 위치가 아래에 있는 구슬을 한 칸 아래으로 이동시킨다.
            if dx[i] == -1:
                if rx > bx:
                    move_rx += 1
                else:
                    move_bx += 1
            # 아래
            elif dx[i] == 1:
                if rx > bx:
                    move_bx -= 1
                else:
                    move_rx -= 1
            # 왼쪽    
            elif dy[i] == -1:
                if ry > by:
                    move_ry += 1
                else:
                    move_by += 1
            # 오른쪽
            elif dy[i] == 1:
                if ry > by:
                    move_by -= 1
                else:
                    move_ry -= 1

        if rx == move_rx and ry == move_ry and bx == move_bx and by == move_by:
            continue

        new_red_bead = (move_rx, move_ry)
        new_blue_bead = (move_bx, move_by)
        new_time = time + 1
        
        back_tracking(board, new_red_bead, new_blue_bead, new_time)

def move_bead(bead, move_x, move_y):
    x, y = bead
    while board[x][y] != '#':
        if board[x][y] == 'O':
            return (x, y)
        x += move_x
        y += move_y
    
    return (x - move_x, y - move_y)
# ex1
# N, M = 5, 5
# board = [['#','#','#','#','#'], ['#','.','.','B','#'], ['#','.','#','.','#'], ['#','R','O','.','#'], ['#','#','#','#','#']]

# ex2
# N, M = 7, 7
# board = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', 'R', 'B', '#'], ['#', '.', '#', '#', '#', '#','#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#','#','.','#'], ['#','O', '.','.','.','.','#'], ['#', '#', '#', '#', '#', '#', '#']]

# ex3
# N, M = 7, 7
# board = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', 'R', '#', 'B', '#'], ['#', '.', '#', '#', '#', '#','#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#','#','.','#'], ['#','O', '.','.','.','.','#'], ['#', '#', '#', '#', '#', '#', '#']]

# ex6
# N, M = 10, 10
# board = [['#', '#','#','#','#','#','#','#','#','#'], ['#', 'R','#','.','.','.','#','#','B','#'],['#', '.','.','.','#','.','#','#','.','#'],['#', '#','#','#','#','.','#','#','.','#'],['#', '.','.','.','.','.','.','#','.','#'],['#', '.','#','#','#','#','#','#','.','#'],['#', '.','#','.','.','.','.','#','.','#'],['#', '.','#','.','#','#','.','.','.','#'],['#', 'O','.','.','#','.','.','.','.','#'],['#', '#','#','#','#','#','#','#','#','#']]

# ex7
# N, M = 3, 10
# board = [['#','#','#','#','#','#','#','#','#','#'], ['#','.','O','.','.','.','.','R','B','#'], ['#','#','#','#','#','#','#','#','#','#']]

# N, M = 7,8
# board = [['#','#','#','#','#','#','#','#'],['#','.','#','O','.','#','R','#'],['#','.','.','.','.','#','B','#'],['#','.','#','.','.','.','.','#'],['#','.','.','.','.','.','.','#'],['#','.','.','.','.','.','.','#'],['#','#','#','#','#','#','#','#']]

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

time = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

red_bead, blue_bead = get_bead(board)

answer = []
back_tracking(board, red_bead, blue_bead, time)

if answer:
    print(1)
else:
    print(0)
