N = int(input())
M = N * 2 -1
star_n = -1
empty_change = 0
for i in range(M):
    if i <= N-1:
        star_n += 2
        empty_change += 1
    else :
        star_n -= 2
        empty_change -= 1
    
    for _ in range(N-empty_change):
        print(' ',end='')
    for _ in range(star_n):
        print('*',end='')
    
    print()