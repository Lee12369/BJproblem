def go_stack(input_word):
    word = input_word[:3]
    error_check = 0
    if word == 'NUM':
        x = int(input_word[4:])
        stack.append(x)
    
    if len(stack) == 0:
        error_check = 1
        return error_check
    
    if word == 'POP':
        stack.pop()

    elif word == 'INV':
        stack[-1] = -stack[-1]

    elif word == 'DUP':
        stack.append(stack[-1])
    
    elif word == 'SWP':
        if len(stack) >= 2:
            stack[-2], stack[-1] = stack[-1], stack[-2]
        else:
            error_check = 1

    elif word == 'ADD':    
        if len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            cal_num = num1 + num2
            if abs(cal_num) <= INF:
                stack.append(cal_num)
            else:
                error_check = 1
        else:
            error_check = 1

    elif word == 'SUB':    
        if len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            cal_num = num2 - num1
            if abs(cal_num) <= INF:
                stack.append(cal_num)
            else:
                error_check = 1
        else:
            error_check = 1

    elif word == 'MUL':
        if len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            cal_num = num1 * num2
            if abs(cal_num) <= INF:
                stack.append(cal_num)
            else:
                error_check = 1
        else:
            error_check = 1

    elif word == 'DIV':
        if len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            if num1 == 0:
                error_check = 1

            elif (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0): 
                stack.append(num2 // num1)
            
            else:
                stack.append(-(-num2 // num1))
        else:
            error_check = 1      

    elif word == 'MOD':
        if len(stack) >= 2:
            num1 = stack.pop()
            num2 = stack.pop()
            if num1 == 0:
                error_check = 1

            elif num2 > 0:
                stack.append(abs(num2) % abs(num1))
             
            elif num2 <= 0:
                stack.append(-(abs(num2) % abs(num1)))
        else:
            error_check = 1

    return error_check

INF = int(1e9)
while True:
    input_words = []
    quit_check = 0
    while True:
        word = input()
        if word == 'END':
            break
        if word == 'QUIT':
            quit_check = 1
            break
        input_words.append(word)
    
    if quit_check == 1:
        break

    N = int(input())
    for _ in range(N):
        number = int(input())
        stack = [number]
        for x in input_words:
            error_check = go_stack(x)
            if error_check == 1:
                stack = []
                break
        
        if len(stack) == 1:
            print(stack[0])
        else:
            print('ERROR')
    print()
