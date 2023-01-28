month, day = [int(input()) for _ in range(2)]

if month == 2 and day == 18:
    print("Special")

elif (month == 2 and day < 18) or month < 2:
    print("Before")

else:
    print("After")