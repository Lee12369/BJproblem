N = int(input())
for i in range(N):
    for j in range(N - i - 1):
        print('',end=' ')
    star_number = i * 2 + 1
    for k in range(star_number):
        print('*', end='')
    print()
