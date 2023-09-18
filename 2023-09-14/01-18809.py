# pypy3 통과, python3 시간 초과
from collections import deque
import sys
input = sys.stdin.readline

# 배양액을 놓을 수 있는 위치를 저장.
def get_possible_location(board):
    GR_location = [(i, j) for j in range(M) for i in range(N) if board[i][j] == 2]
    return GR_location

def back_tracking(board, G, lst_G, visited_G, R, lst_R, visited_R, GR_location):
    # 가지고 있는 모든 배양액을 사용한 경우
    if G == 0 and R == 0:
        cnt = spread_GR(board, lst_G, visited_G, lst_R, visited_R)
        answer.add(cnt)
        return

    # 배양액의 합이 놓을 수 있는 숫자보다 크게 되면 모든 배양액을 놓을 수 없다.
    if (R + G) > len(GR_location):
        return
    
    x, y = GR_location[0]
    # 초록색 배양액
    if G > 0:
        board[x][y] = 'G'
        visited_G[x][y] = 1
        
        back_tracking(board, G - 1, lst_G + [(x, y)], visited_G, R, lst_R, visited_R, GR_location[1:])
        
        board[x][y] = 2
        visited_G[x][y] = 0
    
    # 빨간색 배양액
    if R > 0:
        board[x][y] = 'R'
        visited_R[x][y] = 1

        back_tracking(board, G, lst_G, visited_G, R - 1, lst_R  + [(x, y)], visited_R, GR_location[1:])
        
        board[x][y] = 2
        visited_R[x][y] = 0
    
    # 배양액을 뿌리지 않고 건너띈다.
    back_tracking(board, G, lst_G, visited_G, R, lst_R, visited_R, GR_location[1:])
 
def spread(new_board, queue, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    length = len(queue)
    for _ in range(length):
        x, y = queue.popleft()
        # 꽃의 경우, 배양액은 퍼지지 않는다.
        if new_board[x][y] == 'F':
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and (new_board[nx][ny] == 1 or new_board[nx][ny] == 2):
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return queue, visited


# 배양액이 퍼지는 과정.
def spread_GR(board, lst_G, visited_G, lst_R, visited_R):
    queue_G = deque()
    queue_G.extend(lst_G)
    
    queue_R = deque()
    queue_R.extend(lst_R)

    new_board = [row[:] for row in board]
    new_visited_G = [row[:] for row in visited_G]
    new_visited_R = [row[:] for row in visited_R]

    # 꽃을 피운 횟수
    cnt = 0
    while queue_G and queue_R:
        queue_G, new_visited_G = spread(new_board, queue_G, new_visited_G)
        queue_R, new_visited_R = spread(new_board, queue_R, new_visited_R)
        # 초록 배양액을 기록
        for tpl in queue_G:
            x, y = tpl
            new_board[x][y] = 'G'
        
        # 빨간 배양액을 기록. 만약 초록 배양액이 있으면 꽃을 피운다는 의미에서 'F'를 기록
        for tpl in queue_R:
            x, y = tpl
            if new_board[x][y] == 'G':
                new_board[x][y] = 'F'
                cnt += 1
            else:
                new_board[x][y] = 'R'

    return cnt

# N, M, G, R = 3, 3, 2, 1
# board = [[2, 1, 0], [1, 0, 1], [2,1,2]]

# N, M, G, R = 6, 6, 3, 3
# board = [[1,1,2,1,1,2],[2,1,0,1,1,1],[0,1,0,0,1,2],[2,1,1,1,2,1],[2,1,1,2,1,2],[0,0,0,0,2,1]]

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = set()

GR_location = get_possible_location(board)
lst_G = []
visited_G = [[0 for _ in range(M)] for _ in range(N)]
lst_R = []
visited_R = [[0 for _ in range(M)] for _ in range(N)]

back_tracking(board, G, lst_G, visited_G, R, lst_R, visited_R, GR_location)

print(max(answer))