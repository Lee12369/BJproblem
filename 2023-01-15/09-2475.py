numbers = map(int,input().split())
sum_square = 0
for i in numbers:
    sum_square += i**2
answer = sum_square % 10
print(answer)