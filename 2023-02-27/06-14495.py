N = int(input())

fibb = [1 for _ in range(N + 1)]
for i in range(4, N + 1):
    fibb[i] = fibb[i - 1] + fibb[i - 3]

ans = fibb[N]

print(ans)