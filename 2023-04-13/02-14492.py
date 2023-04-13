import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def calc(x, y):
    for i in range(N):
        if A[x][i] and B[i][y]:
            return 1
    
    return 0

ans = 0
for i in range(N):
    for j in range(N):
        ans += calc(i, j)

print(ans)