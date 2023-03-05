from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_house = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken_house.append((i,j)) 

total_dist = int(1e9)
for chicken_lst in combinations(chicken_house, M):
    sum_dist = 0
    for house_tpl in house:
        house_x, house_y = house_tpl

        min_dist = int(1e6)
        for tpl in chicken_lst:
            chicken_x, chicken_y = tpl
            dist = abs(house_x - chicken_x) + abs(house_y - chicken_y)
            min_dist = min(min_dist, dist)
        sum_dist += min_dist

    total_dist = min(total_dist, sum_dist)

print(total_dist)
