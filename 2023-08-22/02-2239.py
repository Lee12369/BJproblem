import sys, copy
input = sys.stdin.readline

def back_tracking(board, cnt_0):
    if answer:
        return
    
    if cnt_0 == 0:
        new_board = copy.deepcopy(board)
        answer.append(new_board)
        return
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                numbers = get_possible_number(board, i, j)
                for num in numbers:
                    board[i][j] = num

                    back_tracking(board, cnt_0 - 1)

                    board[i][j] = 0

                return

def count_zero(board):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                cnt += 1
    return cnt

def get_possible_number(board, x, y):
    exist = [False for _ in range(10)]
    # row
    for j in range(9):
        num = board[x][j]
        if num > 0:
            exist[num] = True
    
    # column
    for i in range(9):
        num = board[i][y]
        if num > 0:
            exist[num] = True

    start_i = (x // 3) * 3
    start_j = (y // 3) * 3

    # square
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            num = board[i][j]
            if num > 0:
                exist[num] = True
    
    possible = [i for i in range(1, 10) if exist[i] == False]
    return possible

# board = [[1,0,3,0,0,0,5,0,9],[0,0,2,1,0,9,4,0,0],[0,0,0,7,0,4,0,0,0],[3,0,0,5,0,2,0,0,6],[0,6,0,0,0,0,0,5,0],[7,0,0,8,0,3,0,0,4],[0,0,0,4,0,1,0,0,0],[0,0,9,2,0,5,8,0,0],[8,0,4,0,0,0,1,0,7]]

board = [list(map(int, input().rstrip())) for _ in range(9)]
cnt_0 = count_zero(board)

answer = []
back_tracking(board, cnt_0)

for lst in answer[0]:
    for num in lst:
        print(num, end='')
    print()