def recurr(arr, N):
    if N == 1:
        return arr[0][0]
    new_arr = []
    for x in range(0, N, 2):
        lst = []
        for y in range(0, N, 2):
            temp = [arr[i][j] for i in range(x, x + 2) for j in range(y, y + 2)]
            temp.sort(reverse= True)
            lst.append(temp[1])
        new_arr.append(lst)
        
    N //= 2
    answer = recurr(new_arr, N)

    return answer

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = recurr(arr, N)

print(answer)