N = list(map(int, input()))

N.sort(reverse=True)
M = sum(N)
if M % 3 == 0 and 0 in N:
    for x in N:
        print(x, end='')
else:
    print(-1)