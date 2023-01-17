N = int(input())
M = N * 2 - 1
K = 0
for i in range(M):
    if i <= N-1:
        K += 1
    else :
        K -= 1

    for _ in range(K):
        print('*', end='')
    print()