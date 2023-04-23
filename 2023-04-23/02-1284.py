while True:
    id = input()
    if id == '0':
        break

    length = len(id) + 1
    for num in id:
        if num == '1':
            length += 2
        
        elif num == '0':
            length += 4
        
        else:
            length += 3
    
    print(length)