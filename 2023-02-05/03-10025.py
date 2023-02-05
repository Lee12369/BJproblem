import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip('\n').split())

arr = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

max_num = 0
min_num = 10000
for i in range(N):
    if arr[i][1] > max_num:
        max_num = arr[i][1]

    if arr[i][1] < min_num:
        min_num = arr[i][1]

x_line = [0 for _ in range(max_num + 1)]
for i in range(N):
    x_line[arr[i][1]] = arr[i][0]

size = 2 * K + 1
start = min_num + K
end = max_num - K
pre = sum(x_line[min_num: min_num + size])
max_sum = pre

for i in range(start + 1, end + 1):
    curr = pre - x_line[i - K - 1] + x_line[i + K]
    if curr > max_sum:
        max_sum = curr
    pre = curr

print(max_sum)