N = int(input())
M = N * 2 - 1
for i in range(1, M+1):

    empty_num = abs(N - i)
    for _ in range(empty_num):
        print(' ',end='')

    star_num = abs(N - abs(N - i))
    for _ in range(star_num):
        print('*', end='')

    print()
