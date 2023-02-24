fibb = [0 for _ in range(68)]
fibb[0] = 1
fibb[1] = 1
fibb[2] = 2
fibb[3] = 4

for i in range(4, 68):
    fibb[i] = fibb[i - 1] + fibb[i - 2] + fibb[i - 3] + fibb[i - 4]

T = int(input())
for _ in range(T):
    N = int(input())

    ans = fibb[N]

    print(ans)
