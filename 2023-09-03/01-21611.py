import sys
input = sys.stdin.readline

# 거리와 방향에 따라 구슬을 제거한다.
def delete_marble(board, shark, magic):
    row, column = shark
    direct, dist = magic
    for _ in range(1, dist + 1):
        row += up_down_left_right_dx[direct]
        column += up_down_left_right_dy[direct]
        board[row][column] = 0

# 비어있는 공간에 순서대로 구슬이 움직인다.
def move_marble(board):
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    x, y = shark
    new_x, new_y = shark
    idx = 0
    new_idx = 0
    for idx in range(len(dx)):
        x += dx[idx]
        y += dy[idx]
        if board[x][y] == 0:
            continue
        new_x += dx[new_idx]
        new_y += dy[new_idx]

        new_board[new_x][new_y] = board[x][y]
        new_idx += 1

    return new_board

# 4개 이상 시 폭발
def partial_explosion(board, cnt, group, marble_cnt, same_marble):
    for tpl in group:
        a, b = tpl
        board[a][b] = 0
    marble_cnt[same_marble] += len(group)
    cnt = cnt + len(group)
    return cnt

# 구슬 폭발
def explosion(board):
    x, y = shark
    same_marble = 0
    group = []
    cnt = 0
    for i in range(len(dx)):
        x += dx[i]
        y += dy[i]
        number = board[x][y]
        if number > 0:
            # 숫자가 같으면 group에 추가
            if number == same_marble:
                group.append((x, y))
            # 숫자가 다르면 group에 4개 이상이 들었는지 확인하고 현재 숫자로 초기화
            elif number != same_marble:
                if len(group) >= 4:
                    cnt = partial_explosion(board, cnt, group, marble_cnt, same_marble)
                same_marble = number
                group = [(x, y)]
        # 숫자가 0이면 더는 탐색을 멈추어도 무방.
        elif number == 0:
            if len(group) >= 4:
                cnt = partial_explosion(board, cnt, group, marble_cnt, same_marble)
            same_marble = 0
            group = []
    # 폭발한 구슬이 없으면 False 반환
    if cnt == 0:
        return False
    return True

def rebuild_board(board):
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    new_x, new_y = shark
    new_idx = 0

    x, y = shark
    same_marble = board[x][y - 1]
    cnt = 0
    for i in range(len(dx)):
        x += dx[i]
        y += dy[i]
        number = board[x][y]
        if number > 0:
            if number == same_marble:
                cnt += 1
            elif number != same_marble:
                # 보드 범위를 벗어나면 그대로 종료
                if new_idx >= len(dx):
                    break
                # 횟수 추가
                new_x += dx[new_idx]
                new_y += dy[new_idx]
                new_idx += 1
                new_board[new_x][new_y] = cnt

                # 보드 범위를 벗어나면 그대로 종료
                if new_idx >= len(dx):
                    break
                # 종류 추가
                new_x += dx[new_idx]
                new_y += dy[new_idx]
                new_idx += 1
                new_board[new_x][new_y] = same_marble

                # 현재 숫자로 초기화
                same_marble = number
                cnt = 1

        # 현재 구슬이 0이면 group에 들어있는걸 마저 추가하고 종료
        elif number == 0:
            # 위와 동일
            if new_idx >= len(dx):
                break
            new_x += dx[new_idx]
            new_y += dy[new_idx]
            new_idx += 1
            new_board[new_x][new_y] = cnt
            
            if new_idx >= len(dx):
                break
            new_x += dx[new_idx]
            new_y += dy[new_idx]
            new_idx += 1
            new_board[new_x][new_y] = same_marble
            break
    return new_board

# N, M = 7, 1
# board = [[0,0,0,0,0,0,0],[3,2,1,3,2,3,0],[2,1,2,1,2,1,0],[2,1,1,0,2,1,1],[3,3,2,3,2,1,2],[3,3,3,1,3,3,2],[2,3,2,2,3,2,3]]
# magics = [(2, 2)]

# N, M = 7, 4
# board = [[0,0,0,2,3,2,3],[1,2,3,1,2,3,1],[2,3,1,2,3,1,2],[1,2,3,0,2,3,1],[2,3,1,2,3,1,2],[3,1,2,3,1,2,3],[1,2,3,1,2,3,1]]
# magics = [(1, 3), (2, 2), (3, 1), (4, 3)]

# N, M = 7, 4
# board = [[1,1,1,2,2,2,3],[1,2,2,1,2,2,3],[1,3,3,2,3,1,2],[1,2,2,0,3,2,2],[3,1,2,2,3,2,2],[3,1,2,1,1,2,1],[3,1,2,2,2,1,1]]
# magics = [(1, 3), (2, 2), (3, 1),  (4, 3)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]

T = N // 2
shark = (T, T)

up_down_left_right_dx = {
    1 : -1,
    2 : 1,
    3 : 0,
    4 : 0
}

up_down_left_right_dy = {
    1 : 0,
    2 : 0,
    3 : -1,
    4 : 1
}

# 폭발한 구슬의 수 저장
marble_cnt = {
    1 : 0,
    2 : 0,
    3 : 0
}

# 상어를 기준으로 전체적인 순서를 먼저 저장한다. 
# ex) 3*3 : 왼1, 아1, 오2, 위2, 왼2, 
# ex) 5*5 : 왼1, 아1, 오2, 위2, 왼2, 왼1, 아3, 오4, 위4, 왼4 
dx = []
dy = []
for i in range(T):
    odd = 2 * i + 1
    even = 2 * i + 2
    extend_dx = [0] + [1] * odd + [0] * even + [-1] * even + [0] * even
    extend_dy = [-1] + [0] * odd + [1] * even + [0] * even + [-1] * even
    dx.extend(extend_dx)
    dy.extend(extend_dy)

# 마법 사용
for magic in magics:
    # 구슬 삭제, 처음 파괴한 구슬은 폭발로 포함하지 않는다.
    delete_marble(board, shark, magic)
    # 구슬 이동과 폭발 반복
    while True:
        board = move_marble(board)
        # 폭발한 구슬이 없으면 종료
        if not explosion(board):
            break
    # 보드를 구슬 종류와 개수에 따라 다시 만들기
    board = rebuild_board(board)

ans = 0
for i in range(1, 4):
    ans += marble_cnt[i] * i

print(ans)