N = int(input())

for i in range(1, N + 1):
    if i % 2 == 0:
        print(' ', end='')
    
    for _ in range(N):
        print('*', end=' ')
    
    print()
