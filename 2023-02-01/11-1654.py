import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left = 1
right = 2 ** 31
while True:
    cnt = 0
    mid = (left + right) // 2
    if left == mid:
        break

    for x in lines:
        cnt += x // mid
    
    if cnt < N:
        right = mid
    
    elif cnt >= N:
        left = mid

print(mid)