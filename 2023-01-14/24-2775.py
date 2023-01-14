import math
N = int(input())
for i in range(N):
    k, n = [int(input()) for i in range(2)]
    answer = math.factorial(n+k)/math.factorial(k+1)/math.factorial(n-1)
    print(int(answer))