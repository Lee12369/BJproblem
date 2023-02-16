import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end_time = arr[0][0]
for lst in arr:
    if lst[0] >= end_time:   
        end_time = lst[1]
        cnt += 1

print(cnt)
