arr = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
for x in range(101):
    for y in range(101):
        if arr[x][y] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 101 and 0 <= ny < 101 and arr[nx][ny] == 0:
                    cnt += 1
print(cnt)