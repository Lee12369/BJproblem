import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [i for i in range(N + 1)]

for _ in range(M):
    begin, end, mid = map(int, input().split())
    rotate_basket = basket[begin: end + 1]
    
    curr = mid - begin
    for i in range(begin, end + 1):
        basket[i] = rotate_basket[curr]
        curr += 1
        if curr >= len(rotate_basket):
            curr -= len(rotate_basket)

for i in range(1, N + 1):
    print(basket[i], end=' ')