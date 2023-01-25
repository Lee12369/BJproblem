T = int(input())

for _ in range(T):
    N = int(input())
    answer = []

    while N:
        N , res = divmod(N, 2)
        answer.append(res)

    for idx, x in enumerate(answer):
        if x:
            print(idx, end=' ')
    print()
