import sys
N, M = map(int, sys.stdin.readline().split())
NM = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().split())
MK = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]



answer_arr = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        temp = 0
    
        for k in range(M):
            temp += NM[i][k] * MK[k][j]
    
        answer_arr[i][j] = temp

for lists in answer_arr:
    
    for x in lists:
        print(x, end=' ')
    
    print()