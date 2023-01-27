T = int(input())

Y_grade = 0
K_grade = 0
for _ in range(T):
    for _ in range(9):
        Y, K = map(int, input().split())

        Y_grade += Y
        K_grade += K

    if Y_grade > K_grade:
        print("Yonsei")

    elif Y_grade < K_grade:
        print("Korea")

    else:
        print("Draw")
