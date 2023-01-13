num = input('').split()
N = int(num[0])
X = int(num[1])
A = input('').split()
for i in range(N):
    if int(A[i]) < X:
        print(A[i], end=' ')
