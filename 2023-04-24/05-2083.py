while True:
    name, age, weight = input().split()
    if name == '#' and age == '0' and weight == '0':
        break

    if int(age) > 17 or int(weight) >= 80:
        print("{} Senior".format(name))
    
    else:
        print("{} Junior".format(name))