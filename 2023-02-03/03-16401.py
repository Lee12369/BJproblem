import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip('\n').split())
Length = list(map(int, input().rstrip('\n').split()))

left = 1
right = 10 ** 9 + 1
while True:
    cnt = 0
    mid = (left + right) // 2

    for x in Length:
        cnt += x // mid
    
    if mid == left:
        if cnt >= M:
            print(left)
        else:
            print(0)
        break
    if cnt >= M:
        left = mid
    elif cnt < M:
        right = mid
