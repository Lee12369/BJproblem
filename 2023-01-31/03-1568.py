N = int(input())

i = 1
cnt = 0
while N != 0:
    if i > N:
        i = 1
    N -= i
    cnt += 1
    i += 1

print(cnt)