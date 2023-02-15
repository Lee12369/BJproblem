N = int(input())
dic = {}
for _ in range(N):
    a, b, c = map(int, input().split())
    dic[(a,b)] = c

lst = list(dic.items())
lst.sort(key = lambda x : -x[1])

rank = [lst[i][0] for i in range(N)]

gold_x, gold_y = rank[0][0], rank[0][1]
silv_x, silv_y = rank[1][0], rank[1][1]
brz_x, brz_y = rank[2][0], rank[2][1]


if gold_x == silv_x:
    i = 2
    while i < N and  rank[i][0] == gold_x:
            i += 1
    
    brz_x, brz_y = rank[i][0], rank[i][1]


print(gold_x, gold_y)
print(silv_x, silv_y)
print(brz_x, brz_y)        