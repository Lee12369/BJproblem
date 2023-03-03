import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]

def djikstra(N):
    q = []
    heapq.heappush(q, (0, 0, 0))
    
    INF = int(1e9)
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == '0':
                    cost = dist + 1
                else:
                    cost = dist
                
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    
    return distance[N - 1][N - 1]  

ans = djikstra(N)

print(ans)