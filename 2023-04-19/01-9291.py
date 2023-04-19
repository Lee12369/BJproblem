import sys
input = sys.stdin.readline

def check_row():
    for i in range(9):
        temp = set()
        for j in range(9):
            temp.add(sudoku_board[i][j])
        
        if len(temp) < 9:
            return 0
    return 1


def check_column():
    for j in range(9):
        temp = set()
        for i in range(9):
            temp.add(sudoku_board[i][j])
        
        if len(temp) < 9:
            return 0
    return 1


def check_square():
    for k in range(3):
        for l in range(3):
            temp = set()
            for i in range(k * 3, (k + 1)* 3):
                for j in range(l * 3, (l + 1)* 3):
                    temp.add(sudoku_board[i][j])
        
            if len(temp) < 9:
                return 0
    return 1

case_cnt = 1
T = int(input())
for _ in range(T):
    sudoku_board = [list(map(int, input().split())) for _ in range(9)]
    if check_row() and check_column() and check_square():
        print("Case {}: CORRECT".format(case_cnt))
    
    else:
        print("Case {}: INCORRECT".format(case_cnt))
    
    if case_cnt < T:
        input()

    case_cnt += 1
    