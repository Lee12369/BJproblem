dic = {}
for i in range(10):
    dic[str(i)] = i

for i in range(65,91):
    dic[chr(i)] = i -55

N, B = input().split()

N = list(N)
B = int(B)

N.reverse()

answer = 0
for digit, key in enumerate(N):
    answer += dic[key] * (B ** digit)

print(answer)
