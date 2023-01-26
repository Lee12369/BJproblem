N = int(input())
arr = [list(input()) for _ in range(N)]

def row():
    cnt = max_cnt = 1

    for i in range(N):
        for j in range(N - 1):
            if arr[i][j] == arr[i][j + 1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt = 1

    return max_cnt

def column():
    cnt = max_cnt = 1

    for i in range(N):
        for j in range(N - 1):
            if arr[j][i] == arr[j + 1][i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt = 1

    return max_cnt



max_num = 0
for i in range(N):
    for j in range(N - 1):
        if arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            
            max_num = max(row(),column(),max_num)
    
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

for i in range(N - 1):
    for j in range(N):
        if arr[i][j] != arr[i + 1][j]:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            
            max_num = max(row(),column(),max_num)
    
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(max_num)