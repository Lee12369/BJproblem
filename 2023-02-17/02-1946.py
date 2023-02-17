import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    
    apply = []
    passers = []
    pass_or_fail = [1 for _ in range(N + 1)]
    pass_or_fail[0] = 0
    
    for _ in range(N):
        a, b = map(int, input().split())
        apply.append([a, b])
        if a == 1 or b == 1:
            passers.append([a, b])
    
    for x in passers:
        for y in apply:
            if x[0] < y[0] and x[1] < y[1]:
                pass_or_fail[y[0]] = 0
    
    ans = pass_or_fail.count(1)

    print(ans)

    

