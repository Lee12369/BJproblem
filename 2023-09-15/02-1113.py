from collections import deque

def bfs(i, j, num, board, visited, bfs_visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    update_visited = [row[:] for row in visited]
    update_visited[i][j] = 1
    bfs_visited[i][j] = 1

    queue = deque()
    queue.append((i, j))

    cnt = num - board[i][j]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and update_visited[nx][ny] == 0:
                update_visited[nx][ny] = 1
                bfs_visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += num - board[nx][ny]
    
    return cnt, update_visited

# 수영장에 물을 채울 수 있는지 확인한다. 조건은 가장 바깥에 방문기록이 있다면 물이 빠져나가기에 물을 채울 수 없다.
def possible_fill_water(visited, update_visited):
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                # 처음엔 빠져나간 흔적이 없으나 탐색과정에서 빠져나갔다면 False를 반환한다.
                if visited[i][j] == 0 and update_visited[i][j] == 1:
                    return False
    return True

# num 높이로 채울 수 있는 공간이 있는지 확인하는 과정
def main(num, board, visited):
    sum_cnt = 0
    # bfs과정에서 탐색이 완료된 지점을 기록해서 시간을 단축
    bfs_visited = [row[:] for row in visited]
    for i in range(N):
        for j in range(M):
            if bfs_visited[i][j] == 0:
                cnt, update_visited = bfs(i, j, num, board, visited, bfs_visited)
                # 물이 빠져나갔다면 수영장을 채울 수 없기에 건너띈다.
                if not possible_fill_water(visited, update_visited):
                    continue
                
                # 물이 빠져나가지 않았다면 채울 수 있는 물의 양과 방문기록을 업데이트한다.
                visited = update_visited
                sum_cnt += cnt
    return visited, sum_cnt

# N, M = 3, 5
# board = [[1, 6, 6, 6, 1],[6, 1, 1, 1, 6], [1, 6, 6, 6, 1]]
# visited = [[0 for _ in range(M)] for _ in range(N)]

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

water = 0
for num in range(9, 0, -1):
    # 높은 수부터 차례대로 탐색과정에서 제외한다. 쉽게 생각하면 벽을 만든다고 생각해도 좋을 듯 하다. 
    for i in range(N):
        for j in range(M):
            if board[i][j] == num:  
                visited[i][j] = 1
    # num 높이로 채울 수 있는 공간이 있는지 확인하는 과정
    visited, sum_cnt = main(num, board, visited)
    water += sum_cnt

print(water)
        