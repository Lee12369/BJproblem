import sys, heapq
input = sys.stdin.readline

N, M, R = map(int, input().split())
item = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(R):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))


def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    
    INF = int(1e9)
    distance = [INF for _ in range(N + 1)]
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
    sum = 0
    for i in range(1, N + 1):
        if distance[i] <= M:
            sum += item[i]

    return sum

max_ans = 0
for i in range(1, N + 1):
    ans = djikstra(i)
    max_ans = max(max_ans, ans)

print(max_ans)