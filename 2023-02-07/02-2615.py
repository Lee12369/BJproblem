def get_row(arr, i, N):
    j = 0
    while j < 19:
        cnt = 0
        while j < 19 and arr[i][j] == N:
            j += 1
            cnt += 1
        
        if cnt == 5:
            winner = N
            win_x, win_y = i + 1, j - 4
            return [winner, win_x, win_y]
        
        j += 1
    return 0

def get_column(arr, i, N):
    j = 0
    while j < 19:
        cnt = 0
        while j < 19 and arr[j][i] == N:
            j += 1
            cnt += 1
        
        if cnt == 5:
            winner = N
            win_x, win_y = j - 4, i + 1
            return [winner, win_x, win_y]
        
        j += 1
    return 0

def get_diag_right(arr, i, j, N):
    while i < 19 and j < 19:
        cnt = 0
        while i < 19 and j < 19 and arr[i][j] == N:
            i += 1
            j += 1
            cnt += 1
        
        if cnt == 5:
            winner = N
            win_x, win_y = i - 4, j - 4
            return [winner, win_x, win_y]
        i += 1
        j += 1
    return 0

def get_diag_left(arr, i, j, N):
    while i < 19 and j >= 0:
        cnt = 0
        while i < 19 and j >= 0 and arr[i][j] == N:
            i += 1
            j -= 1
            cnt += 1
        
        if cnt == 5:
            winner = N
            win_x, win_y = i, j + 2
            return [winner, win_x, win_y]
        i += 1
        j -= 1
    return 0

arr = [list(map(int, input().split())) for _ in range(19)]
answer = 0

for i in range(19):
    win_row1 = get_row(arr, i, 1)
    win_row2 = get_row(arr, i, 2)

    win_col1 = get_column(arr, i, 1)
    win_col2 = get_column(arr, i, 2)

    lst = [win_row1, win_row2, win_col1, win_col2]
    for x in lst:
        if x != 0:
            answer = x
    
for i in range(19):
    win_dig_r1_1 = get_diag_right(arr, i, 0, 1)
    win_dig_r1_2 = get_diag_right(arr, 0, i, 1)
    
    win_dig_r2_1 = get_diag_right(arr, i, 0, 2)
    win_dig_r2_2 = get_diag_right(arr, 0, i, 2)
    
    
    win_dig_l1_1 = get_diag_left(arr, i, 0, 1)
    win_dig_l1_2 = get_diag_left(arr, 0, i, 1)
    
    win_dig_l2_1 = get_diag_left(arr, i, 0, 2)
    win_dig_l2_2 = get_diag_left(arr, 0, i, 2)

    lst = [win_dig_r1_1, win_dig_r1_2, win_dig_r2_1, win_dig_r2_2, win_dig_l1_1, win_dig_l1_2, win_dig_l2_1, win_dig_l2_2]
    for x in lst:
        if x != 0:
            answer = x
        
if answer != 0:
    winner = answer[0]
    row, column = answer[1], answer[2]

    print(winner)
    print(row, column)
else:
    print(0)