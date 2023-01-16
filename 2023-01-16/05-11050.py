import math
N, K = map(int,input().split())

answer = int(math.factorial(N)/(math.factorial(K) * math.factorial(N - K)))

print(answer)