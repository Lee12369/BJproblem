N = int(input())
numbers = [0,1]
if N <= 1:
    print(numbers[N])
else:
    for i in range(2,N+1):
        numbers.append(numbers[i-1] + numbers[i-2])
    print(numbers[-1])