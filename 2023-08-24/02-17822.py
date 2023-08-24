from collections import deque
import sys
input = sys.stdin.readline

def rotation(board, i, k):
    board[i].rotate(k)

def reverse_rotation(board, i, k):
    board[i].rotate(-k)

def delete_near_same_number(board):
    new_board = [deque(lst) for lst in board]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and board[i][j] == board[i][j - 1]:
                new_board[i][j] = 0
                new_board[i][j - 1] = 0

    for j in range(M):
        for i in range(1, N):
            if board[i][j] > 0 and board[i][j] == board[i - 1][j]:
                new_board[i][j] = 0
                new_board[i - 1][j] = 0

    if board == new_board:
        return False
    
    return new_board

def get_average(board):
    sum_num = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                sum_num += board[i][j]
                cnt += 1
    if cnt == 0:
        return 0
    
    return sum_num / cnt

def plus_or_minus(board, average):
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                if board[i][j] > average:
                    board[i][j] -= 1
                elif board[i][j] < average:
                    board[i][j] += 1

def get_answer(board):
    ans = 0
    for lst in board:
        ans += sum(lst)
    return ans



dic_rotate = {
    0 : rotation,
    1 : reverse_rotation
}

# N, M, T = 4,4, 4
# inputs = [[1,1,2,3],[5,2,4,2],[3,1,3,5],[2,1,3,2]]
# board = []
# for nums in inputs:
#     board.append(deque(nums))

N, M, T = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    
    # rotate - reverse_rotate
    for i in range(N):
        if (i + 1) % x == 0:
            dic_rotate[d](board, i, k)
    
    # delete
    new_board = delete_near_same_number(board)
    if new_board == False:
        average = get_average(board)
        plus_or_minus(board, average)
    else:
        board = new_board

ans = get_answer(board)

print(ans)
        