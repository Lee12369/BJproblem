stack = []
lst = list(input().replace('()','2').replace('[]','3'))

for curr in lst:
    stack.append(curr)
    
    if len(stack) > 2:
        if curr == ')' and stack[-2].isnumeric() and stack[-3] == '(':
            temp = str(int(stack[-2]) * 2)
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(temp)
            curr = temp

        if curr == ']' and stack[-2].isnumeric() and stack[-3] == '[':
            temp = str(int(stack[-2]) * 3)
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append(temp)
            curr = temp
    
    if len(stack) > 1: 
        if curr.isnumeric() and stack[-2].isnumeric():
            temp = str(int(curr) + int(stack[-2]))
            stack.pop()
            stack.pop()
            stack.append(temp)
            curr = temp

if len(stack) == 1 and stack[0].isnumeric():
    print(stack[0])

else:
    print(0)