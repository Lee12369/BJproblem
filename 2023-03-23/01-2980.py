N, L = map(int, input().split())

road = [0 for _ in range(L + 1)]
for _ in range(N):
    D, R, G = map(int, input().split())
    road[D] = (R, G)

time = 0
curr = 0
while curr < L:
    if road[curr + 1] == 0:
        curr += 1
    
    else:
        R, G = road[curr + 1]
        rem = time % (R + G)
        if rem >= R:
            curr += 1

    if curr == L:
        break

    time += 1
    
print(time)