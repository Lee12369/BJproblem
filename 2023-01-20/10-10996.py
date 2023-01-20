import math
N = int(input())
for _ in range(N):
    for _ in range(math.ceil(N / 2)):
        print('*', end=' ')
    
    print()
    print(end=' ')
    
    for _ in range(math.floor(N / 2)):
        print('*', end=' ')
    
    print()
