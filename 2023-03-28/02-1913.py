N = int(input())
M = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

i = (N + 1) // 2 - 1 
j = (N + 1) // 2 - 1
K = (N + 1) // 2

arr[i][j] = 1
curr = 1
for k in range(1, K):
    # 위로 한 칸
    curr += 1
    i -= 1
    arr[i][j] = curr

    # 오른쪽으로 이동
    for _ in range(k * 2 - 1):
        curr += 1
        j += 1
        arr[i][j] = curr

    # 아래로 이동
    for _ in range(k * 2):
        curr += 1
        i += 1
        arr[i][j] = curr

    # 왼쪽으로 이동
    for _ in range(k * 2):
        curr += 1
        j -= 1
        arr[i][j] = curr
    
    # 위로 이동
    for _ in range(k * 2):
        curr += 1
        i -= 1
        arr[i][j] = curr

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        if arr[i][j] == M:
            target_i = i
            target_j = j
    print()

print(target_i + 1, target_j + 1)