N = int(input())
square_board = [list(input()) for _ in range(N)]

# 심장
heart = False
for i in range(N):
    for j in range(N):
        if square_board[i][j] == '*':
            heart = (i + 1, j)
            break
    
    if heart:
        break

# 팔
i = heart[0]
left_arm = 0
right_arm = 0
for j in range(N):
    if j < heart[1] and square_board[i][j] == '*':
        left_arm += 1
    
    elif j > heart[1] and square_board[i][j] == '*':
        right_arm += 1

# 허리
waist = 0
j = heart[1]
for i in range(heart[0] + 1, N):
    if square_board[i][j] == '*':
        waist += 1
    else:
        break 

# 다리
left_leg = 0
right_leg = 0
start_i = heart[0] + waist
for i in range(start_i, N):
    if square_board[i][heart[1] - 1] == '*':
        left_leg += 1
    
    if square_board[i][heart[1] + 1] == '*':
        right_leg += 1

print(heart[0] + 1, heart[1] + 1)
print("{} {} {} {} {}".format(left_arm, right_arm, waist, left_leg, right_leg))