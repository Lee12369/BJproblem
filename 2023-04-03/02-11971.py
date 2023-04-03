import sys
input = sys.stdin.readline

N, M = map(int, input().split())
road = [[0, 0] for _ in range(101)]

# 전체 도로의 제한 속도
start = 1
for _ in range(N):
    dist, limit_speed = map(int, input().split())
    end = start + dist
    for i in range(start, end):
        road[i][0] = limit_speed
    start += dist
    
# 전체 도로의 운행 속도
start = 1
for _ in range(M):
    dist, car_speed = map(int, input().split())
    end = start + dist
    for i in range(start, end):
        road[i][1] = car_speed
    start += dist

# 운행 속도가 제한 속도보다 높을 경우 속도 위반한 최댓값을 저장
max_over_speed = 0
for i in range(101):
    if road[i][1] > road[i][0]:
        over_speed = road[i][1] - road[i][0]
        max_over_speed = max(max_over_speed, over_speed)

print(max_over_speed)

