def get_change(move, arr, N, M):
    if move == 1 or move == 2:
        new_arr = [[0 for _ in range(M)] for _ in range(N)]
        
        if move == 1:
            for i in range(N):
                for j in range(M):
                    new_arr[i][j] = arr[N - 1 - i][j]
        
        elif move == 2:
            for i in range(N):
                for j in range(M):
                    new_arr[i][j] = arr[i][M - 1 - j]

    if move == 3 or move == 4:
        N, M = M, N
        new_arr = [[0 for _ in range(M)] for _ in range(N)]
        if move == 3:
            for i in range(N):
                for j in range(M):
                    new_arr[i][j] = arr[M - 1 - j][i] 
        elif move == 4:
            for i in range(N):
                for j in range(M):
                    new_arr[i][j] = arr[j][N - 1 -i]
    
    if move == 5 or move == 6:
        new_arr = [[0 for _ in range(M)] for _ in range(N)]
        n = N // 2
        m = M // 2
        if move == 5:
            for i in range(0, n):
                for j in range(0, m):
                    new_arr[i][j] = arr[i + n][j]
                    
            for i in range(0, n):
                for j in range(m, m * 2):
                    new_arr[i][j] = arr[i][j - m]

            for i in range(n, n * 2):
                for j in range(m, m * 2):
                    new_arr[i][j] = arr[i - n][j]

            for i in range(n, n * 2):
                for j in range(0, m):
                    new_arr[i][j] = arr[i][j + m]

        if move == 6:
            for i in range(0, n):
                for j in range(0, m):
                    new_arr[i][j] = arr[i][j + m]
                    
            for i in range(0, n):
                for j in range(m, m * 2):
                    new_arr[i][j] = arr[i + n][j]

            for i in range(n, n * 2):
                for j in range(m, m * 2):
                    new_arr[i][j] = arr[i][j - m]

            for i in range(n, n * 2):
                for j in range(0, m):
                    new_arr[i][j] = arr[i - n][j]
                    
    return new_arr, N, M

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
nums = list(map(int, input().split()))

for x in nums:
    arr, N, M = get_change(x, arr, N, M)
    
for lst in arr:
    for x in lst:
        print(x, end= ' ')
    print()