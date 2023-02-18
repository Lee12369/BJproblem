import sys
input = sys.stdin.readline

fibb = {
    0 : [1, 0],
    1 : [0, 1]
}
for x in range(2, 41):
    a = fibb[x - 1][0] + fibb[x - 2][0]
    b = fibb[x - 1][1] + fibb[x - 2][1]
    fibb[x] = [a, b]

T = int(input())

for _ in range(T):
    N = int(input())
    
    ans = fibb[N]

    print(ans[0], ans[1])