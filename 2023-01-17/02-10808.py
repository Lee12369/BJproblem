S = input()
alphabet = [chr(i) for i in range(97,123)]
for x in alphabet:
    cts = 0
    for y in S:
        if x == y:
            cts += 1
    print(cts, end=' ')
