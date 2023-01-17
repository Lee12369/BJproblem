N = True
while N:
    N = int(input())
    if N == 0:
        break
    N_list = list(str(N))
    N_length = len(N_list)
    M = [0 for i in range(N_length)]

    N_index = N_length - 1
    for i in range(N_length):
        M[i] = N_list[N_index - i]

    if N_list == M:
        print("yes")
    else:
        print("no")    