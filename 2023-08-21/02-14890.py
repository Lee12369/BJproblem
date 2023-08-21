import sys
input = sys.stdin.readline

# 이전 낮은 구간에 경사로를 놓을 수 있는지 확인
def low_to_high(board, x, y, visited):
    num = board[x][y - 1]
    for i in range(L):
        idx = y - 1 - i
        # board의 범위를 벗어난 경우, 이미 경사로를 놓은 적이 있는 경우, 경사로를 놓는 구간의 높이가 달라질 경우 경사로를 놓을 수 없다.
        if idx < 0 or visited[idx] == 1 or board[x][idx] != num:
            return False
        visited[idx] = 1
    return True

# 이후 낮은 구간에 경사로를 놓을 수 있는지 확인
def high_to_low(board, x, y, visited):
    num = board[x][y]
    for i in range(L):
        idx = y + i
        # board의 범위를 벗어난 경우, 이미 경사로를 놓은 적이 있는 경우, 경사로를 놓는 구간의 높이가 달라질 경우 경사로를 놓을 수 없다.
        if idx >= N or visited[idx] == 1 or board[x][idx] != num:
            return False
        visited[idx] = 1
    return True

def possible(board, i, visited):
    pre = board[i][0]
    for j in range(N):
        curr = board[i][j]
        # 1칸 높은 경우
        if curr - pre == 1:
            if not low_to_high(board, i, j, visited):
                return False
        # 1칸 낮은 경우
        elif curr - pre == -1:
            if not high_to_low(board, i, j, visited):
                return False
        # 높이 차가 2칸 이상일 경우
        elif abs(curr - pre) > 1:
            return False
        pre = int(curr)

    return True

# 행렬 전환
def change_row_column(board):
    transposed = [[board[j][i] for j in range(N)] for i in range(N)]    
    return transposed

# ex 1, 2
# N, L = 6,2
# board = [[3,3,3,3,3,3],[2,3,3,3,3,3],[2,2,2,3,2,3],[1,1,1,2,2,2],[1,1,1,3,3,1],[1,1,2,3,3,2]]
# board = [[3,2,1,1,2,3],[3,2,2,1,2,3],[3,2,2,2,3,3],[3,3,3,3,3,3],[3,3,3,3,2,2],[3,3,3,3,2,2]]

# ex 3, 4
# N, L = 6, 3
# N, L = 6, 1
# board = [[3,2,1,1,2,3],[3,2,2,1,2,3],[3,2,2,2,3,3],[3,3,3,3,3,3],[3,3,3,3,2,2],[3,3,3,3,2,2]] 


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# row 확인
for i in range(N):
    visited = [0 for _ in range(N)]
    if possible(board, i, visited):
        ans += 1

# 행렬을 전환시켜 column확인
transposed_board = change_row_column(board)
for i in range(N):
    visited = [0 for _ in range(N)]
    if possible(transposed_board, i, visited):
        ans += 1

print(ans)
