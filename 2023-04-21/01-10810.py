N, M = map(int, input().split())
basket = [0 for _ in range(N + 1)]
for _ in range(M):
    start, end, number = map(int, input().split())
    for i in range(start, end + 1):
        basket[i] = number
        
for i in range(1, N + 1):
    print(basket[i], end=' ')
