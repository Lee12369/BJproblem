import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

def djikstra(start):
    q = []
    heapq.heappush(q, (start, 0))

    INF = int(1e9)
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance[N]

ans = djikstra(1)

print(ans)
    