lst = [i ** 2 for i in range(1, 101)]

M, N = [int(input()) for _ in range(2)]

answers = []

for x in lst:
    if M <= x <= N:
        answers.append(x)


if answers:
    ans_sum = sum(answers)
    ans_min = answers[0]

    print(ans_sum)
    print(ans_min)

else :
    print(-1)