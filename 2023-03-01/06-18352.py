from heapq import *
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

INF = int(1e9)
distance = [INF for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

dijkstra(X)

check = 0
for city, dist in enumerate(distance):
    if dist == K:
        check = 1
        print(city)

if check == 0:
    print(-1)