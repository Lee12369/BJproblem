N = int(input())

lst = [list(map(int,input().split())) for i in range(N)]

curr = 1
for i in range(N):
    if lst[i][0] == curr:
        curr = lst[i][1]
    
    elif lst[i][1] == curr:
        curr = lst[i][0]

print(curr)
