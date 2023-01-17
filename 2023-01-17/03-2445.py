N = int(input())
M = N * 2 -1
j = N * 2
k = 0
for i in range(M):
    if i <= N-1:
        k += 1
        j -= 2
    else :
        k -= 1
        j += 2
    
    for _ in range(k):
        print('*', end='')
    
    for _ in range(j):
        print(' ', end='')
    
    for _ in range(k):
        print('*',end='')
    print()