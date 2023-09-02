from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, board, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    mineral_cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
                if board[nx][ny] == 'x':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    mineral_cnt += 1
    return mineral_cnt

# 바닥에 있는 것들을 중심으로 탐색했을 때 전체 미네랄 수와 같다면 공중에 떠 있는 클러스터는 없다는 의미다.
def check_cluster(board):
    total_cnt = 0
    visited = [[0 for _ in range(C)] for _ in range(R)]
    for j in range(C):
        if board[R - 1][j] == 'x' and visited[R - 1][j] == 0:
            mineral_cnt = bfs(R - 1, j, board, visited)
            total_cnt += mineral_cnt
    if total_cnt == mineral:
        return True, visited
    return False, visited

# 공중에 떠 있는 클러스터 하단을 기준으로 빈 공간이 얼마나 있는지 확인한다.
def count_empty(x, y, board):
    empty_cnt = 0
    for i in range(x + 1, R):
        if board[i][y] == 'x':
            return empty_cnt 
        empty_cnt += 1
    return empty_cnt 

# 하강
def down(down_visited, board):
    up_visited = [[0 for _ in range(C)] for _ in  range(R)]
    # 공중에 떠 있는 미네랄의 위치를 저장
    for i in range(R):
        for j in range(C):
            if down_visited[i][j] == 0 and board[i][j] == 'x':
                up_visited[i][j] = 1

    # 공중에 떠 있는 미네랄들 중 아래에 공간이 얼마나 남았는지 확인하고 이 중에서 가장 작은 값을 얻는다.
    min_empty = R
    for j in range(C):
        for i in range(R - 1, -1, -1):
            if up_visited[i][j] == 1:
                empty_cnt = count_empty(i, j, board)
                if empty_cnt < min_empty:
                    min_empty = empty_cnt
                break

    # 공중에 떠 있는 미네랄 들은 empty 공간만큼 더한 위치로 옮기고 바닥에 있는 미네랄은 원래 있던 위치로 배치한다.
    new_board = [['.' for _ in range(C)] for _ in  range(R)]
    for i in range(R):
        for j in range(C):
            if up_visited[i][j] == 1:
                new_board[i + min_empty][j] = 'x'
            if down_visited[i][j] == 1:
                new_board[i][j] = 'x'

    return new_board

# ex1
# R, C = 5,6
# board = [['.','.','.','.','.','.'], ['.','.','x','x','.','.'], ['.','.','x','.','.','.'], ['.','.','x','x','.','.'], ['.','x','x','x','x','.']]
# _ = 1
# heights = [1,1,1,1]

# ex2
# R, C = 8, 8
# board = [['.','.','.','.','.','.','.','.'], ['.','.','.','.','.','.','.','.'], ['.','.','.','x','.','x','x','.'], ['.','.','.','x','x','x','.','.'], ['.','.','x','x','x','.','.','.'], ['.','.','x','.','x','x','x','.'], ['.','.','x','.','.','.','x','.'], ['.','x','x','x','.','.','x','.']]
# _ = 5
# heights = [6, 6, 4, 3, 1]

# ex3
# R, C = 7, 6
# board = [['.','.','.','.','.','.'], ['.','.','.','.','.','.'], ['x','x','.','.','.','.'], ['.','x','x','.','.','.'], ['.','.','x','x','.','.'], ['.','.','.','x','x','.'], ['.','.','.','.','x','.']]
# _ = 2
# heights = [6,4]

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
_ = int(input())
heights = list(map(int, input().split()))

mineral = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == 'x':
            mineral += 1

cnt = 0
for height in heights:
    i = R - height
    # 왼쪽에서 막대기를 던지는 경우
    if cnt % 2 == 0:
        for j in range(C):
            if board[i][j] == 'x':
                board[i][j] = '.'
                mineral -= 1
                break_mineral = (i, j)
                break
    # 오른쪽에서 막대기를 던지는 경우
    elif cnt % 2 == 1:
        for j in range(C - 1, -1, -1):
            if board[i][j] == 'x':
                board[i][j] = '.'
                mineral -= 1
                break_mineral = (i, j)
                break
    
    # down_visited는 바닥에 붙어있는 미네랄의 위치를 표시한다.
    True_or_False, down_visited = check_cluster(board)
    # 공중에 클러스터가 존재 한다면
    if not True_or_False:
        board = down(down_visited, board)

    cnt += 1

# 출력
for row in board:
    for word in row:
        print(word, end='')
    print()