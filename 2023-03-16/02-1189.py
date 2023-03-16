import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dist = 1
visited = [[0 for _ in range(C)] for _ in range(R)]
ans_lst = []
def back_tracking(x, y, dist, visited):
    if dist == K and x == 0 and y == C - 1:
        ans_lst.append((x, y))
        return 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]              
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == '.':
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                save_dist = dist + 1

                back_tracking(nx, ny, save_dist, visited)

                visited[nx][ny] = 0

visited[R - 1][0] = 1                 
back_tracking(R - 1, 0, dist, visited)

ans = len(ans_lst)

print(ans)