T = int(input())
for _ in range(T):
    N = int(input())
    dic = {}
    for i in range(1, N + 1):
        dic[i] = int(input())

    cnt = 0
    curr = 1
    check = 0   
    while cnt < N:
        if curr == N:
            check = 1
            break

        curr = dic[curr]
        cnt += 1
    

    if check == 1:
        print(cnt)
    else:
        print(0)

        