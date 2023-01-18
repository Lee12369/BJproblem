M = [0 for _ in range(4)]
for i in range(4):
    M[i] = list(map(int, input().split()))
    
N =[0 for _ in range(3)]

for i in range(3):
    if i == 0:
        N[0] = M[0][1]

    N[i] = N[i-1]  + M[i][1]  - M[i][0]

print(max(N))
