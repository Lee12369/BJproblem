from collections import deque
import sys
input = sys.stdin.readline

# 영역의 크기, 무지개색 칸 수, row, column, num을 저장한다.
def get_area(num, x, y, visited):
    area_0 = 0
    area_num = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] == num:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    area_num += 1
                elif board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    area_0 += 1
    
    area = area_num + area_0
    if area < 2:
        return False
    
    result = (area, area_0, x, y, num)
    areas.append(result)
    return True

# 블록을 제거
def delete_block(num, x, y):
    EMPTY = int(1e9)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    board[x][y] = EMPTY
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] == num or board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    board[nx][ny] = EMPTY

# 중력 작용
def gravity(board):
    for j in range(N):
        curr_i = N - 1
        empty_i = N - 1
        empty_i = get_empty(board, empty_i, j)
        while empty_i > -1 and curr_i > -1:
            if empty_i <= curr_i:
                curr_i = empty_i - 1
                continue

            elif 0 <= board[curr_i][j] <= M:
                board[empty_i][j] = int(board[curr_i][j])
                board[curr_i][j] = EMPTY
                empty_i = get_empty(board, empty_i, j)
            
            elif board[curr_i][j] == -1:
                empty_i = get_empty(board, curr_i, j)

            curr_i -= 1

# 빈 공간을 찾는다.
def get_empty(board, empty_i, y):
    while empty_i >= 0:
        if board[empty_i][y] == EMPTY:
            break
        empty_i -= 1
    return empty_i

def counterclockwise(board):
    rotated = [[row[::-1][i] for row in board] for i in range(N)]
    return rotated

   

# N, M = 5, 3
# board = [[2,2,-1,3,1],[3,3,2,0,-1],[0,0,0,1,2],[-1,3,1,3,2],[0,3,2,2,1]]

# N, M = 6, 4
# board = [[2,3,1,0,-1,2],[2,-1,4,1,3,3],[3,0,4,2,2,1],[-1,4,-1,2,3,4],[3,-1,4,2,0,3],[1,2,2,2,2,1]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
EMPTY = int(1e9)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

score = 0
while True:
    areas = []
    for num in range(1, M + 1):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if num == board[i][j]:
                    get_area(num, i, j, visited)

    if not areas:
        break
    
    # 크기가 큰 수 대로 정렬하면 문제에서 요구하는 순서대로 정렬이 이루어진다. 면적이 가장 큰 수, 0의 개수가 가장 많은 수, row, column.
    areas.sort(reverse=True)
    big_area = areas[0]
    area, _, row, column, num = big_area

    delete_block(num, row, column)
    score += area * area

    gravity(board)
    board = counterclockwise(board)
    gravity(board)

print(score)