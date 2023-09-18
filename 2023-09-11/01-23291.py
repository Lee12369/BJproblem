import sys
input = sys.stdin.readline

# 가작 적은 물고기가 있는 어항들에 물고기 한 마리씩 추가
def plus_fish(fishbowls):
    N = len(fishbowls)
    min_bowl = min(fishbowls)
    for i in range(N):
        if fishbowls[i] == min_bowl:
            fishbowls[i] += 1

# 시계 방향으로 90도 회전
def clockwise(plane):
    R = len(plane)
    C = len(plane[0])
    plane = [[plane[-i - 1][j] for i in range(R)] for j in range(C)]
    return plane

# 첫 번째 공중 부양
def levitation(board):
    while True:
        R = len(board)
        C = len(board[0])
        # 90도 회전해야하는 범위를 설정
        up_board = [[board[i][j] for j in range(C)] for i in range(R)]
        up_board = clockwise(up_board)
        
        # 바닥에 남는 범위
        down_board = board[-1][C:]
        # 바닥에 남은 길이보다 위로 올라간 길이가 길 경우 종료
        if len(up_board[0]) > len(down_board):
            return board
        
        # 위에 올라갈 보드를 먼저 저장하고 마지막에 아래에 깔리는 보드를 저장
        new_board = [lst[::] for lst in up_board]
        new_board.append(down_board)
        board = new_board

# 물고기 증감량 저장
def check_move_fishes(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt_board = [[0 for _ in range(len(board[i]))] for i in range(len(board))]
    R = len(board)
    for i in range(R):
        C = len(board[i])
        for j in range(C):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < R and 0 <= ny < len(board[nx]) and board[i][j] > board[nx][ny]:
                    d = (board[i][j] - board[nx][ny]) // 5
                    cnt_board[i][j] -= d
                    cnt_board[nx][ny] += d
    return cnt_board

# 물고기 증감량 적용
def move_fishes(board, cnt_board):
    R = len(board)
    for i in range(R):
        C = len(board[i])
        for j in range(C):
            board[i][j] += cnt_board[i][j]
    return board
    
# 한 줄로 정리
def make_fishbowls(board):
    R = len(board)
    C = len(board[0])
    fishbowls = []
    for j in range(C):
        for row in board[::-1]:
            fishbowls.append(row[j]) 
    fishbowls.extend(board[-1][C:])
    return fishbowls

# 두 번째 공중부양
def second_levitation(fishbowls):
    # 2층
    C = N // 2
    board = [fishbowls[:C][::-1], fishbowls[C:]]

    # 4층
    R = 2
    C = C // 2
    left_board = [[board[i][j] for j in range(C)] for i in range(R)]
    # 180도 회전
    left_board = clockwise(clockwise(left_board))
    right_board = [[board[i][j] for j in range(C, 2 * C)] for i in range(R)]
    
    board = []
    board.extend(left_board)
    board.extend(right_board)

    # 물고기 조절 작업
    cnt_board = check_move_fishes(board)
    board = move_fishes(board, cnt_board)
    
    # 일자 정렬
    fishbowls = make_fishbowls(board)

    return fishbowls


def gap_fishbowls(fishbowls):
    max_fishbowl = max(fishbowls)
    min_fishbowl = min(fishbowls)
    gap = max_fishbowl - min_fishbowl
    return gap

# N, K = 8, 7 
# fishbowls = [5, 2, 3, 14, 9, 2, 11, 8]


# N, K = 4, 0 
# fishbowls = [1, 10000, 1, 10000]


N, K = map(int, input().split())
fishbowls = list(map(int, input().split()))

time = 1
while True:
    # 첫 번째 공중부양
    plus_fish(fishbowls)
    board = [[fishbowls[0]], fishbowls[1:]]
    board = levitation(board)
    cnt_board = check_move_fishes(board)
    board = move_fishes(board, cnt_board)
    fishbowls = make_fishbowls(board)

    # 두 번째 공중부양
    fishbowls = second_levitation(fishbowls)

    gap = gap_fishbowls(fishbowls)
    if gap <= K:
        break

    time += 1

print(time)