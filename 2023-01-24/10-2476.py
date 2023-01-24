import sys
N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

prizes = []

for x in lst:
    if x[0] == x[1] == x[2]:
        money = 10000 + x[0] * 1000
        prizes.append(money)
    
    elif x[0] == x[1] or x[0] == x[2]:
        money = 1000 + x[0] * 100
        prizes.append(money)
    
    elif x[1] == x[2]:
        money = 1000 + x[1] * 100
        prizes.append(money)
    
    else:
        money = max(x) * 100
        prizes.append(money)
    
max_prize = max(prizes)

print(max_prize)
