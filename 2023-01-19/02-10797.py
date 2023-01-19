N = int(input())
M = list(map(int, input().split()))

cts = 0
for x in M:
    if x == N:
        cts += 1

print(cts)
