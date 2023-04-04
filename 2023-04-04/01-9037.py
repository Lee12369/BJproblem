import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    candy = list(map(int, input().split()))
    
    cnt = 0
    M = len(candy)
    while True:    
        max_candy = 0
        min_candy = 30
        pass_candy = [0 for _ in range(M)]
        for i in range(M):
            if candy[i] % 2 == 1:
                candy[i] += 1

            max_candy = max(max_candy, candy[i])
            min_candy = min(min_candy, candy[i])
            pass_candy[i] = candy[i] // 2

        if max_candy == min_candy:
            print(cnt)
            break

        for i in range(M):
            candy[i] //= 2
            candy[i] += pass_candy[i - 1]
        
        cnt += 1
    