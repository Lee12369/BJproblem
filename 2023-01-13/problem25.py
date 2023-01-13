A = int(input())
B = int(input())
C = int(input())
num = str(A*B*C)
for i in range(10):
    cnt = num.count('{}'.format(i))
    print(cnt)

