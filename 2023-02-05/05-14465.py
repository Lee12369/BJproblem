import sys
input = sys.stdin.readline
N, K, B = map(int, input().rstrip('\n').split())
broken_light = [int(input()) for _ in range(B)]

all_light = [1 for _ in range(N)]

for x in broken_light:
    all_light[x - 1] = 0

pre = sum(all_light[:K])
max_light = pre

for i in range(K, N):
    curr = pre - all_light[i - K] + all_light[i]
    max_light = max(max_light, curr)
    pre = curr

if max_light >= K:
    answer = 0
else:
    answer = K - max_light

print(answer)