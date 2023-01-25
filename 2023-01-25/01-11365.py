while True:
    lst = input()
    
    if lst == 'END':
        break
    
    lst_rev = list(reversed(lst))
    
    for x in lst_rev:
        print(x, end='')
    
    print()
    