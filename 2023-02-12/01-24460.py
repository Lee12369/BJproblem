def recurr(arr, n):
    if n == 1:
        return arr[0][0]

    new_arr = []
    for x in range(0, n, 2):
        lst = []
        for y in range(0, n, 2):
            temp = [arr[i][j] for i in range(x, x + 2) for j in range(y, y + 2)]
            temp.sort()
            lst.append(temp[1])
        new_arr.append(lst)
    
    n //= 2
    return recurr(new_arr, n)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = recurr(arr, N)

print(answer)

