num = input('').split()
A = int(num[0])
B = int(num[1])
C = int(num[2])

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
