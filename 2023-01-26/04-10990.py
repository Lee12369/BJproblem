N = int(input())

for i in range(N):  
    for _ in range(N - i - 1):
        print(' ',end='')

    print('*', end='')

    if i:
        for _ in range(i * 2 - 1):
            print(' ', end='')

        print('*', end='')
    
    print()