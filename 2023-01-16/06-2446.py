N = int(input())
M = N * 2 - 1
n = 0
for i in range(M):
    for _ in range(n):
        print(' ', end='')
    for _ in range(M):
        print('*', end='')
    print()

    if i < N-1:
        n += 1
        M -= 2
        
    else:
        n -= 1 
        M += 2
        
    