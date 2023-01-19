N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
    
        sum_AB = A[i][j] + B[i][j]
    
        print(sum_AB,end=' ')
    
    print()
