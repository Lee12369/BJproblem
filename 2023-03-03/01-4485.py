import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def djikstra(arr):
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    distance = [[INF for _ in range(N)] for _ in range(N)]
    
    distance[0][0] = arr[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + arr[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance[N - 1][N - 1]

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans = djikstra(arr)

    print("Problem {}: {}".format(cnt, ans))

    cnt += 1