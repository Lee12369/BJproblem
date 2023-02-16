N = int(input())

sum = [0]
answer = 1
for i in range(1, N + 1):
    M = sum[i - 1] + i
    sum.append(M)
    if M > N:
        answer = i - 1
        break

print(answer)
