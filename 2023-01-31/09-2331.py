A, P = map(int, input().split())

lst = [A]

while True:
    M = len(str(lst[-1]))
    digits = []
    for i in range(M):
        dg = (lst[-1] % (10 ** (i + 1))) // (10 ** i)
        digits.append(dg)
        
    # thousand_digit = lst[-1] // 1000
    # hundred_digit = (lst[-1] % 1000) // 100
    # ten_digit = (lst[-1] % 100) // 10
    # one_digit = lst[-1] % 10

    N = 0
    for x in digits:
        N += x ** P 
    
    if N in lst:
        break
    else:
        lst.append(N)

idx = lst.index(N)
lst = lst[:idx]
answer = len(lst)

print(answer)