def recurr(arr, x, y, n):
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                check = -1
                break

    if check == -1:
        n //= 2
        print("(", end='')
        recurr(arr, x, y, n)
        recurr(arr, x, y + n, n)
        recurr(arr, x + n, y, n)
        recurr(arr, x + n, y + n, n)
        print(")", end='')
    elif check == 0:
        print(0, end='')

    elif check == 1:
        print(1, end='')

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

recurr(arr, 0, 0, N)
