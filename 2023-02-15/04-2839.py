N = int(input())

M = N // 5
answer = 0
for i in range(M, -1, -1):
    M_rem = N - i * 5
    K = M_rem // 3
    K_rem = M_rem % 3
    if K_rem == 0:
        answer = i + K
        break

if answer > 0:
    print(answer)
else:
    print(-1)