import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

INF = int(1e9)
distance = [INF for _ in range(V + 1)]

def djikstra(start):
    q = []
    heapq.heappush(q, (0,start))
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

djikstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])