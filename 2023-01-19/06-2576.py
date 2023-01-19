N = [int(input()) for _ in range(7)]
odd_N = []
for x in N:
    if x % 2 == 1:
        odd_N.append(x)

if odd_N != []:
    odd_sum = sum(odd_N)
    odd_min = min(odd_N)
    
    print(odd_sum)
    print(odd_min)

else:
    print(-1)

