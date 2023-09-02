from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

# 공의 정보를 저장
inputs = []
for _ in range(N):
    color, size = map(int, input().split())
    inputs.append((color, size))

# 공의 정보를 복사해서 정렬하는 이유는 딕셔너리의 키값의 순서를 오름차순으로 만들기 위함. 또한 마지막 출력에서는 inputs를 사용하여 기존 순서대로 결과를 출력한다.
balls = inputs[::]
balls.sort()

balls_size = [0 for _ in range(2001)]
balls_color = [defaultdict(int) for _ in range(N + 1)]
for ball in balls:
    color, size = ball
    balls_size[size] += size
    balls_color[color][size] += size

# 크기 단위로 누적합
sum_balls_size = [0 for _ in range(2001)]
for i in range(1, 2001):
    sum_balls_size[i] = sum_balls_size[i - 1] + balls_size[i] 

# color 단위로 누적합을 진행
sum_balls_color = [defaultdict(int) for _ in range(N + 1)]
for color in range(1, N + 1):
    keys = list(balls_color[color].keys())
    if not keys:
        continue
    pre_idx = keys[0]
    sum_balls_color[color][pre_idx] = 0
    for i in range(1, len(keys)):
        idx = keys[i]
        # 보통의 누적합의 경우 현재 자신의 위치의 값을 더해주어야 하지만 이 경우에는 전체적으로 index를 한 칸 씩 뒤로 미뤄서 자신이 포함하지 않도록 한다.
        sum_balls_color[color][idx] = sum_balls_color[color][pre_idx] + balls_color[color][pre_idx]
        pre_idx = idx

for ball in inputs:
    color, size = ball
    # size가 한 단계 작은 ball들의 크기의 합에서 자신과 색깔이 같은 것들 중 size가 작은 것들을 빼주어야 한다.
    # 메모리 문제로 배열이 아닌 딕셔너리로 만들었기에 현재 size보다 작은 것들 중에서 가장 큰 size를 찾아야 하지만 여기서는 sum_balls_color를 만드는 과정에서 index를 뒤로 한 칸씩 미루어서 현재 size를 가리키는 곳에는 현재 size보다 작은 값들의 합이 저장되어 있다.
    # 정리하자면 (현재 크기보다 작은 것들의 총 합 - 색깔이 같은 것들 중 크기가 작은 것들의 합)을 출력하게 된다.
    ans = sum_balls_size[size - 1] - sum_balls_color[color][size]
    print(ans)
