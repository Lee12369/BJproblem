from collections import defaultdict, deque
import sys
input = sys.stdin.readline

           
def get_heaters_checkPoints(board):
    heaters = defaultdict(list)
    check_points = []
    for i in range(R):
        for j in range(C):
            num = board[i][j]
            if 0 < num <= 4:
                # 히터 바로 앞의 위치를 저장. 이후 히터를 작동시킬 때 히터 앞을 기준으로 작동.
                heaters[board[i][j]].append((i + heater_dx[num][1][0], j + heater_dy[num][1][0]))
            if num == 5:
                check_points.append((i, j))
    return heaters, check_points

# 벽에 부딕히는지 확인
def block_wall(x, y , dx, dy):
    curr_x = int(x)
    curr_y = int(y)
    for j in range(len(dx)):
        nx = curr_x + dx[j]
        ny = curr_y + dy[j]
        # 벽이 있거나 범위를 벗어나면 종료
        if walls[(curr_x, curr_y, nx, ny)] == True or walls[(nx, ny, curr_x, curr_y)] == True or not (0 <= nx < R and 0 <= ny < C):
            return True, nx, ny
        curr_x = int(nx)
        curr_y = int(ny)

    return False, nx, ny

# 히터를 작동시켰을 때 올라가는 온도
def spread_heater(heaters):
    up_tempers = [[0 for _ in range(C)] for _ in range(R)]
    for num in heaters.keys():
        arr_dx = heater_dx[num]
        arr_dy = heater_dy[num]
        for heater in heaters[num]:
            x, y = heater
            queue = deque()
            queue.append((x, y))
            # 히터 앞은 5이다.
            up_tempers[x][y] += 5
            visited = [[0 for _ in range(C)] for _ in range(R)]
            # 다음은 4부터
            up_temper = 4
            while queue:
                # 올라갈 온도가 0이면 종료
                if up_temper == 0:
                    break
                N = len(queue)
                for _ in range(N):
                    x, y = queue.popleft()
                    for i in range(3):
                        dx = arr_dx[i]
                        dy = arr_dy[i]
                        block, nx, ny = block_wall(x, y, dx, dy)
                        # 벽에 부딪히거나 방문한 적이 있으면 건너띈다.
                        if block == True or visited[nx][ny] == 1:
                            continue
                        
                        up_tempers[nx][ny] += up_temper
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                up_temper -= 1
    return up_tempers

def spread_temperature(temperatures):
    change_temperature = [[0 for _ in range(C)] for _ in range(R)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(R):
        for j in range(C):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < R and 0 <= ny < C and temperatures[i][j] > temperatures[nx][ny]:
                    # 벽에 부딕히지 않을 경우 진행
                    if walls[(i, j, nx, ny)] == False and walls[(nx, ny, i, j)] == False:
                        temper = (temperatures[i][j] - temperatures[nx][ny]) // 4
                        change_temperature[i][j] -= temper
                        change_temperature[nx][ny] += temper
    # 변화된 온도 적용
    for i in range(R):
        for j in range(C):
            temperatures[i][j] += change_temperature[i][j]

# 외곽 온도 감소. 모서리 4부분에 중복 감소되지 않도록 주의할 것
def down_temperature(temperatures):
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                if temperatures[i][j] > 0:
                    temperatures[i][j] -= 1

# 특정 지점 온도 확인.
def check_temperature(temperatures, check_points):
    for point in check_points:
        x, y = point
        if temperatures[x][y] < K:
            return False
    return True

# R, C, K = 7, 8, 1000
# board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 5, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0]]
# W = 3
# walls = defaultdict(bool)
# inputs = [[4, 4, 1], [5, 4, 0], [5, 6, 0]]
# for i in range(W):
#     dx = [-1, 0]
#     dy = [0, 1]
#     x, y, direct = inputs[i]
#     nx = x + dx[direct]
#     ny = y + dy[direct]
#     walls[(x - 1, y - 1, nx - 1, ny - 1)] = True
#     walls[(nx - 1, ny - 1, x - 1, y - 1)] = True

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = defaultdict(bool)
for _ in range(W):
    dx = [-1, 0]
    dy = [0, 1]
    x, y, direct = map(int, input().split())
    nx = x + dx[direct]
    ny = y + dy[direct]
    walls[(x - 1, y - 1, nx - 1, ny - 1)] = True
    walls[(nx - 1, ny - 1, x - 1, y - 1)] = True

heater_dx = {
    1 : [[-1, 0], [0], [1, 0]],
    2 : [[-1, 0], [0], [1, 0]],
    3 : [[0, -1], [-1], [0, -1]],
    4 : [[0, 1], [1], [0, 1]]
}
heater_dy = {
    1 : [[0, 1], [1], [0, 1]],
    2 : [[0, -1], [-1], [0, -1]],
    3 : [[-1, 0], [0], [1, 0]],
    4 : [[-1, 0], [0], [1, 0]]
}

# heater와 체크포인트 위치 저장
heaters, check_points = get_heaters_checkPoints(board)
temperatures = [[0 for _ in range(C)] for _ in range(R)]

# 온풍기 작동시 올라가는 온도 저장
up_tempers = spread_heater(heaters)
ans = 0
while ans <= 100:
    # 온풍기에서 바람
    for i in range(R):
        for j in range(C):
            temperatures[i][j] += up_tempers[i][j]

    # 온도 조절
    spread_temperature(temperatures)
    
    # 온도가 1이상인 바깥온도 1씩 감소
    down_temperature(temperatures)

    # 초콜릿 하나 먹는다.
    ans += 1

    # 조사하는 모든 칸의 온도가 K 이상인지 확인
    if check_temperature(temperatures, check_points):
        break
    
if ans > 100:
    ans = 101

print(ans)
