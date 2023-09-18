from collections import defaultdict
import sys
input = sys.stdin.readline

def get_bead(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red_bead = (i, j)
            if board[i][j] == 'B':
                blue_bead = (i, j)
    
    return red_bead, blue_bead

def back_tracking(board, red_bead, blue_bead, time, command):
    if time > 10:
        return
    # 빨간 구슬과 파란 구슬의 위치에 따른 시간을 저장한다. 만약 같은 위치에 도달했을 때 시간이 더 오래 걸렸다면 더 진행할 의미가 없다. 그 이전의 과정이 더 짧은 시간이 걸릴 것이다.
    if info[(red_bead, blue_bead)] > 0 and info[(red_bead, blue_bead)] <= time:
        return
    info[(red_bead, blue_bead)] = time

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
            answer.append((time, command + commands[(dx[i], dy[i])]))
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

        new_red_bead = (move_rx, move_ry)
        new_blue_bead = (move_bx, move_by)
        new_time = time + 1
        
        back_tracking(board, new_red_bead, new_blue_bead, new_time, command + commands[(dx[i], dy[i])])

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

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

commands = {
    (-1, 0) : 'U',
    (1, 0) : 'D',
    (0, -1) : 'L',
    (0, 1) : 'R'
}

red_bead, blue_bead = get_bead(board)

info = defaultdict(int)

answer = []
time = 1
command = ''
back_tracking(board, red_bead, blue_bead, time, command)
answer.sort()

if answer:
    ans_time, ans_command = answer[0]
    print(ans_time)
    print(ans_command)
else:
    print(-1)