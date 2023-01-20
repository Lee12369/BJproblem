N = int(input())
lst = list([int(input()) for _ in range(N)])

if lst.count(1) > lst.count(0):
    print("Junhee is cute!")

else:
    print("Junhee is not cute!")