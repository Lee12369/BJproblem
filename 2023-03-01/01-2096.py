import sys
input = sys.stdin.readline

N = int(input())

dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for i in range(N):
    x, y, z = map(int, input().split())
    x_max = x + max(dp_max[0], dp_max[1])
    y_max = y + max(dp_max)
    z_max = z + max(dp_max[1], dp_max[2])

    dp_max = [x_max, y_max, z_max]

    x_min = x + min(dp_min[0], dp_min[1])
    y_min = y + min(dp_min)
    z_min = z + min(dp_min[1], dp_min[2])

    dp_min = [x_min, y_min, z_min]

max_score = max(dp_max)
min_score = min(dp_min)
    
print(max_score, min_score)