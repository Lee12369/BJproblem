import sys
input = sys.stdin.readline

money = int(input())
stocks = list(map(int, input().split()))

BNP_money = int(money)
BNP_stock = 0
Timing_money = int(money)
Timing_stock = 0

# BNP
for i in range(14):
    cnt = BNP_money // stocks[i]
    if cnt > 0:
        BNP_stock += cnt
        BNP_money -= cnt * stocks[i]

BNP_asset = BNP_stock * stocks[-1] + BNP_money

# Timing
for i in range(3, 14):
    if stocks[i] > stocks[i - 1] > stocks[i - 2] > stocks[i - 3]:
        Timing_money += Timing_stock * stocks[i]
        Timing_stock = 0

    elif stocks[i] < stocks[i - 1] < stocks[i - 2] < stocks[i - 3]:
        cnt = Timing_money // stocks[i]
        Timing_stock += cnt
        Timing_money -= cnt * stocks[i]

Timing_asset = Timing_stock * stocks[-1] + Timing_money

if BNP_asset > Timing_asset:
    print("BNP")
elif Timing_asset > BNP_asset:
    print("TIMING")
else:
    print("SAMESAME")
    