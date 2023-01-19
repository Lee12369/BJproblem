import sys
N, M = map(int, sys.stdin.readline().split())
NxM = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

sum_arr = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_arr[i][j] = NxM[i - 1][j - 1] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]


K = int(input())

    
for _ in range(K):
    i, j, x, y = list(map(int,sys.stdin.readline().split()))

    answer = sum_arr[x][y] + sum_arr[i - 1][j - 1] - sum_arr[i - 1][y] -sum_arr[x][j - 1]
    
    print(answer)
