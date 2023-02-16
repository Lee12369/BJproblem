N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
total = 0
for i in range(N - 1):
    if prices[i] <= min_price:
        total += prices[i] * roads[i]
        min_price = prices[i]

    else:
        total += min_price * roads[i]

print(total)