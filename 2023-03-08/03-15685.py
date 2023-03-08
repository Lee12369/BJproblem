import sys
input = sys.stdin.readline

N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)] 

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    move = [d]
    for _ in range(g):
        temp = move.copy()
        for z in move[::-1]:
            next = z + 1
            if next > 3:
                next -= 4
            temp.append(next)
        move = temp.copy()

    arr[x][y] = 1
    for i in move:
        x = x + dx[i]
        y = y + dy[i]
        arr[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
            cnt += 1
print(cnt) 


