from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

# color에 따라 사이즈별로 각 인덱스에 저장
# 공의 정보를 저장
balls = []
for _ in range(N):
    color, size = map(int, input().split())
    balls.append((color, size))

balls_size = [0 for _ in range(2001)]
balls_color = defaultdict(list)
for ball in balls:
    color, size = ball
    balls_size[size] += size
    balls_color[color].append(size)

for key in balls_color.keys():
    balls_color[key].sort()

# 크기 단위로 누적합
sum_balls_size = [0 for _ in range(2001)]
for i in range(1, 2001):
    sum_balls_size[i] = sum_balls_size[i - 1] + balls_size[i] 

# color 단위로 누적합을 진행
sum_balls_color = defaultdict(list)
for color in range(1, N + 1):
    for idx, val in enumerate(balls_color[color]):
        if idx == 0:
            sum_balls_color[color].append(balls_color[color][0])
            continue
        
        result = sum_balls_color[color][idx - 1] + balls_color[color][idx]
        sum_balls_color[color].append(result)
        

def two_pointer(target, color):
    left = 0
    right = len(balls_color[color]) - 1 
    while True:
        mid = (left + right) // 2
        if mid == left:
            if balls_color[color][right] == target:
                return right
            return left

        size = balls_color[color][mid]
        if target < size:
            right = mid
        elif target >= size:
            left = mid

for ball in balls:
    color, size = ball
    idx = two_pointer(size, color)
    ans = sum_balls_size[size - 1] - sum_balls_color[color][idx - 1]
    if idx == 0 or sum_balls_color[color][idx] == sum_balls_color[color][0]:
        ans = sum_balls_size[size - 1]
    
    print(ans)
