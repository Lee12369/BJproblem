def recurr(arr, N):
    if N == 1:
        if arr[0][0] == 0:
            white += 1
        elif arr[0][0] == 1:
            blue += 1
        return 0
        
    M = N // 2
    cnt = 0
    for i in range(N):
        cnt  += arr[i].count(1)

    if cnt == N ** 2:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        arr_1 = [arr[i][:M] for i in range(M)]
        arr_2 = [arr[i][M:] for i in range(M)]
        arr_3 = [arr[i + M][:M] for i in range(M)]
        arr_4 = [arr[i + M][M:] for i in range(M)]
        return recurr(arr_1, M), recurr(arr_2, M), recurr(arr_3, M), recurr(arr_4, M)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0
recurr(arr, N)

print(white)
print(blue)
