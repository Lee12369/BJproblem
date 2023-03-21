from fractions import Fraction

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    N = Fraction(a, b)

    ans = int(b)
    i = 2
    while N:
        M = Fraction(1, i)

        if N >= M:
            N -= M
            if N.numerator == 1:
                ans = N.denominator
                break
        i += 1   

    print(ans)
    