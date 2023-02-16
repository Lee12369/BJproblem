N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

sum = 0
for i in range(N):
    max_num = max(B)
    sum += A[i] * max(B)
    B.remove(max_num)

print(sum)