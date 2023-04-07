import sys
input = sys.stdin.readline

R, C = map(int, input().split())
lst = [input() for _ in range(R)]

cnt_lst = [0 for _ in range(10)]
for word in lst:
    cnt = 0
    for i in range(1, C):
        if word[i] == '.':
            cnt += 1
        
        elif word[i].isnumeric():
            cnt_lst[int(word[i])] = cnt
            break

lst_rank = [0 for _ in range(10)]
for i in range(1, 10):
    rank = set()
    for x in cnt_lst:
        if x >= cnt_lst[i]:
            rank.add(x)
    
    lst_rank[i] = len(rank)

for i in range(1, 10):
    print(lst_rank[i])

