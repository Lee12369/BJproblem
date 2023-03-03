import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

start, end = map(int, input().split())

INF = int(1e9)
distance = [INF for _ in range(n + 1)]
root = [[] for _ in range(n + 1)]

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    root[start].append(start)

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                root[i[0]] = root[now] + [i[0]]
                
djikstra(start)

print(distance[end])
print(len(root[end]))
for x in root[end]:
    print(x, end=' ')