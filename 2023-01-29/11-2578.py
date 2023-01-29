def get_row_bingo(lst):
    cnt = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            idx = (i * 5) + j
            if lst[idx] == 0:
                temp +=1
        if temp == 5:
            cnt += 1 

    return cnt

def get_column_bingo(lst):
    cnt = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            idx = (j * 5) + i
            if lst[idx] == 0:
                temp +=1
        if temp == 5:
            cnt += 1 

    return cnt

 

def get_diagonal_bingo(arr):
    cnt = 0
    temp1= temp2 = 0
    for i in range(5):
        if arr[i * 6] == 0:
            temp1 += 1

        if arr[i * 4 + 4] == 0:
            temp2 += 1

    if temp1 == 5:
        cnt += 1
    if temp2 == 5:
        cnt += 1

    return cnt

arr_bingo_board = [list(map(int, input().split())) for _ in range(5)]
arr_call_nums = [list(map(int, input().split())) for _ in range(5)]

bingo_board = []
call_nums = []

for lst in arr_bingo_board:
    bingo_board += lst

for lst in arr_call_nums:
    call_nums += lst

for i in range(25):
    idx = bingo_board.index(call_nums[i])
    bingo_board[idx] = 0
    bingo_cnt = get_row_bingo(bingo_board) + get_column_bingo(bingo_board) + get_diagonal_bingo(bingo_board)
    
    if bingo_cnt >= 3:
        N = i + 1
        print(N)
        break