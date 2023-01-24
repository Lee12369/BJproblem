X, Y = input().split()

X_rev = X[-1::-1]
Y_rev = Y[-1::-1]

XY = int(X_rev) + int(Y_rev)

answer = str(XY)[-1::-1].lstrip('0')

print(answer)
