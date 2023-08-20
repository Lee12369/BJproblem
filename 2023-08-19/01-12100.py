from collections import deque
import sys
input = sys.stdin.readline

def back_tracking(board, cnt):
    if cnt == 5:
        get_max(board)
        return
    
    save_cnt = cnt + 1
    
    up_board = up(board)
    back_tracking(up_board, save_cnt)
    
    down_board = down(board)
    back_tracking(down_board, save_cnt)
        
    right_board = right(board)
    back_tracking(right_board, save_cnt)
        
    left_board = left(board)
    back_tracking(left_board, save_cnt)


def up(board):
    new_board = []
    for j in range(N):
        nums = deque()
        for i in range(N):
            if board[i][j] == 0:
                continue
            nums.append(board[i][j])
        
        new_lst = left_sum(nums)
        new_board.append(new_lst)

    new_board = transpose(new_board)
    return new_board

def down(board):
    new_board = []
    for j in range(N):
        nums = deque()
        for i in range(N):
            if board[i][j] == 0:
                continue
            nums.append(board[i][j])
        
        new_lst = right_sum(nums)
        new_board.append(new_lst)

    new_board = transpose(new_board)
    return new_board


def right(board):
    new_board = []
    for i in range(N):
        nums = deque()
        for j in range(N):
            if board[i][j] == 0:
                continue
            nums.append(board[i][j])
        
        new_lst = right_sum(nums)
        new_board.append(new_lst)
    return new_board


def left(board):
    new_board = []
    for i in range(N):
        nums = deque()
        for j in range(N):
            if board[i][j] == 0:
                continue
            nums.append(board[i][j])
        
        new_lst = left_sum(nums)
        new_board.append(new_lst)

    return new_board

def left_sum(nums):
    new_lst = []
    sum_nums = deque()
    while nums:
        if len(sum_nums) < 2:
            num = nums.popleft()
            sum_nums.append(num)
        
        if len(sum_nums) == 2:
            first = sum_nums.popleft()
            second = sum_nums.popleft()
            if first == second:
                new_lst.append(2 * first)
            else:
                new_lst.append(first)
                sum_nums.append(second)
    
    while sum_nums:
        num = sum_nums.popleft()
        new_lst.append(num)

    while len(new_lst) < N:
        new_lst.append(0)
    
    return new_lst

def right_sum(nums):
    new_lst = deque()
    sum_nums = deque()
    while nums:
        if len(sum_nums) < 2:
            num = nums.pop()
            sum_nums.appendleft(num)
        
        if len(sum_nums) == 2:
            first = sum_nums.pop()
            second = sum_nums.pop()
            if first == second:
                new_lst.appendleft(2 * first)
            else:
                new_lst.appendleft(first)
                sum_nums.appendleft(second)
    
    while sum_nums:
        num = sum_nums.pop()
        new_lst.appendleft(num)

    while len(new_lst) < N:
        new_lst.appendleft(0)

    return list(new_lst)

def get_max(board):
    max_num = 0
    for lst in board:
        for num in lst:
            if num > max_num:
                max_num = num
    
    answer.append(max_num)

## 행렬 전환
def transpose(board):
    transposed = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            transposed[i][j] = board[j][i]
    
    return transposed

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []

back_tracking(board, cnt)

## 출력
print(max(answer))