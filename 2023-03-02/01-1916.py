import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

start, end = map(int, input().split())


INF = int(1e9)
min_costs = [INF for _ in range(N + 1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    min_costs[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if min_costs[now] < cost:
            continue

        for i in graph[now]:
            sum_cost = cost + i[1]
            if sum_cost < min_costs [i[0]]:
                min_costs[i[0]] = sum_cost
                heapq.heappush(q, (sum_cost, i[0]))

dijkstra(start)

ans = min_costs[end]
if ans == INF:
    ans = -1
print(ans)