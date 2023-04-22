N, M = map(int, input().split())
basket = [i for i in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    temp = basket.copy()
    for i in range(start, end + 1):
        basket[i] = temp[end + start - i]

for i in range(1, N + 1):
    print(basket[i], end=' ') 