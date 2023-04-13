import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))

min_price = prices[0]
max_gain = 0
for i in range(1, N):
    min_price = min(min_price, prices[i])
    gain = prices[i] - min_price

    max_gain = max(max_gain, gain)

print(max_gain)