N = int(input())

for number in range(N, 0, -1):
    check = 1
    for num in str(number):
        if num != '4' and num != '7':
            check = 0
            break
        
    if check == 1:
        print(number)
        break
