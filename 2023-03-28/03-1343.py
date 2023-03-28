board = input()

len_board = len(board)

i = 0
while i < len_board:
    if board[i] == 'X':
        cnt = 0
        start = i
        while i < len_board and board[i] == 'X':
            i += 1
            cnt += 1
        end = start + cnt
    
        if cnt % 2 == 0:
            num_AAAA = cnt // 4
            num_BB = (cnt % 4) // 2
            board = board[:start] + 'AAAA' * num_AAAA + 'BB' * num_BB + board[end:]
        else:
            break
    i += 1

if 'X' not in board:
    print(board)
else:
    print('-1')
