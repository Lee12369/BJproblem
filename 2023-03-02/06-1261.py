import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = int(1e9)
break_cnt = [[INF for _ in range(N)] for _ in range(M)]

def djikstra(N, M):
    q = []
    heapq.heappush(q, (0, 0, 0))
    break_cnt[0][0] = 0

    while q:
        cnt, x, y = heapq.heappop(q)

        if break_cnt[x][y] < cnt:
            continue

        for i in range(4):
            cost = break_cnt[x][y]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == '1':
                    cost += 1
                
                if cost < break_cnt[nx][ny]: 
                    break_cnt[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    return break_cnt[M - 1][N - 1]

ans = djikstra(N, M)

if ans >= INF:
    ans = -1

print(ans)