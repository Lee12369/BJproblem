import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B_arr = [list(map(int, input().split())) for _ in range(H + X)]

A_arr = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i >= X and j >= Y:
            A_arr[i][j] = B_arr[i][j] - A_arr[i - X][j - Y]
        else:
            A_arr[i][j] = B_arr[i][j]

for lst in A_arr:
    for x in lst:
        print(x, end=' ')
    print()
