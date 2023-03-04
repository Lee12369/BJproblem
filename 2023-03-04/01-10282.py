import sys, heapq
input = sys.stdin.readline

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))

    INF = int(1e9)
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    cnt = 0
    max_cost = 0
    for x in distance:
        if x < INF:
            cnt += 1
            max_cost = max(max_cost, x)

    return cnt, max_cost

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    cnt, max_time = djikstra(c)

    print(cnt, max_time)

    