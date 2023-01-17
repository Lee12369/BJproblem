N = int(input())
M = N * 2 -1
for i in range(N):
    for _ in range(i):
        print(' ', end='')
    for _ in range(M):
        print('*',end='')
    
    M -=2
    print()