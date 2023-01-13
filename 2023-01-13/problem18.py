N = int(input('')) 
digit10 = int(N/10)
digit1 = N % 10
count = 0
if digit10 == 0 :
    digit10 = digit1
    count +=1
K = digit10 + digit1
while N - K:
    sum = digit10 + digit1
    digit10 = digit1
    if sum < 10:
        digit1 = sum
    else :
        digit1 =  sum % 10
    K = digit10*10 +digit1
    count += 1
print(count)

