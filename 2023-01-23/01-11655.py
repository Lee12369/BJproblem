lst = list(input())

for x in lst:
    if x.isalpha():
        x_ord = ord(x)
        if ord(x) >= 110:
            print(chr(x_ord - 13), end='')
        
        elif ord(x) >= 97:
            print(chr(x_ord + 13), end='')

        elif ord(x) >= 78:
            print(chr(x_ord - 13), end='')
        
        else:
            print(chr(x_ord + 13), end='')
        
    else:
        print(x, end='')