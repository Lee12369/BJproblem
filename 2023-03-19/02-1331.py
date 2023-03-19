route = [input() for _ in range(36)]
route.append(route[0])

chess_board = [[0 for _ in range(6)] for _ in range(6)]

dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,-1,1,-2,-2]

valid = 1
for i in range(1, 37):
    pre = route[i - 1]
    curr = route[i]
    chess_board[ord(curr[0]) - 65][int(curr[1]) - 1] += 1
    check = 0
    for k in range(8):
        nx = ord(pre[0]) + dx[k]
        ny = int(pre[1]) + dy[k]
        if nx == ord(curr[0]) and ny == int(curr[1]):
            check = 1
            break
    if check == 0:
        valid = 0
        break

for lst in chess_board:
    for x in lst:
        if x != 1:
            valid = 0
            break

if valid == 1:
    print('Valid')
else:
    print('Invalid')
