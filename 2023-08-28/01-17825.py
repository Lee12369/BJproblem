from collections import defaultdict
import sys
input = sys.stdin.readline

class Piece:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

def piece_on_move_place(pieces, row, column):
    # 도착 지점은 위치가 겹쳐도 상관이 없다.
    if row > 4:
        return False
    
    # 이동 지점에 말이 있는 경우 False, 전부 겹치지 않는다면 True
    for piece in pieces:
        if piece.row == row and piece.column == column:
            return True
        # 서로 다른 행에 있는 40은 같은 위치를 가리키므로 예외 처리
        if board[row][column] == board[piece.row][piece.column] and board[row][column] == 40:
            return True
    return False

def escape_list(board, row, column):
    # 배열의 길이를 벗어날 경우.
    N = len(board[row])
    if column >= N:
        if row == 0 or row == 4:
            row = 5
            column = 0
        elif row == 1 or row == 2 or row == 3:
            row = 4
            # 다시 재귀를 돌리는 이유는 4변째 행 기준으로 column이 배열의 길이를 벗어날 수도 있기 때문이다. 예를 들어 26번 위치에서 5가 떠서 움직일 경우, 다음 배열을 건너뛰고 도착지점인 row = 5에 도착하게 된다. 그렇게 되면 row = 4로 되어있는 지금 indexError가 뜰 수 있다. 
            return escape_list(board, row, column - N)
    return row, column


def back_tracking(pieces, nums_index, scores):
    if nums_index == 10:
        answer.add(scores)
        return
    
    for i in range(4):
        piece = pieces[i]
        row = piece.row
        column = piece.column + nums[nums_index]
        if row == 5:
            continue

        # 배열의 길이를 벗어날 경우.
        row, column = escape_list(board, row, column)
        # N = len(board[row])
        # if column >= N:
        #     if row == 0 or row == 4:
        #         row = 5
        #         column = 0
        #     elif row == 1 or row == 2 or row == 3:
        #         row = 4
        #         column = column - N

        # 첫 행에서 특정 위치에 도착할 경우 행을 변경한다.
        if change_row[(row, column)]:
            row = change_row[(row, column)]
            column = 0 

        # 위치가 겹칠 경우
        if piece_on_move_place(pieces, row, column):
            continue
        
        new_pieces = list(pieces[:])
        new_pieces[i] = Piece(row, column)
        score = board[row][column]
        
        back_tracking(new_pieces, nums_index + 1, scores + score)

board = [[2 * i for i in range(21)], [10, 13, 16, 19], [20, 22, 24], [30, 28, 27, 26], [25, 30, 35, 40], [0]]
change_row = {
    (0, 5) : 1,
    (0, 10) : 2,
    (0, 15) : 3
}
change_row = defaultdict(bool, change_row)

nums = list(map(int, input().split()))
pieces = [Piece(0, 0), Piece(0, 0), Piece(0, 0), Piece(0, 0)]
nums_index = 0
scores = 0
answer = set()

back_tracking(pieces, nums_index, scores)

ans = max(answer)

print(ans)
