N = list(map(int, input()))
M = len(N) // 2
left = N[:M]
right = N[M:]

if sum(left) == sum(right):
    print("LUCKY")

else:
    print("READY")