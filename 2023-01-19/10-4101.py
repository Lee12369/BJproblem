while True:
    N = list(map(int,input().split()))

    if N == [0,0]:
        break

    if N[0] > N[1]:
        print("Yes")
    else:
        print("No")