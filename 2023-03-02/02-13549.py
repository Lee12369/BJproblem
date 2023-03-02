import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())

INF = int(1e9) 
min_times = [INF for _ in range(200001)]

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    min_times[start] = 0

    
    while q:
        time, now = heapq.heappop(q)
        if min_times[now] < time:
            continue
        
        dnow = [1, -1, now]
        dtime = [1, 1, 0]

        for i in range(3):
            inow = now + dnow[i]
            itime = time + dtime[i]

            if 0 <= inow < 200001 and min_times[inow] > itime:
                min_times[inow] = itime
                heapq.heappush(q, (itime, inow))

djikstra(N)

ans = min_times[M]

print(ans)