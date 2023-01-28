import sys
input = sys.stdin.readline

while True: 

    N = int(input())

    if N == -1:
        break

    measure = [i for i in range(1, N) if N % i == 0]
    
    if sum(measure) == N:
        print("{} = ".format(N), end='')
        for x in measure:
            print("{}".format(x), end=' ')
            if x == measure[-1]:
                break
            print("+", end=' ')
    
    else:
        print("{} is NOT perfect.".format(N))
    
