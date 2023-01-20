L, P = map(int, input().split())
N = L * P
M = list(map(int, input().split()))

for x in M:
    answer = x - N
    
    print(answer, end= ' ')
