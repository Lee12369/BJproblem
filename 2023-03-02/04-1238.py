import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

INF = int(1e9)
times = [INF for _ in range(N + 1)]

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    times[start] = 0
    
    while q:
        time, now = heapq.heappop(q)

        if times[now] < time:
            continue

        for i in graph[now]:
            cost = time + i[1]
            if cost < times[i[0]]:
                times[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 

def go(start, X):
    INF = int(1e9)
    times = [INF for _ in range(N + 1)]

    q = []
    heapq.heappush(q, (0, start))
    times[start] = 0
    
    while q:
        time, now = heapq.heappop(q)

        if times[now] < time:
            continue

        for i in graph[now]:
            cost = time + i[1]
            if cost < times[i[0]]:
                times[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 
    
    return times[X]

djikstra(X)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, times[i] + go(i, X))

print(ans)
