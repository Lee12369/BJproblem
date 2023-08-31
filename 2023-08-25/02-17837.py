import sys
input = sys.stdin.readline

class pieces:
    def __init__(self, row, column, direct) -> None:
        self.row = row
        self.column = column
        self.direct = direct


def white_color(row, column, move_row, move_column, num, direct):
    tower = piece_board[row][column]

    # 움직일 말의 위치를 찾고 움직이는 말 뒤에 있는 전부를 이동.
    idx = tower.index(num)
    move_pieces = tower[idx:]
    piece_board[move_row][move_column].extend(move_pieces)
    piece_board[row][column] = tower[:idx]

    # 움직이는 말들의 위치 정보를 수정
    for number in move_pieces:
        dic_piece[number].row = move_row
        dic_piece[number].column = move_column

def red_color(row, column, move_row, move_column, num, direct):
    tower = piece_board[row][column]

    idx = tower.index(num)
    move_pieces = tower[idx:]
    piece_board[move_row][move_column].extend(move_pieces[::-1]) # red칸에는 순서가 반대로 되서 더해준다.
    piece_board[row][column] = tower[:idx]

    for number in move_pieces:
        dic_piece[number].row = move_row
        dic_piece[number].column = move_column

def blue_color(row, column, move_row, move_column, num, direct):
    change_direct = {
        1 : 2,
        2 : 1,
        3 : 4,
        4 : 3
    }
    
    new_direct = change_direct[direct]

    new_move_row = row + dx[new_direct]
    new_move_column = column + dy[new_direct]
    
    dic_piece[num].direct = new_direct

    # 새로 움직일 위치 역시 범위에서 벗어나거나 파란 칸일 경우 그대로 종료.
    if not (0 <= new_move_row < N and 0 <= new_move_column < N):
        return
    
    new_color = board[new_move_row][new_move_column]
    if new_color == 2:
        return
    
    # white or blue
    func_color[new_color](row, column, new_move_row, new_move_column, num, new_direct)


# 종료 조건. 말의 개수가 4개 이상 쌓이는 순간 그대로 종료한다. 말이 움직일 때마다 확인해야한다.
def stop():
    for i in range(N):
        for j in range(N):
            if len(piece_board[i][j]) >= 4:
                return True
    return False

def main():
    time = 1
    while time <= 1000:
        for num in range(1, K + 1):
            piece = dic_piece[num]
            row, column, direct = piece.row, piece.column, piece.direct

            move_row = row + dx[direct]
            move_column = column + dy[direct]

            if not (0 <= move_row < N and 0 <= move_column < N):
                blue_color(row, column, move_row, move_column, num, direct)
                continue

            board_color = board[move_row][move_column]
            
            func_color[board_color](row, column, move_row, move_column, num, direct)

            if stop():
                return time

        time += 1
    
    return -1



# N, K = 4, 4
# board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# piece_board = [[[] for _ in range(N)] for _ in range(N)]
# dic_piece = {}
# inputs = [[1,1,1],[1,2,1],[1,3,1],[3,3,3]]

# N, K = 6, 10
# board = [[0,1,2,0,1,1],[1,2,0,1,1,0],[2,1,0,1,1,0],[1,0,1,1,0,2],[2,0,1,2,0,1],[0,2,1,0,2,1]]
# piece_board = [[[] for _ in range(N)] for _ in range(N)]
# dic_piece = {}
# inputs = [[1,1,1],[2,2,2],[3,3,4],[4,4,1],[5,5,3],[6,6,2],[1,6,3],[6,1,2],[2,4,3],[4,2,1]]

# num = 1
# for nums in inputs:
#     row, column, direct = nums
#     dic_piece[num] = pieces(row - 1, column - 1, direct)
#     piece_board[row - 1][column - 1].append(num)
#     num += 1

N, K = map(int, input().split())
# 색깔 번호가 적힌 보드판
board = [list(map(int, input().split())) for _ in range(N)]

# 말의 번호가 적히는 보드판
piece_board = [[[] for _ in range(N)] for _ in range(N)]

# 말의 정보를 담는 곳
dic_piece = {}
for num in range(1, K + 1):
    row, column, direct = map(int, input().split())
    dic_piece[num] = pieces(row - 1, column - 1, direct)
    piece_board[row - 1][column - 1].append(num)


# 오, 왼, 위, 아래
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

func_color = {
    0 : white_color,
    1 : red_color,
    2 : blue_color
}

ans = main()

print(ans)
