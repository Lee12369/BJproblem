import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    A = A[1:]

    B = list(map(int, input().split()))
    B = B[1:]

    winner = 'D'
    for i in range(4, 0, -1):
        A_cnt = A.count(i)
        B_cnt = B.count(i)
        if A_cnt > B_cnt:
            winner = 'A'
            break 

        elif A_cnt < B_cnt:
            winner = 'B'
            break
    
    print(winner)