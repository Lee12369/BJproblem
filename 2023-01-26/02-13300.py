import sys
import math
N, M = map(int, input().split())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

student_n = []

for i in range(2):
    for j in range(1, 7):
        cnt = lst.count([i, j])
        student_n.append(cnt)

answer = 0
for x in student_n:
    answer += math.ceil(x / M)

print(answer)