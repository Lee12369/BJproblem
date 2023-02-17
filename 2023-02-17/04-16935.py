A, B = input().split()
A = int(A)

check = 0
cnt = 1

while B:
    if A == int(B):
        check = 1
        break

    if B[-1] == '1':
        B = B[:-1]
        cnt += 1

    elif int(B[-1]) % 2 == 0:
        B = str(int(B) // 2)
        cnt += 1

    else:
        break

if check == 1:
    print(cnt)
else:
    print(-1)