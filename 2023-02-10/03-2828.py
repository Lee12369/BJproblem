N, M = map(int, input().split())
K = int(input())
apples = [int(input()) for _ in range(K)]

basket = [i for i in range(1, M + 1)]

sum_cnt = 0
for x in apples:
    max_basket = max(basket)
    min_basket = min(basket)
    if x > max_basket:
        cnt = x - max_basket
        sum_cnt += cnt
        for i in range(M):
            basket[i] += cnt
    
    elif x < min_basket:
        cnt = min_basket - x
        sum_cnt += cnt
        for i in range(M):
            basket[i] -= cnt

print(sum_cnt)