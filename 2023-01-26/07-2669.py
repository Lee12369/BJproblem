arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            arr[i][j] = 1

answer = 0
for lst in arr:
    answer += lst.count(1)

print(answer)