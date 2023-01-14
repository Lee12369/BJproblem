except_numbers = [0 for i in range(10000)]
for i in range(0, 10000):
    temp = i
    thousand = temp//1000
    temp %= 1000 
    hundred = temp//100
    temp %= 100
    ten = temp//10
    temp %= 10
    one = temp
    except_numbers[i] = i + thousand + hundred + ten + one
for i in range(1,10000):
    if i not in except_numbers:
        print(i)