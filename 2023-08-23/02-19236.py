from collections import defaultdict
import sys, copy

input = sys.stdin.readline

class fishes:
    def __init__(self, row, column, direct, size):
        self.row = row
        self.column = column
        self.direct = direct
        self.size = size

class sharks:
    def __init__(self, row, column, direct, eat):
        self.row = row
        self.column = column
        self.direct = direct
        self.eat = eat

def move_fishes(board, fish_info):
    new_board = [lst[:] for lst in board]
    new_fish_info = defaultdict(bool, fish_info)
    for size in range(1, 17):
        if new_fish_info[size]:
            fish = new_fish_info[size]
            move_fish(new_board, new_fish_info, fish)

    return new_board, new_fish_info

def move_fish(new_board, new_fish_info, fish):
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    for direct in range(fish.direct, fish.direct + 8):
        if direct > 8:
            direct -= 8
        
        curr_row = int(fish.row)
        curr_column = int(fish.column)

        move_row = curr_row + dx[direct]
        move_column = curr_column + dy[direct]
            
        if 0 <= move_row < 4 and 0 <= move_column < 4 and new_board[move_row][move_column] >= 0:
            new_fish_info[fish.size].row = move_row
            new_fish_info[fish.size].column = move_column
            new_fish_info[fish.size].direct = direct

            moved_size = new_board[move_row][move_column]
            if moved_size > 0:
                new_fish_info[moved_size].row = curr_row
                new_fish_info[moved_size].column = curr_column
            
            new_board[move_row][move_column], new_board[curr_row][curr_column] = new_board[curr_row][curr_column], new_board[move_row][move_column]
            
            return

def find_food(moved_board, shark):
    foods = []
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    for num in range(1, 4):
        move_i = shark.row + dx[shark.direct] * num
        move_j = shark.column + dy[shark.direct] * num
        if 0 <= move_i < 4 and 0 <= move_j < 4 and moved_board[move_i][move_j] > 0:
            foods.append((move_i, move_j))
    return foods

def eat_shark(board, shark, fish, fish_info):
    new_board = [lst[:] for lst in board]

    new_board[shark.row][shark.column] = 0
    new_board[fish.row][fish.column] = -1

    new_shark = sharks(fish.row, fish.column, fish.direct, shark.eat + fish.size)

    new_fish_info = copy.deepcopy(fish_info)
    new_fish_info[fish.size] = False

    return new_board, new_shark, new_fish_info

def back_tracking(board, shark, fish_info):
    answer.append(shark.eat)

    moved_board, moved_fish_info = move_fishes(board, fish_info)

    foods = find_food(moved_board, shark)    
    for food in foods:
        i, j = food
        size = moved_board[i][j]
        fish = moved_fish_info[size]

        new_board, new_shark, new_fish_info = eat_shark(moved_board, shark, fish, moved_fish_info)

        back_tracking(new_board, new_shark, new_fish_info)


answer = []
board = [[0 for _ in range(4)] for _ in range(4)]
fish_info = defaultdict(bool)
for i in range(4):
    nums = list(map(int, input().split()))
    for j in range(4):
        fish_size, fish_direct = nums[2 * j], nums[2* j + 1]
        fish_info[fish_size] = fishes(i, j, fish_direct, fish_size)
        board[i][j] = fish_size

# answer = []
# board = [[0 for _ in range(4)] for _ in range(4)]
# fish_info = defaultdict(bool)
# inputs = [[7,6,2,3,15,6,9,8],[3,1,1,8,14,7,10,1],[6,1,13,6,4,3,11,4],[16,1,8,7,5,2,12,2]]
# for i in range(4):
#     for j in range(4):
#         fish_size, fish_direct = inputs[i][2 * j], inputs[i][2* j + 1]
#         fish_info[fish_size] = fishes(i, j, fish_direct, fish_size)
#         board[i][j] = fish_size

shark = sharks(0, 0, 0, 0)
fish = fish_info[board[0][0]]
board, shark, fish_info = eat_shark(board, shark, fish, fish_info)
board[0][0] = -1    # shark의 보드 위치는 -1.

back_tracking(board, shark, fish_info)

ans = max(answer)

print(ans)