import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

students = [1 for _ in range(N + 3)]

sleeps = list(map(int, input().split()))
attends = list(map(int, input().split()))

attends = list(set(attends) - set(sleeps))

for num in attends:
    R = (N + 2) // num
    for i in range(1, R + 1):
        students[num * i] = 0

for num in sleeps:
    students[num] = 1

accumulation_sum = [0 for _ in range(N + 3)]
for i in range(N):
    accumulation_sum[i + 3] = students[i + 3] + accumulation_sum[i + 2]



for _ in range(M):
    S, E = map(int, input().split())
    
    ans = accumulation_sum[E] - accumulation_sum[S - 1]

    print(ans)