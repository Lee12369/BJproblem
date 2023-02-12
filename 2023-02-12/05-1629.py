A, B, C = map(int, input().split())

def recurr(A, B, C):
    if B == 1:
        return A % C
    
    N = B % 2
    B //= 2

    if N == 0:
        return (recurr(A, B, C) ** 2) % C
    elif N == 1:
        return ((recurr(A, B, C) ** 2) * A) % C

answer = recurr(A, B, C)

print(answer)