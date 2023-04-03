N = int(input())
snows = list(map(int, input().split()))
snows.sort(reverse=True)

time = 0
if N > 1:
    max_snow_1 = snows[0]
    max_snow_2 = snows[1]
    while max_snow_1 > 0 and max_snow_2 > 0:
        snows[0] -= 1
        snows[1] -= 1
        snows.sort(reverse=True)
        max_snow_1 = snows[0]
        max_snow_2 = snows[1]
        time += 1
    
    time += max_snow_1 + max_snow_2

elif N == 1:
    time = snows[0]

if time > 1440:
    time = -1

print(time)

    