import sys
while True:
    lst = list(sys.stdin.readline().rstrip('\n'))

    if not lst:
        break

    low_alpha_N, up_alpha_N, number_N, empty_N = 0, 0, 0, 0 

    for x in lst:
        if x.islower():
            low_alpha_N += 1

        elif x.isupper():
            up_alpha_N += 1
        
        elif x.isnumeric():
            number_N += 1 
        
        elif x.isspace():
            empty_N += 1

    answer = [low_alpha_N, up_alpha_N, number_N, empty_N]

    for x in answer:
        print(x, end=' ')