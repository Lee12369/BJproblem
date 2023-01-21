N = int(input())

for i in range(1, N):
    for _ in range(N - i):
        print(' ',end='')
    
    print('*',end='')

    for _ in range(i * 2 -3):
        print(' ',end='')

    if i > 1:
        print('*',end='')
    
    print()

print('*' * (N * 2 - 1))