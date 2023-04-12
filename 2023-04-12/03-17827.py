import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
C = list(map(int, input().split()))


for _ in range(M):
    number = int(input())
    head = V - 1
    rotate = N - head
    if number >= N:
        number -= N
        idx = number % rotate + head
    else:
        idx = number
    
    ans = C[idx]

    print(ans)

