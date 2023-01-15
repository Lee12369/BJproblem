# 포기
N = int(input())
lst = [list(map(int, input().split())) for i in range(N)]
temp_w = [lst[i][0] for i in range(N)]
temp_h = [lst[i][1] for i in range(N)]

rank_w = [0 for i in range(N)]
rank_h = [0 for i in range(N)]
cts = 1
for i in range(N):
    max_weight = max(temp_w)
    max_height = max(temp_h)
    max_windex = temp_w.index(max_weight)
    max_hindex = temp_h.index(max_height)
    
    rank_w[max_windex] = cts
    rank_h[max_hindex] = cts
    cts += 1
    
    temp_w[max_windex] = 0
    temp_h[max_hindex] = 0

Rank = [0 for i in range(N)]

for i in range(5):
    if rank_w[i] == rank_h[i]:
        Rank[i] = rank_w[i] 
