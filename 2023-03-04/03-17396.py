import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
search = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

INF = int(1e10) + 1
def djikstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    
    distance = [INF for _ in range(N)]
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if (search[i[0]] == 0 or i[0] == N - 1) and distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance[N - 1]

ans = djikstra(0)
if ans == INF:
    ans = -1

print(ans)
    