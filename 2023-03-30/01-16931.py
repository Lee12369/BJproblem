import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 위, 아래 겉넓이.
total_square = N * M * 2

for i in range(N):
    # 서에서 동으로 높이 차 만큼 겉넓이 추가.
    total_square += arr[i][0]
    for j in range(1, M):
        square = arr[i][j] - arr[i][j - 1]
        if square > 0:
            total_square += square

    # 동에서 서로 높이 차 만큼 겉넓이 추가.
    total_square += arr[i][M - 1]
    for j in range(M - 1, 0, -1):
        square = arr[i][j - 1] - arr[i][j]
        if square > 0:
            total_square += square

for j in range(M):
    # 북에서 남으로 높이 차 만큼 겉넓이 추가.
    total_square += arr[0][j]
    for i in range(1, N):
        square = arr[i][j] - arr[i - 1][j]
        if square > 0:
            total_square += square
    
    # 남에서 북으로 높이 차 만큼 겉넓이 추가.
    total_square += arr[N - 1][j]
    for i in range(N - 1, 0, -1):
        square = arr[i - 1][j] - arr[i][j]
        if square > 0:
            total_square += square

print(total_square)