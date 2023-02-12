N = int(input())

i = 0
while 2 ** i < N:
    i += 1

left = 0
right = 2 ** i
cnt = 0
while True:
    if N == 1:
        break 

    mid = (left + right) // 2
    if mid < N:
        N -= mid
        cnt += 1
    right = mid

answer = cnt % 2

print(answer)