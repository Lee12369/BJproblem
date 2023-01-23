A, B, C, D = [int(input()) for _ in range(4)]

sum_ABCD = A + B + C + D

x = sum_ABCD // 60
y = sum_ABCD % 60

print(x)
print(y)