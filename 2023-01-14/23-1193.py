N = int(input())
sum = 0
cts = 0
for i in range(1,N+1):
    sum += i
    cts += 1
    if N <= sum:
        break
gap = sum-N
if cts % 2:
    print("{}/{}".format(gap+1,cts-gap))
else:
    print("{}/{}".format(cts-gap,gap+1))
