equation = input()


def get_sum(equation):
    i = 0
    N = len(equation)
    while True:
        start_1st = i
        while i < N and equation[i].isnumeric():
            i += 1

        if i == N:
            return equation

        end_1st = i
        first = int(equation[start_1st : end_1st])
        
        
        if equation[i] == '+':
            i += 1
            start_2nd = i
            while i < N and equation[i].isnumeric():
                i += 1
            end_2nd = i
            second = int(equation[start_2nd : end_2nd])
            sum = str(first + second)
            equation = equation[:start_1st] + sum + equation[end_2nd:]
            i = start_1st
            N = len(equation)
        else:
            i += 1

def get_diff(equation):
    i = 0
    N = len(equation)
    while True:
        start_1st = i
        while i < N and equation[i].isnumeric():
            i += 1
        
        if i == N:
            return equation
            
        end_1st = i
        print(start_1st, end_1st)
        first = int(equation[start_1st : end_1st])
        
        if equation[i] == '-':
            i += 1
            start_2nd = i
            while i < N and equation[i].isnumeric():
                i += 1
            end_2nd = i
            second = int(equation[start_2nd : end_2nd])
            diff = str(first - second)
            equation = equation[:start_1st] + diff + equation[end_2nd:]
            i = start_1st
            N = len(equation)
        else:
            i += 1

equation = get_sum(equation)
# answer = get_diff(equation)

print(equation)