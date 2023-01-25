A, B = list(input().split())

A = A.replace('6','5')
B = B.replace('6','5')

min_sumAB = int(A) + int(B)

A = A.replace('5','6')
B = B.replace('5','6')

max_sumAB = int(A) + int(B)

print(min_sumAB, max_sumAB)