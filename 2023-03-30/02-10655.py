import sys
input = sys.stdin.readline

N = int(input())
check_points = [tuple(map(int, input().split())) for _ in range(N)]

# 체크 포인트 구간 별 거리
distances = []
total_distance = 0
for i in range(1, N):
    x1, y1 = check_points[i - 1] 
    x2, y2 = check_points[i]
    dist = abs(x2 - x1) + abs(y2 - y1)

    total_distance += dist
    distances.append(dist)

min_distance = int(total_distance)
for i in range(N - 2):
    # 전체 거리에서 i ~ i + 1, i + 1 ~ i + 2 까지의 구간을 뺀다.
    dist = total_distance - distances[i] - distances[i + 1]
    
    # i ~ i + 2 까지의 직통 거리를 더한다. (i + 1 checkpoint를 건너뛴다.)
    x1, y1 = check_points[i] 
    x2, y2 = check_points[i + 2]
    dist += abs(x2 - x1) + abs(y2 - y1)

    min_distance = min(min_distance, dist)

print(min_distance)