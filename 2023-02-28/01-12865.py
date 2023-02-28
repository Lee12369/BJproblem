import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp_W = [0]
dp_V = [0]
max_V = 0
cnt = 1
for i in range(N):
    for j in range(cnt):
        W = arr[i][0] + dp_W[j]
        if W <= K:
            V = arr[i][1] + dp_V[j]
            dp_W.append(W)
            dp_V.append(V)
            cnt += 1
            if V > max_V:
                max_V = V

print(max_V)
    