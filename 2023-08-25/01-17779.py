from collections import deque
import sys
input = sys.stdin.readline


def get_gap(x, y):
    for d1 in range(1, N):
        for d2 in range(1, N):
            vertex = [(x, y), (x + d1, y - d1), (x + d2, y + d2), (x + d1 + d2, y - d1 + d2)]
            if not check_vertex(vertex):
                continue
            
            visited = [[0 for _ in range(N)] for _ in range(N)]
            visited[0][0] = 1
            visited[0][-1] = 2
            visited[-1][0] = 3
            visited[-1][-1] = 4

            make_boundary(visited, vertex, x, y, d1, d2)

            gap = get_area(visited)
            answer.append(gap)

def check_vertex(vertex):
    for point in vertex:
        nx, ny = point
        if not (0 <= nx < N and 0 <= ny < N):
                return False
    return True

def make_boundary5(visited, x, y, d1, d2):
    for i in range(d1 + 1):
        visited[x + i][y - i] = 5
        visited[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1):
        visited[x + i][y + i] = 5
        visited[x + d1 + i][y - d1 + i] = 5
            
def make_boundary1(visited, up_vertex):
    up_i, up_j = up_vertex 
    for i in range(up_i):
         visited[i][up_j] = -1

def make_boundary2(visited, right_vertex):
    right_i, right_j = right_vertex 
    for j in range(right_j + 1, N):
         visited[right_i][j] = -2

def make_boundary3(visited, left_vertex):
    left_i, left_j = left_vertex 
    for j in range(left_j):
         visited[left_i][j] = -3

def make_boundary4(visited, down_vertex):
    down_i, down_j = down_vertex 
    for i in range(down_i + 1, N):
         visited[i][down_j] = -4

def make_boundary(visited, vertex, x, y, d1, d2):
    up_vertex, left_vertex, right_vertex, down_vertex = vertex

    make_boundary1(visited, up_vertex)
    make_boundary2(visited, right_vertex)
    make_boundary3(visited, left_vertex)
    make_boundary4(visited, down_vertex)
    make_boundary5(visited, x, y, d1, d2)

def get_sum_area_number(number, visited):
    targets = {
        1 : (0, 0),
        2 : (0, N - 1),
        3 : (N - 1, 0),
        4 : (N - 1, N - 1) 
    }
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    x, y = targets[number]
    queue = deque()
    queue.append((x, y))

    area = board[x][y]
    while queue:
        x, y = queue.popleft()          
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = number
                    area += board[nx][ny]
                    queue.append((nx, ny))
                elif visited[nx][ny] == -number:
                    visited[nx][ny] = number
                    area += board[nx][ny]
    return area

def get_area(visited):
    area1 = get_sum_area_number(1, visited)
    area2 = get_sum_area_number(2, visited)
    area3 = get_sum_area_number(3, visited)
    area4 = get_sum_area_number(4, visited)
    area5 = total_areas - (area1 + area2 + area3 + area4)

    areas = [area1, area2, area3, area4, area5]

    min_area = min(areas)
    max_area = max(areas)    
    gap = max_area - min_area

    return gap

# N = 6
# board = [[1,2,3,4,1,6],[7,8,9,1,4,2],[2,3,4,1,1,3],[6,6,6,6,9,4],[9,1,9,1,9,5],[1,1,1,1,9,9]]

# N = 6
# board = [[5,5,5,5,5,5],[5,5,5,5,5,5],[5,5,5,5,5,5],[5,5,5,5,5,5],[5,5,5,5,5,5],[5,5,5,5,5,5]]

# N = 8
# board = [[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,1],[4,5,6,7,8,9,1,2],[5,6,7,8,9,1,2,3],[6,7,8,9,1,2,3,4],[7,8,9,1,2,3,4,5],[8,9,1,2,3,4,5,6]]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

total_areas = 0 
for nums in board:
     total_areas += sum(nums)

answer = []
for i in range(N):
    for j in range(N):
        get_gap(i, j)

ans = min(answer)
print(ans)