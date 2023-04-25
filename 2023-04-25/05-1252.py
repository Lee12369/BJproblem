A, B = input().split()

A = int(A, 2)
B = int(B, 2)

ans = bin(A + B)

print(ans[2:])