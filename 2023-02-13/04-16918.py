N, M, T = map(int, input().split())
arr = [input() for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    arr[i] = arr[i].replace('O','2')

for t in range(T):
    if t % 2 == 0:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == '1':
                    arr[i] = arr[i][:j] + '.' + arr[i][j + 1:]    
                    
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != '1':
                            arr[ni] = arr[ni][:nj] + '.' + arr[ni][nj + 1:] 
    elif t % 2 == 1:
        for i in range(N):
            arr[i] = arr[i].replace('2','1')
            arr[i] = arr[i].replace('.','2')
   
   
for i in range(N):
    arr[i] = arr[i].replace('1','O').replace('2','O')

for x in arr:
    print(x)