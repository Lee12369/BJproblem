import sys
T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = [1 for _ in range(N)]
    
    for x in range(1, N + 1):
        M = N // x
        
        for y in range(1, M + 1):
            idx = x * y - 1
            if lst[idx]:
                lst[idx] = 0
            else:
                lst[idx] = 1
    
    answer = lst.count(0)

    print(answer)