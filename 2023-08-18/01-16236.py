from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 상어의 초기 위치를 찾는다.
def get_shark():
    shark = []
    for i in range(N):
        for j in range(N):
            fish_size = arr[i][j]
            if fish_size == 9:
                shark = (i, j)
                return shark


# 상어를 기준으로 이동할 수 있는 거리 정보를 얻는다.
def get_dist(shark):
    queue = deque()
    queue.append(shark)
    INF = int(1e9)
    distances = [[INF for _ in range(N)] for _ in range(N)]
    distances[shark[0]][shark[1]] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x , y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= shark_size:
                if distances[nx][ny] > (distances[x][y] + 1):
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx,ny))

    distances[shark[0]][shark[1]] = INF

    return distances

# 물고기를 먹으면 발생하는 과정. 시간의 경과부터 위치 변화, 상어 크기 변화, 먹은 횟수 증가
def eat_fish(time, shark_size, shark_eat, shark_location):
    time += min_dist
    shark_eat += 1
    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0

    arr[shark_location[0]][shark_location[1]] = 0
    arr[fish_location[0]][fish_location[1]] = 9
    shark_location = fish_location
    
    return time, shark_size, shark_eat, shark_location



# main
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
shark_size = 2
shark_eat = 0
shark_location = get_shark()
INF = int(1e9)
while True:
    distances = get_dist(shark_location)
    min_dist = INF
    fish_location = (INF,INF)
    # 먹을 수 있는 물고기 중 가장 가까운 위치
    for i in range(N):
        for j in range(N):
            fish_size, dist = arr[i][j], distances[i][j]
            if 0 < fish_size < shark_size and dist < min_dist:
                min_dist = dist
                fish_location = (i, j)

    # 먹을 수 있는 물고기가 없으면 종료 
    if min_dist == INF:
        break

    time, shark_size, shark_eat, shark_location = eat_fish(time, shark_size, shark_eat, shark_location)

# 출력
print(time)