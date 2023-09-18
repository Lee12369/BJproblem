from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력값을 보드에 작성
def write_board(board, info, num):
    x, y = info[0], info[1]
    row = alphabets[x]
    col = int(y) - 1
    board[row][col] = num

# 스도쿠 규칙에 따라 비어있는 칸에 들어갈 수 있는 숫자를 기록
def possible_numbers(board, x, y):
    total = {1,2,3,4,5,6,7,8,9}
    numbers = set()
    for i in range(9):
        number = board[i][y]
        if number > 0:
            numbers.add(number)
        number = board[x][i]
        if number > 0:
            numbers.add(number)
    start_i = x // 3 * 3
    start_j = y // 3 * 3
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            if board[i][j] > 0:
                numbers.add(board[i][j])

    possible_board[x][y] = total - numbers

# 인접한 칸이 있어야 도미노를 집어넣을 수 있다. 이를 확인
def check_isolate(board, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 9 and 0 <= ny < 9 and board[nx][ny] == 0:
            return True
    return False

# 칸에 새로운 숫자가 들어갔을 때, possible_number에 값을 제거해주어야 중복해서 숫자가 들어가지 않는다.
def delete_possible_board(possible_board, x, y, num):
    new_possible_board = [[set(possible_board[i][j]) for j in range(9)] for i in range(9)]
    new_possible_board[x][y] = set()
    for i in range(9):
        new_possible_board[i][y] -= {num}
    
    for j in range(9):
        new_possible_board[x][j] -= {num}
    
    start_i = x // 3 * 3
    start_j = y // 3 * 3
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            new_possible_board[i][j] -= {num}
    return new_possible_board

def push_number(board, possible_board, cnt, i, j):
    # 현재 위치에서 들어갈 수 있는 숫자 중
    for num1 in possible_board[i][j]:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < 9 and 0 <= ny < 9 and board[nx][ny] == 0:
                # 인접한 위치에서 들어갈 수 있는 숫자
                for num2 in possible_board[nx][ny]:
                    # 두개의 숫자를 조합해서 domino가 있는 경우 도미노를 집어넣는다.
                    if dominos[(num1, num2)] == True or dominos[(num2, num1)] == True:
                        dominos[(num1, num2)] = False
                        dominos[(num2, num1)] = False
                        board[i][j] = num1
                        board[nx][ny] = num2

                        new_possible_board = delete_possible_board(possible_board, i, j, num1)
                        new_possible_board = delete_possible_board(new_possible_board, nx, ny, num2)

                        back_tracking(board, new_possible_board, cnt - 1)
                        
                        dominos[(num1, num2)] = True
                        board[i][j] = 0
                        board[nx][ny] = 0

def back_tracking(board, possible_board, cnt):
    if len(answer) == 1:
        return
    if cnt == 0:
        new_board = [row[:] for row in board]
        answer.append(new_board)
        return
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # 인접한 칸이 없이 한 칸만 비어있으면 도미노를 넣을 수 없다.
                if not check_isolate(board, i, j):
                    return
                # 숫자를 집어 넣는다.
                push_number(board, possible_board, cnt, i, j)
                # return 하는 이유는 board[i][j]에 0 인 상태로 넘어가기 때문에 이 지점에서 종료한다.
                return

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

alphabets = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8
}  

puzzle_cnt = 1
while True:
    board = [[0 for _ in range(9)] for _ in range(9)]
    N = int(input())
    if N == 0:
        break
    
    # 도미노의 전체 종류
    dominos = defaultdict(bool)
    for i in range(1, 10):
        for j in range(1, 10):
            if i < j:
                dominos[(i, j)] = True

    # 이미 사용한 도미노 체크하고 보드에 기록
    for _ in range(N):
        num1, info1, num2, info2 = input().split()
        num1, num2 = int(num1), int(num2)
        write_board(board, info1, num1)
        write_board(board, info2, num2)
        dominos[(min(num1, num2), max(num1, num2))] = False

    # 9개 지점 보드에 기록
    nums = list(input().split())
    for i in range(len(nums)):
        write_board(board, nums[i], i + 1)

    # 빈 칸인 보드에 넣을 수 있는 숫자 기록
    possible_board = [[set() for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possible_numbers(board, i, j)

    # 계산
    cnt = 36 - N
    answer = []
    back_tracking(board, possible_board, cnt)
    
    # 출력
    print("Puzzle {}".format(puzzle_cnt))
    for row in answer[0]:
        for num in row:
            print(num, end='')
        print()
        
    puzzle_cnt += 1
