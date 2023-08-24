from collections import deque, defaultdict
import sys, copy
input = sys.stdin.readline

def get_starting(board, visited):
    bridge_length = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                starting_point = (i, j, bridge_length)
                return starting_point

# 땅을 기준으로 근처에 바다가 있다면 다리를 놓았을 때 그 끝에 육지가 있는지 확인하고 있다면 반대편 육지의 좌표와 다리의 길이를 points에 저장한다.
def find_points(x, y):
    points = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 육지 주위에 바다가 있는지 확인
        bridge_length = 0
        while 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                nx += dx[i]
                ny += dy[i]
                bridge_length += 1

            elif board[nx][ny] == 1:
                # 방문한 적이 있거나 다리 길이가 1이면 반복문에서 빠져나온다.
                if bridge_length <= 1:
                    break
                points.append((nx, ny, bridge_length))    
                break
    return points

# starting point 와 연결된 영역을 전부 저장한다.
def get_land_near_sea(x, y, visited):
    new_visited = [lst[:] for lst in visited]
    lands = [(x, y)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    new_visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                if new_visited[nx][ny] == 0:
                    new_visited[nx][ny] = 1
                    lands.append((nx, ny))
                    queue.append((nx, ny))
    
    return lands

def bfs(x, y, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return visited

def back_tracking(start_i, start_j, points, visited, total_bridge):
    lands = get_land_near_sea(start_i, start_j, visited)
    visited = bfs(start_i, start_j, visited)
    
    # 새로운 땅 전체 기준에서 다리를 놓을 수 있는 point를 얻어 기존의 points에 추가한다. 즉, 다리로 이어진 영역 전체의 point를 얻을 수 있다.
    for land in lands:
        land_i, land_j = land
        add_points = find_points(land_i, land_j)
        points.extend(add_points)


    # queue를 사용해서 다리 끝에 위치한 땅을 방문한 적이 있다면 버리고 방문한 적이 없다면 다리를 놓은 경우에 대해 다시 탐색한다.
    T = len(points)
    while T > 0:
        depart_i, depart_j, bridge = points.popleft()     
        # 다리를 놓았을 때 방문한 적이 없다면
        if visited[depart_i][depart_j] == 0:
            new_points = deque(points)
            new_visited = [lst[:] for lst in visited]

            back_tracking(depart_i, depart_j, new_points, new_visited, total_bridge + bridge)

            # 이 다리를 먼저 설치하지 않고 다른 경우를 탐색하고 설치할 수도 있기 때문에
            points.append((depart_i, depart_j, bridge))
        T -= 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                return
            
    answer.append(total_bridge)
    return

# N, M = 7, 8
# board = [[0,0,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,0,0],[1,1,0,0,0,1,1,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]]

# N, M = 7, 8
# board = [[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]]

# N, M = 7, 8
# board = [[1,0,0,1,1,1,0,0],[0,0,1,0,0,0,1,1],[0,0,1,0,0,0,1,1],[0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0],[1,1,1,1,1,1,0,0]]

# N, M = 7, 7
# board = [[1,1,1,0,1,1,1], [1,1,1,0,1,1,1], [1,1,1,0,1,1,1], [0,0,0,0,0,0,0], [1,1,1,0,1,1,1],[1,1,1,0,1,1,1],[1,1,1,0,1,1,1]]

answer = []

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

starting_point = get_starting(board, visited)
start_i, start_j, bridge = starting_point

back_tracking(start_i, start_j, deque(), visited, bridge)

if answer:
    ans = min(answer)
    print(ans)
else:
    print(-1)