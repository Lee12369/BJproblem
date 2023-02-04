N, K = map(int, input().split())
A = list(map(int, input().split()))

if K != 1:
    pre = A[0] + sum(A[-K + 1:])
else:
    pre = A[0]

max_tasty = pre

for i in range(1, N):
    sum_tasty = pre - A[- K + i] + A[i]
    max_tasty = max(max_tasty, sum_tasty)
    pre = sum_tasty

print(max_tasty)