N = int(input())
for i in range(N):
    print(' '*i, end='')
    for j in range(N-i):
        print('*',end='')
    print()