import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
v1, v2 = map(int, input().split())

INF = int(1e9)
    

def djikstra(start, end):
    distance = [INF for _ in range(N + 1)]

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1] 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[end]

ans = djikstra(v1, v2) + min(djikstra(1, v1) + djikstra(v2, N), djikstra(1, v2) + djikstra(v1, N))

if ans >= INF:
    ans = -1

print(ans)