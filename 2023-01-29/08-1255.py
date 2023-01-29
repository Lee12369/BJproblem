A, B = input().split()
A =list(map(int, list(A)))
B =list(map(int, list(B)))

dic = {}
sum_A = sum(A)
for i in range(10):
    dic[i] = sum_A * i

sum_AxB = 0
for b in B:
    sum_AxB += dic[b]

print(sum_AxB) 